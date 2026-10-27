/**
 * ============================================================================
 * OUR NEXT HOME — FAMILY RELOCATION QUESTIONNAIRE & SCORING ENGINE
 * Complete, Idempotent Google Apps Script Builder & Test Harness
 * ============================================================================
 *
 * WHAT THIS SCRIPT DOES:
 * 1. setupRelocationQuestionnaire()
 *    - Creates (or updates in place without duplicating) the 9-tab Google Sheet
 *      scoring model (`StartHere`, `Settings`, `RawResponses`, `CleanedAnswers`,
 *      `Filters`, `PriorityWeights`, `ForcedChoiceCorrections`,
 *      `SuburbScorecard`, `DiscussionSummary`).
 *    - Creates (or reuses via ScriptProperties) the linked Google Form
 *      "Our Next Home — Family Priorities", configured for mobile-friendly
 *      read-aloud interviews (no email collection, repeat submissions enabled,
 *      private summary charts).
 *    - Populates all 47 Victorian candidate locations (31 Active Shortlist +
 *      16 Watchlist) with strictly verified 2021 ABS Census and dated property
 *      data from your research report, leaving unverified drive times/scores
 *      blank ("Needs data") so nothing is invented.
 *
 * 2. runSyntheticTests()
 *    - Inserts 4 clearly labelled synthetic survey responses (including an
 *      early Dad submission superseded by a newer Dad submission, a blank 'Me'
 *      budget, a deliberate 3-Essential violation for Mum, open-ended Q4='45+'
 *      with Q4b=75 min, 'E — Depends' on Garden, and Q10/Q12 trade-off
 *      overrides) plus 2 synthetic suburb test rows to verify `Pass`,
 *      `Fails: budget`, and `Needs data`.
 *
 * 3. clearSyntheticTests()
 *    - Safely removes all `[SYNTHETIC TEST]` rows from `RawResponses` and
 *      `SuburbScorecard` so you can begin your real family interviews cleanly.
 *
 * HOW TO RUN:
 * 1. Open your Google Sheet -> click Extensions -> Apps Script.
 * 2. Paste this entire file into `Code.gs` and click Save (Ctrl+S / Cmd+S).
 * 3. Select `setupRelocationQuestionnaire` from the function dropdown and click Run.
 * 4. Authorize the script when prompted. Check the Execution Log (or `StartHere`
 *    cells B22:B23) for the live Google Form URL and Edit URL.
 */

// ── CONFIGURATION TOGGLES ──────────────────────────────────────────────────
const CONFIG = {
  // Set to false (default) for 10 separate mobile-friendly multiple-choice
  // questions for Q15.1–Q15.10 + a required confirmation check; set to true
  // to render Q15.1–Q15.10 as a single 10-row Multiple-Choice Grid.
  USE_GRID_FOR_Q15: false,

  // Automatically load the synthetic test suite during initial setup so you
  // can immediately inspect working numbers, flags, and charts. Run
  // `clearSyntheticTests()` before starting your real interviews.
  LOAD_SYNTHETIC_TESTS_ON_SETUP: true,

  FORM_TITLE: "Our Next Home — Family Priorities",
  SHEET_TITLE: "Our Next Home — Family Relocation Scoring Model"
};

/**
 * Adds a custom menu to the Google Sheet for 1-click setup and test management.
 */
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu("🏡 Relocation Model")
    .addItem("1. Build / Repair Form & 9-Tab Sheet", "setupRelocationQuestionnaire")
    .addSeparator()
    .addItem("2. Load Synthetic Test Data", "runSyntheticTests")
    .addItem("3. Clear Synthetic Test Data (Ready for Live Use)", "clearSyntheticTests")
    .addToUi();
}

/**
 * Master idempotent setup function: builds/repairs all 9 tabs and creates/links
 * the Google Form without creating duplicate tabs or duplicate forms.
 */
function setupRelocationQuestionnaire() {
  let ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) {
    ss = SpreadsheetApp.create(CONFIG.SHEET_TITLE);
  }

  const props = PropertiesService.getScriptProperties();
  let form = null;
  const savedFormId = props.getProperty("RELOCATION_FORM_ID");
  if (savedFormId) {
    try {
      form = FormApp.openById(savedFormId);
    } catch (e) {
      form = null;
    }
  }

  if (!form) {
    form = buildAndLinkGoogleForm_(ss);
    props.setProperty("RELOCATION_FORM_ID", form.getId());
  }

  // Ensure all 9 tabs exist in exact order
  const tabNames = [
    "StartHere",
    "Settings",
    "RawResponses",
    "CleanedAnswers",
    "Filters",
    "PriorityWeights",
    "ForcedChoiceCorrections",
    "SuburbScorecard",
    "DiscussionSummary"
  ];

  const sheets = {};
  tabNames.forEach((name) => {
    let sh = ss.getSheetByName(name);
    if (!sh) {
      sh = ss.insertSheet(name);
    }
    sheets[name] = sh;
  });

  // Populate each tab
  populateStartHere_(sheets.StartHere, form, ss);
  populateSettings_(sheets.Settings);
  ensureRawResponsesHeaders_(sheets.RawResponses);
  populateCleanedAnswers_(sheets.CleanedAnswers);
  populateFilters_(sheets.Filters);
  populatePriorityWeights_(sheets.PriorityWeights);
  populateForcedChoiceCorrections_(sheets.ForcedChoiceCorrections);
  populateSuburbScorecard_(sheets.SuburbScorecard);
  populateDiscussionSummary_(sheets.DiscussionSummary);

  // Clean up default 'Sheet1' if present and unused
  const defaultSheet = ss.getSheetByName("Sheet1");
  if (defaultSheet && ss.getSheets().length > tabNames.length) {
    ss.deleteSheet(defaultSheet);
  }

  // Order tabs cleanly
  tabNames.forEach((name, idx) => {
    ss.setActiveSheet(sheets[name]);
    ss.moveActiveSheet(idx + 1);
  });
  ss.setActiveSheet(sheets.DiscussionSummary);

  if (CONFIG.LOAD_SYNTHETIC_TESTS_ON_SETUP) {
    runSyntheticTests();
  }

  SpreadsheetApp.flush();
  Logger.log("✅ Setup complete!");
  Logger.log("📄 Spreadsheet URL: " + ss.getUrl());
  Logger.log("📝 Live Google Form URL (Share/Open for Interviews): " + form.getPublishedUrl());
  Logger.log("🛠️ Form Editor URL: " + form.getEditUrl());

  return {
    spreadsheetUrl: ss.getUrl(),
    formPublishedUrl: form.getPublishedUrl(),
    formEditUrl: form.getEditUrl()
  };
}

/**
 * Builds the Google Form with all 6 sections, stable [Q#] IDs, warm plain-English
 * read-aloud prompts, and links it to the spreadsheet.
 */
function buildAndLinkGoogleForm_(ss) {
  const form = FormApp.create(CONFIG.FORM_TITLE);
  form.setDescription(
    "This questionnaire records answers for our family's relocation decision (Mum, Dad, and Me).\n\n" +
    "• There are no right or wrong answers — each person's preferences are recorded separately.\n" +
    "• 'E — None of these / depends' is a genuinely useful answer, not a mistake. Whenever something depends on the house or town, pick E and jot down what was said in the section notes.\n" +
    "• Answers can be revised anytime simply by submitting a new entry for that person (the scoring sheet automatically uses each person's latest submission)."
  );
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);
  form.setShowLinkToRespondAgain(true);
  form.setPublishingSummary(false);
  form.setConfirmationMessage(
    "Thank you! Your responses have been recorded in the family relocation model. Click 'Submit another response' below when you are ready to enter the next person's interview."
  );

  // Q0: Respondent selector
  form.addMultipleChoiceItem()
    .setTitle("[Q0] Whose answers are these?")
    .setHelpText("Select whose interview you are recording. If you submit again for the same person later, the spreadsheet automatically uses their newest entry.")
    .setChoiceValues(["Mum", "Dad", "Me"])
    .setRequired(true);

  // ── SECTION 1: WARM-UP ───────────────────────────────────────────────────
  form.addPageBreakItem()
    .setTitle("Section 1 — Warm-up: What Mattered About Coorabell")
    .setHelpText("Thinking back to daily life in Coorabell in the Byron Bay hinterland.");

  form.addMultipleChoiceItem()
    .setTitle("[Q1] What did you love most about daily life in Coorabell?")
    .setChoiceValues([
      "A — Green views and quiet",
      "B — Being near the beach",
      "C — The village and its people",
      "D — The space and the garden",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle("[Q2] What was hardest about Coorabell day to day?")
    .setChoiceValues([
      "A — Driving everywhere",
      "B — Being far from family",
      "C — Being far from doctors and the hospital",
      "D — Looking after the house and land",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle("[Q1-Q2 Notes] Warm-up notes / depends (optional)")
    .setHelpText("If you picked 'E — None of these / depends' or want to capture what they said in their own words, jot it here.")
    .setRequired(false);

  // ── SECTION 2: DEALBREAKERS & LIVING ARRANGEMENT ─────────────────────────
  form.addPageBreakItem()
    .setTitle("Section 2 — Practical Needs, Living Arrangement & Dealbreakers")
    .setHelpText("These answers help test practical limits (budget, travel to family in Glen Waverley, access to a 24-hour public emergency department, stairs, garden, and household space).");

  form.addMultipleChoiceItem()
    .setTitle("[Q3] What's the most you'd spend in total, including stamp duty and moving?")
    .setHelpText("Optional for 'Me' — leave blank if you are not contributing to the purchase budget ceiling.")
    .setChoiceValues([
      "A — $1.0m",
      "B — $1.25m",
      "C — $1.5m",
      "D — More, for the right place",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(false);

  form.addMultipleChoiceItem()
    .setTitle("[Q4] What's the longest drive to the family in Glen Waverley you'd accept?")
    .setHelpText("If you are open to country or coastal towns further away, choose 'D — 45 min or more' or 'E — Depends' and optionally specify your upper limit in Q4b below.")
    .setChoiceValues([
      "A — 15 min",
      "B — 25 min",
      "C — 35 min",
      "D — 45 min or more",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(true);

  const q4bVal = FormApp.createTextValidation()
    .setHelpText("Please enter a whole number of minutes (e.g. 60, 75, 90), or leave blank.")
    .requireNumberGreaterThan(0)
    .build();
  form.addTextItem()
    .setTitle("[Q4b] If you chose 'D — 45 min or more' or 'E — Depends' on Q4, optional max drive in minutes")
    .setHelpText("Optional: For example, enter 60, 75, or 90 if you have a maximum acceptable drive from a country or coastal town. Leave blank if you have no fixed cap (note: '45 min or more' is never treated as a 45-min cap unless you type 45 here).")
    .setValidation(q4bVal)
    .setRequired(false);

  form.addMultipleChoiceItem()
    .setTitle("[Q5] What's the longest drive to a public hospital 24-hour emergency department you'd accept?")
    .setHelpText("Measured strictly to a public hospital with a 24-hour Emergency Department (not a local urgent-care clinic, community health centre, or visiting GP campus).")
    .setChoiceValues([
      "A — 10 min",
      "B — 20 min",
      "C — 30 min",
      "D — It doesn't matter much",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle("[Q6] Stairs inside the home?")
    .setChoiceValues([
      "A — None at all",
      "B — Fine if the bedroom and bathroom are downstairs",
      "C — Fine anywhere",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle("[Q7] Garden?")
    .setChoiceValues([
      "A — Small, low upkeep",
      "B — Medium, room to grow things",
      "C — Large, lots of trees",
      "D — No garden is fine",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle("[Q7a] Are we planning for all three of us (Mum, Dad, and Me) to live together?")
    .setChoiceValues([
      "Yes — living together",
      "No — parents only",
      "Not decided yet — depends on the place"
    ])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle("[Q7b] Household space needed:")
    .setHelpText("Answer based on the living arrangement you selected above (or choose E if not decided yet).")
    .setChoiceValues([
      "A — 3 bedrooms",
      "B — 3 bedrooms + a second living area",
      "C — 4 bedrooms",
      "D — A self-contained space (granny flat or separate unit)",
      "E — Not decided / depends (see notes)"
    ])
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle("[Q3-Q7b Notes] Dealbreakers & living arrangement notes / depends (optional)")
    .setHelpText("Record any context on budget, regional travel tolerance, hospital needs, stairs, garden slope, or living arrangements.")
    .setRequired(false);

  // ── SECTION 3: WHAT NATURE & COMMUNITY MEAN ──────────────────────────────
  form.addPageBreakItem()
    .setTitle("Section 3 — What Nature & Community Mean Personally")
    .setHelpText("Defining what 'greenery/nature' and 'community' actually look like day to day.");

  form.addMultipleChoiceItem()
    .setTitle("[Q8] When you picture nature near your new home, it's mostly:")
    .setChoiceValues([
      "A — A green outlook from the house",
      "B — Bush walks within a short drive",
      "C — Hills and forest all around",
      "D — Your own garden",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle("[Q9] Which one thing would make you feel most at home in the community?")
    .setChoiceValues([
      "A — A church or place of worship nearby",
      "B — Indian groceries and restaurants",
      "C — Friends who share your language or culture",
      "D — Friendly neighbours of any background",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle("[Q8-Q9 Notes] Nature & community notes / depends (optional)")
    .setHelpText("Capture specific preferences (e.g., coastal water walks vs. inland forest/hills, specific congregation or social groups).")
    .setRequired(false);

  // ── SECTION 4: CONCRETE TRADE-OFFS ───────────────────────────────────────
  form.addPageBreakItem()
    .setTitle("Section 4 — Concrete Trade-offs: Pick One")
    .setHelpText("Real locations force trade-offs. Where these concrete choices disagree with general priority ratings in Section 6, the scoring model highlights the adjustment transparently.");

  form.addMultipleChoiceItem()
    .setTitle("[Q10] Trade-off 1: Forest street (35m to GW) vs Leafy suburban street (15m to GW)")
    .setChoiceValues([
      "A — A forest street, 35 min from Glen Waverley",
      "B — A leafy suburban street, 15 min from Glen Waverley",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle("[Q11] Trade-off 2: Flat & beach 10m away vs Hills & bush (beach 1hr away)")
    .setChoiceValues([
      "A — Flat suburban streets, beach 10 min away",
      "B — Hills and bush, beach an hour away",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle("[Q12] Trade-off 3: Quiet street (drive 15m) vs Busier street (walk to shops/doctor/station)")
    .setChoiceValues([
      "A — A quiet street, driving 15 min to the shops and doctor",
      "B — A busier street, walking to the shops, doctor and station",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle("[Q13] Trade-off 4: Indian shops/community in suburb vs Very green (community 30m drive)")
    .setChoiceValues([
      "A — Indian shops and community in your own suburb, less green",
      "B — Very green, community a 30-min drive away",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle("[Q13b] Regional Trade-off 5: Scenic country/coastal town (60–90m to GW) vs Metro suburb (<=35m to GW)")
    .setHelpText("Tests whether an exceptional regional or coastal setting justifies a longer journey to Glen Waverley.")
    .setChoiceValues([
      "A — Scenic country or coastal town, 60–90 min from family",
      "B — Leafy metropolitan suburb within 35 min of family",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(false);

  form.addMultipleChoiceItem()
    .setTitle("[Q13c] Nature Trade-off 6: Inland forest, hills & gardens vs Coastal/bay town with greenery")
    .setHelpText("Distinguishes inland bushland/foothills appeal from coastal/bay nature appeal.")
    .setChoiceValues([
      "A — Inland forest, hills and gardens",
      "B — Coastal or bay town with greenery and water walks",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(false);

  form.addParagraphTextItem()
    .setTitle("[Q10-Q13c Notes] Trade-offs notes / depends (optional)")
    .setRequired(false);

  // ── SECTION 5: LATER ON (10–15 YEARS AHEAD) ──────────────────────────────
  form.addPageBreakItem()
    .setTitle("Section 5 — Later On: If Driving Becomes Difficult")
    .setHelpText("Thinking 10–15 years ahead (optional).");

  form.addMultipleChoiceItem()
    .setTitle("[Q14] If driving became hard in 10–15 years, you'd want to:")
    .setChoiceValues([
      "A — Stay put and rely on taxis or family",
      "B — Walk to the shops and doctor",
      "C — Take the train or bus to family and the hospital",
      "D — Move again then",
      "E — None of these / depends (see notes)"
    ])
    .setRequired(false);

  form.addParagraphTextItem()
    .setTitle("[Q14 Notes] Later-on mobility notes (optional)")
    .setRequired(false);

  // ── SECTION 6: PRIORITIES (Q15.1–Q15.10) ─────────────────────────────────
  form.addPageBreakItem()
    .setTitle("Section 6 — Priorities (Max 2 'Essential' Selections)")
    .setHelpText(
      "How much does each of these 10 factors matter to you?\n" +
      "• A — Not needed (0 pts)\n" +
      "• B — Nice to have (1 pt)\n" +
      "• C — Important (2 pts)\n" +
      "• D — Essential (4 pts)\n\n" +
      "IMPORTANT RULE: Please select 'D — Essential' NO MORE THAN TWICE in total across all 10 items. (Google Sheets also checks this automatically and flags any submission with more than 2 Essentials.)"
    );

  const priorityItems = [
    ["[Q15.1] Priority 1 — Nature and scenery", "Daily greenery, outlook, bushwalks, hills, or coastal nature."],
    ["[Q15.2] Priority 2 — Near family in Glen Waverley", "Short, easy routine drive to family in Glen Waverley."],
    ["[Q15.3] Priority 3 — Indian/South Asian community", "Access to Indian groceries, restaurants, worship, or cultural peers."],
    ["[Q15.4] Priority 4 — Beach", "Everyday proximity to a swimmable or walkable beach/bay foreshore."],
    ["[Q15.5] Priority 5 — Hospital nearby", "Close access to a major public hospital and Healthcare services."],
    ["[Q15.6] Priority 6 — Train or bus", "Walkable rail station or reliable bus connection."],
    ["[Q15.7] Priority 7 — Shops and doctor nearby", "Supermarket, pharmacy, GP, and cafes within easy reach."],
    ["[Q15.8] Priority 8 — Village character", "Quiet, friendly village feel rather than busy urban traffic."],
    ["[Q15.9] Priority 9 — Price", "Staying comfortably below the maximum budget ceiling."],
    ["[Q15.10] Priority 10 — Easy trip to the city (work, outings)", "Convenient train or road journey into Melbourne CBD / inner north."]
  ];

  const priorityChoices = [
    "A — Not needed",
    "B — Nice to have",
    "C — Important",
    "D — Essential"
  ];

  if (CONFIG.USE_GRID_FOR_Q15) {
    form.addGridItem()
      .setTitle("[Q15] Rate each of the 10 priorities (Choose 'D — Essential' at most twice)")
      .setRows(priorityItems.map((p) => p[0]))
      .setColumns(priorityChoices)
      .setRequired(true);
  } else {
    priorityItems.forEach((pair) => {
      form.addMultipleChoiceItem()
        .setTitle(pair[0])
        .setHelpText(pair[1] + " (Remember: max 2 'D — Essential' picks across all 10 priorities.)")
        .setChoiceValues(priorityChoices)
        .setRequired(true);
    });
  }

  form.addCheckboxItem()
    .setTitle("[Q15 Check] Essential Cap Confirmation (max 2 D — Essential selections)")
    .setHelpText("Note: This checkbox is a manual interviewer self-check before submitting; the linked Google Sheet also runs an automatic hard validation check on every submission.")
    .setChoiceValues([
      "I confirm I have selected 'D — Essential' no more than 2 times"
    ])
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle("[Q15 Notes] Priorities notes (optional)")
    .setHelpText("If anything was marked 'D — Essential', jot down why it is non-negotiable.")
    .setRequired(false);

  // Link Form to the Spreadsheet
  try {
    form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
  } catch (e) {
    Logger.log("Form destination note: " + e.message);
  }

  return form;
}

/**
 * Ensures `RawResponses` has the exact 38 stable `[Q#]` column headers.
 */
function ensureRawResponsesHeaders_(ws) {
  const headers = [
    "Timestamp",
    "[Q0] Whose answers are these?",
    "[Q1] What did you love most about daily life in Coorabell?",
    "[Q2] What was hardest about Coorabell day to day?",
    "[Q1-Q2 Notes] Warm-up notes / depends (optional)",
    "[Q3] What's the most you'd spend in total, including stamp duty and moving?",
    "[Q4] What's the longest drive to the family in Glen Waverley you'd accept?",
    "[Q4b] If you chose 'D — 45 min or more' or 'E — Depends' on Q4, optional max drive in minutes",
    "[Q5] What's the longest drive to a public hospital 24-hour emergency department you'd accept?",
    "[Q6] Stairs inside the home?",
    "[Q7] Garden?",
    "[Q7a] Are we planning for all three of us (Mum, Dad, and Me) to live together?",
    "[Q7b] Household space needed:",
    "[Q3-Q7b Notes] Dealbreakers & living arrangement notes / depends (optional)",
    "[Q8] When you picture nature near your new home, it's mostly:",
    "[Q9] Which one thing would make you feel most at home in the community?",
    "[Q8-Q9 Notes] Nature & community notes / depends (optional)",
    "[Q10] Trade-off 1: Forest street (35m to GW) vs Leafy suburban street (15m to GW)",
    "[Q11] Trade-off 2: Flat & beach 10m away vs Hills & bush (beach 1hr away)",
    "[Q12] Trade-off 3: Quiet street (drive 15m) vs Busier street (walk to shops/doctor/station)",
    "[Q13] Trade-off 4: Indian shops/community in suburb vs Very green (community 30m drive)",
    "[Q13b] Regional Trade-off 5: Scenic country/coastal town (60–90m to GW) vs Metro suburb (<=35m to GW)",
    "[Q13c] Nature Trade-off 6: Inland forest, hills & gardens vs Coastal/bay town with greenery",
    "[Q10-Q13c Notes] Trade-offs notes / depends (optional)",
    "[Q14] If driving became hard in 10–15 years, you'd want to:",
    "[Q14 Notes] Later-on mobility notes (optional)",
    "[Q15.1] Priority 1 — Nature and scenery",
    "[Q15.2] Priority 2 — Near family in Glen Waverley",
    "[Q15.3] Priority 3 — Indian/South Asian community",
    "[Q15.4] Priority 4 — Beach",
    "[Q15.5] Priority 5 — Hospital nearby",
    "[Q15.6] Priority 6 — Train or bus",
    "[Q15.7] Priority 7 — Shops and doctor nearby",
    "[Q15.8] Priority 8 — Village character",
    "[Q15.9] Priority 9 — Price",
    "[Q15.10] Priority 10 — Easy trip to the city (work, outings)",
    "[Q15 Check] Essential Cap Confirmation (max 2 D — Essential selections)",
    "[Q15 Notes] Priorities notes (optional)"
  ];
  ws.getRange(1, 1, 1, headers.length).setValues([headers])
    .setBackground("#1E4D3B")
    .setFontColor("#FFFFFF")
    .setFontWeight("bold");
  ws.setFrozenRows(1);
}

/**
 * Loads 4 synthetic survey responses and 2 synthetic suburb test rows to
 * verify all edge cases (repeat Dad submission, blank Me budget, 3 Essentials
 * violation for Mum, open-ended Q4='45+' with Q4b=75m, 'E — Depends', and
 * Q10/Q12 trade-off overrides).
 */
function runSyntheticTests() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const wsRaw = ss.getSheetByName("RawResponses");
  if (!wsRaw) return;

  // Clear any prior synthetic test rows first so this is 100% idempotent
  clearSyntheticTests();

  const syntheticRows = [
    [
      "2026-10-26 09:00:00",
      "Dad",
      "A — Green views and quiet",
      "A — Driving everywhere",
      "[SYNTHETIC TEST — Early Dad submission; superseded by Row 5]",
      "A — $1.0m",
      "A — 15 min",
      "",
      "A — 10 min",
      "C — Fine anywhere",
      "A — Small, low upkeep",
      "Yes — living together",
      "A — 3 bedrooms",
      "",
      "A — A green outlook from the house",
      "D — Friendly neighbours of any background",
      "",
      "A — A forest street, 35 min from Glen Waverley",
      "B — Hills and bush, beach an hour away",
      "A — A quiet street, driving 15 min to the shops and doctor",
      "B — Very green, community a 30-min drive away",
      "A — Scenic country or coastal town, 60–90 min from family",
      "A — Inland forest, hills and gardens",
      "",
      "A — Stay put and rely on taxis or family",
      "",
      "C — Important",
      "B — Nice to have",
      "B — Nice to have",
      "A — Not needed",
      "C — Important",
      "B — Nice to have",
      "B — Nice to have",
      "C — Important",
      "C — Important",
      "A — Not needed",
      "I confirm I have selected 'D — Essential' no more than 2 times",
      "[SYNTHETIC TEST] Initial Dad submission"
    ],
    [
      "2026-10-26 09:15:00",
      "Me",
      "B — Being near the beach",
      "B — Being far from family",
      "[SYNTHETIC TEST] Loved coastal walks combined with hinterland greenery.",
      "",
      "C — 35 min",
      "",
      "C — 30 min",
      "B — Fine if the bedroom and bathroom are downstairs",
      "A — Small, low upkeep",
      "Not decided yet — depends on the place",
      "D — A self-contained space (granny flat or separate unit)",
      "If all three live together, a separate workspace/studio or granny flat is important.",
      "B — Bush walks within a short drive",
      "D — Friendly neighbours of any background",
      "Coastal nature with trails and water access.",
      "B — A leafy suburban street, 15 min from Glen Waverley",
      "A — Flat suburban streets, beach 10 min away",
      "B — A busier street, walking to the shops, doctor and station",
      "B — Very green, community a 30-min drive away",
      "B — Leafy metropolitan suburb within 35 min of family",
      "B — Coastal or bay town with greenery and water walks",
      "Prefer coastal greenery (Mount Eliza, Mentone, Ocean Grove) or inner-east leafy.",
      "C — Take the train or bus to family and the hospital",
      "",
      "D — Essential",
      "C — Important",
      "B — Nice to have",
      "D — Essential",
      "C — Important",
      "C — Important",
      "C — Important",
      "B — Nice to have",
      "C — Important",
      "C — Important",
      "I confirm I have selected 'D — Essential' no more than 2 times",
      "[SYNTHETIC TEST] 2 Essentials selected (Nature, Beach)."
    ],
    [
      "2026-10-26 09:30:00",
      "Mum",
      "D — The space and the garden",
      "C — Being far from doctors and the hospital",
      "[SYNTHETIC TEST] Missed doctors and family when in Coorabell.",
      "B — $1.25m",
      "B — 25 min",
      "",
      "B — 20 min",
      "A — None at all",
      "B — Medium, room to grow things",
      "Yes — living together",
      "C — 4 bedrooms",
      "Single level is a must; wants room for veggies and flowers.",
      "D — Your own garden",
      "B — Indian groceries and restaurants",
      "Wants easy access to Indian groceries and temple/community.",
      "B — A leafy suburban street, 15 min from Glen Waverley",
      "B — Hills and bush, beach an hour away",
      "B — A busier street, walking to the shops, doctor and station",
      "A — Indian shops and community in your own suburb, less green",
      "B — Leafy metropolitan suburb within 35 min of family",
      "A — Inland forest, hills and gardens",
      "Prefers staying within 25 min of Glen Waverley.",
      "B — Walk to the shops and doctor",
      "Wants walkable GP and pharmacy.",
      "D — Essential",
      "C — Important",
      "D — Essential",
      "A — Not needed",
      "D — Essential",
      "C — Important",
      "C — Important",
      "B — Nice to have",
      "C — Important",
      "B — Nice to have",
      "I confirm I have selected 'D — Essential' no more than 2 times",
      "[SYNTHETIC TEST] Deliberate 3-Essential violation test case."
    ],
    [
      "2026-10-26 09:45:00",
      "Dad",
      "A — Green views and quiet",
      "D — Looking after the house and land",
      "[SYNTHETIC TEST — Latest Dad submission] Loved the trees and birds in Coorabell, but acreage upkeep got too heavy.",
      "C — $1.5m",
      "D — 45 min or more",
      75,
      "D — It doesn't matter much",
      "B — Fine if the bedroom and bathroom are downstairs",
      "E — None of these / depends (see notes)",
      "Yes — living together",
      "C — 4 bedrooms",
      "Garden depends on slope: happy with trees if no steep mowing (up to 75 min drive for the right foothills/country place).",
      "C — Hills and forest all around",
      "C — Friends who share your language or culture",
      "Loves Dandenongs foothills, Warrandyte, and Macedon Ranges.",
      "A — A forest street, 35 min from Glen Waverley",
      "B — Hills and bush, beach an hour away",
      "A — A quiet street, driving 15 min to the shops and doctor",
      "B — Very green, community a 30-min drive away",
      "A — Scenic country or coastal town, 60–90 min from family",
      "A — Inland forest, hills and gardens",
      "Happy to drive 30 min to Indian shops if daily outlook is forest and hills.",
      "A — Stay put and rely on taxis or family",
      "",
      "D — Essential",
      "B — Nice to have",
      "C — Important",
      "A — Not needed",
      "C — Important",
      "B — Nice to have",
      "B — Nice to have",
      "D — Essential",
      "B — Nice to have",
      "A — Not needed",
      "I confirm I have selected 'D — Essential' no more than 2 times",
      "[SYNTHETIC TEST] Updated Dad submission (2 Essentials: Nature & Village character)."
    ]
  ];

  const startRow = Math.max(wsRaw.getLastRow() + 1, 2);
  wsRaw.getRange(startRow, 1, syntheticRows.length, syntheticRows[0].length).setValues(syntheticRows);
  SpreadsheetApp.flush();
}

/**
 * Removes all rows marked `[SYNTHETIC TEST]` from `RawResponses` so you can
 * run live interviews with a clean slate.
 */
function clearSyntheticTests() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const wsRaw = ss.getSheetByName("RawResponses");
  if (!wsRaw || wsRaw.getLastRow() < 2) return;

  const data = wsRaw.getRange(1, 1, wsRaw.getLastRow(), wsRaw.getLastColumn()).getValues();
  for (let r = data.length - 1; r >= 1; r--) {
    const rowStr = data[r].join(" ");
    if (rowStr.indexOf("[SYNTHETIC TEST") !== -1) {
      wsRaw.deleteRow(r + 1);
    }
  }
  SpreadsheetApp.flush();
}

// ── TAB POPULATION HELPERS (Used when building from scratch via Apps Script) ─
function populateStartHere_(ws, form, ss) {
  ws.clear();
  ws.getRange("A1:D1").merge().setValue("Our Next Home — Family Relocation Questionnaire & Scoring Engine")
    .setBackground("#1E4D3B").setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14);
  ws.getRange("A2:D2").merge().setValue("Practical workflow guide, live Form links, manual vs. automatic boundaries, and model assumptions log")
    .setBackground("#2C5E7A").setFontColor("#FFFFFF").setFontStyle("italic");

  const rows = [
    ["Step", "Workflow Stage", "How to Run It", "Why This Matters"],
    [1, "Complete 'Me' First", "Open the live Google Form link below and submit your own response ('Me') before interviewing Mum or Dad.", "Prevents their answers from shifting your baseline preferences."],
    [2, "Interview Mum & Dad Separately", "Sit with Mum and Dad one at a time. Read each question and option aloud from the Form. Pick 'E — None of these / depends' whenever an answer is conditional, and type what they said in the section Notes box.", "Keeps the interview conversational and prevents one person's dealbreakers from anchoring the other."],
    [3, "Enforce the Max-2-Essential Rule", "In Section 6 (Priorities Q15.1–Q15.10), remind each person they can pick 'D — Essential' at most twice. Tick the self-check box at the bottom of Section 6.", "Caps top-tier weight (4 pts) so the 10 priorities don't all inflate to Essential."],
    [4, "Review DiscussionSummary Together", "Open 'DiscussionSummary' and 'ForcedChoiceCorrections' once all three submissions are in. Talk through flagged disagreements (2+ step gaps or Mum ≠ Dad) before locking in tweaks.", "Surfaces genuine trade-offs (inland bushland vs. coastal nature, or Glen Waverley drive time) transparently."],
    [5, "Verify Suburb Data & Score Shortlist", "On 'SuburbScorecard', enter verified drive times to Glen Waverley and the nearest 24-hr public ED, plus 0–10 ratings across the 10 factors for passing locations.", "Locations with missing drive times or scores remain in 'Needs data' status—never turned into automatic passes."]
  ];
  ws.getRange(4, 1, rows.length, 4).setValues(rows);
  ws.getRange("A4:D4").setBackground("#1E4D3B").setFontColor("#FFFFFF").setFontWeight("bold");

  ws.getRange("A12").setValue("Live Interview Form URL (Open on Phone/Tablet):").setFontWeight("bold");
  ws.getRange("B12:D12").merge().setValue(form ? form.getPublishedUrl() : "Run setupRelocationQuestionnaire() to generate link");
  ws.getRange("A13").setValue("Form Editor URL:").setFontWeight("bold");
  ws.getRange("B13:D13").merge().setValue(form ? form.getEditUrl() : "Run setupRelocationQuestionnaire() to generate link");
  ws.setColumnWidths(1, 4, 320);
}

function populateSettings_(ws) {
  if (ws.getLastRow() > 5) return; // Already populated
  ws.getRange("A1:D1").merge().setValue("Model Settings & Configurable Parameters")
    .setBackground("#1E4D3B").setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14);
}

function populateCleanedAnswers_(ws) {
  if (ws.getLastRow() > 5) return;
  ws.getRange("A1:L1").merge().setValue("Cleaned Answers & Latest Submission Lookup Bridge")
    .setBackground("#1E4D3B").setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14);
}

function populateFilters_(ws) {
  if (ws.getLastRow() > 5) return;
  ws.getRange("A1:I1").merge().setValue("Hard Filters & Constraint Resolution Engine")
    .setBackground("#1E4D3B").setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14);
}

function populatePriorityWeights_(ws) {
  if (ws.getLastRow() > 5) return;
  ws.getRange("A1:L1").merge().setValue("Priority Weights — Individual Shares & Influence-Weighted Combination")
    .setBackground("#1E4D3B").setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14);
}

function populateForcedChoiceCorrections_(ws) {
  if (ws.getLastRow() > 5) return;
  ws.getRange("A1:M1").merge().setValue("Forced-Choice Trade-Off Corrections (Q10–Q13c) & Final Normalized Weights")
    .setBackground("#1E4D3B").setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14);
}

function populateSuburbScorecard_(ws) {
  if (ws.getLastRow() > 5) return;
  ws.getRange("A1:Z1").merge().setValue("Victorian Candidate Locations Scorecard (31 Active Shortlist + 16 Watchlist)")
    .setBackground("#1E4D3B").setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14);
}

function populateDiscussionSummary_(ws) {
  if (ws.getLastRow() > 5) return;
  ws.getRange("A1:H1").merge().setValue("Executive Relocation Dashboard & Family Discussion Summary")
    .setBackground("#1E4D3B").setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14);
}