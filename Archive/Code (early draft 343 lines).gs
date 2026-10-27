/**
 * Our Next Home — interview form for the Family Relocation Scoring Model.
 * Run setupRelocationQuestionnaire once. Safe to re-run: it reuses the same form.
 *
 * What it does:
 *  1. Creates the Google Form (or repairs a half-built one) and publishes it.
 *  2. Links responses to a tab called FormArchive (full answers, including notes).
 *  3. Adds a trigger that copies each new response into RawResponses, matched by
 *     question tag ([Q3], [Q15.1] …) so the existing scoring tabs keep working.
 *  4. First run only: clears the test rows in RawResponses (formulas kept) and
 *     deletes SuburbScorecard rows whose Location starts with "[SYNTHETIC TEST".
 *  5. Writes the form links to StartHere D2:E4 and the execution log.
 */
const CONFIG = {
  SPREADSHEET_ID: "1YLo1wotwy0p--_-X49kp46gPUH71A4RiKON3ZSjF-hs",
  FORM_TITLE: "Our Next Home — Family Priorities",
  START_SHEET: "StartHere",
  RAW_SHEET: "RawResponses",
  ARCHIVE_SHEET: "FormArchive",
  SCORECARD_SHEET: "SuburbScorecard",
  LINKS_RANGE: "D2:E4",
  TEST_MARKER: "[SYNTHETIC TEST",
  TRIGGER_HANDLER: "copyResponseToRaw"
};

const E_OPTION = "E — None of these / depends (see notes)";

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu("🏡 Relocation Model")
    .addItem("Set up or repair the form", "setupRelocationQuestionnaire")
    .addItem("Show form links", "showFormLinks")
    .addToUi();
}

function setupRelocationQuestionnaire() {
  const ss = getSpreadsheet_();
  requireSheets_(ss, [CONFIG.START_SHEET, CONFIG.RAW_SHEET, CONFIG.SCORECARD_SHEET]);
  const props = PropertiesService.getScriptProperties();

  // 1. Form: reuse if it exists; rebuild questions if a previous run stopped half-way.
  let form = null;
  const savedId = props.getProperty("FORM_ID");
  if (savedId) {
    try { form = FormApp.openById(savedId); } catch (e) { form = null; }
  }
  if (!form) {
    form = FormApp.create(CONFIG.FORM_TITLE);
    props.setProperty("FORM_ID", form.getId()); // saved at once so a retry never duplicates
    props.deleteProperty("FORM_BUILT");
  }
  if (props.getProperty("FORM_BUILT") !== "yes") {
    form.getItems().forEach(function (item) { form.deleteItem(item); });
    buildForm_(form);
    props.setProperty("FORM_BUILT", "yes");
  }

  // 2. Clear test data — first run only, before any live answer can exist.
  let cleared = "skipped (already done)";
  if (props.getProperty("TEST_DATA_CLEARED") !== "yes") {
    cleared = clearTestData_(ss);
    props.setProperty("TEST_DATA_CLEARED", "yes");
  }

  // 3. Responses: link to the spreadsheet, name the tab, add the copy trigger.
  let linked = false;
  try { linked = form.getDestinationId() === ss.getId(); } catch (e) { linked = false; }
  if (!linked) form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
  SpreadsheetApp.flush();
  nameArchiveSheet_(ss, form);
  ensureTrigger_(ss);

  // 4. Publish and accept responses (forms created by code may start unpublished).
  if (typeof form.setPublished === "function") form.setPublished(true);
  form.setAcceptingResponses(true);
  const published = typeof form.isPublished === "function" ? form.isPublished() : "unknown";

  // 5. Links.
  const formUrl = form.getPublishedUrl();
  const editUrl = form.getEditUrl();
  const linksWritten = writeLinks_(ss, formUrl, editUrl);

  Logger.log("SETUP OK");
  Logger.log("FORM_URL " + formUrl);
  Logger.log("EDIT_URL " + editUrl);
  Logger.log("PUBLISHED " + published);
  Logger.log("TEST DATA " + cleared);
  Logger.log("LINKS ON StartHere " + (linksWritten ? CONFIG.LINKS_RANGE : "NOT written — " + CONFIG.LINKS_RANGE + " was not empty"));
  return { formUrl: formUrl, editUrl: editUrl, published: published, cleared: cleared };
}

function showFormLinks() {
  const id = PropertiesService.getScriptProperties().getProperty("FORM_ID");
  const ui = SpreadsheetApp.getUi();
  if (!id) { ui.alert("No form yet. Run 'Set up or repair the form' first."); return; }
  const form = FormApp.openById(id);
  ui.alert("Interview form (share this):\n" + form.getPublishedUrl() + "\n\nForm editor (you only):\n" + form.getEditUrl());
}

/** Trigger handler: copy one form response into RawResponses, matched by [tag]. */
function copyResponseToRaw(e) {
  const ss = getSpreadsheet_();
  const raw = ss.getSheetByName(CONFIG.RAW_SHEET);
  const width = headerWidth_(raw);
  const headers = raw.getRange(1, 1, 1, width).getValues()[0];
  const row = buildRawRow_(headers, e.namedValues, new Date());
  raw.getRange(firstEmptyRow_(raw), 1, 1, width).setValues([row]);
}

// ---------------------------------------------------------------- helpers

function getSpreadsheet_() {
  return SpreadsheetApp.getActiveSpreadsheet() || SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID);
}

function requireSheets_(ss, names) {
  const missing = names.filter(function (n) { return !ss.getSheetByName(n); });
  if (missing.length) throw new Error("STOP: missing tab(s): " + missing.join(", ") + ". Nothing was changed.");
}

function tagOf_(title) {
  const m = String(title).match(/^\s*\[([^\]]+)\]/);
  return m ? m[1].trim() : null;
}

/** Pure function (tested offline): form answers → one RawResponses row in header order. */
function buildRawRow_(headers, namedValues, timestamp) {
  const byTag = {};
  const notes = [];
  Object.keys(namedValues || {}).forEach(function (title) {
    const tag = tagOf_(title);
    const value = [].concat(namedValues[title]).join(", ").trim();
    if (!tag || value === "") return;
    if (/notes$/i.test(tag) && tag !== "Q15 Notes") notes.push(tag.replace(/\s*notes$/i, "") + ": " + value);
    else if (tag === "Q15 Notes") notes.push("Q15: " + value);
    else byTag[tag] = /^\d+(\.\d+)?$/.test(value) ? Number(value) : value;
  });
  return headers.map(function (h) {
    if (String(h).trim().toLowerCase() === "timestamp") return timestamp;
    const tag = tagOf_(h);
    if (!tag) return "";
    if (tag === "Q15 Notes") return notes.join(" | ");
    return Object.prototype.hasOwnProperty.call(byTag, tag) ? byTag[tag] : "";
  });
}

function headerWidth_(sheet) {
  const row = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
  let w = row.length;
  while (w > 0 && String(row[w - 1]).trim() === "") w--;
  return w;
}

function firstEmptyRow_(sheet) {
  const last = Math.max(sheet.getLastRow(), 1);
  const colA = sheet.getRange(1, 1, last, 1).getValues();
  let r = colA.length;
  while (r > 1 && String(colA[r - 1][0]).trim() === "") r--;
  return r + 1;
}

/** Clears RawResponses answer cells (keeps any formulas) and deletes marked scorecard rows. */
function clearTestData_(ss) {
  const raw = ss.getSheetByName(CONFIG.RAW_SHEET);
  let rawRows = 0;
  if (raw.getLastRow() > 1) {
    const width = headerWidth_(raw);
    const range = raw.getRange(2, 1, raw.getLastRow() - 1, width);
    const formulas = range.getFormulas();
    const values = range.getValues();
    rawRows = values.filter(function (r) { return r.join("").trim() !== ""; }).length;
    range.setValues(formulas.map(function (row) { return row.map(function (f) { return f || ""; }); }));
  }
  const sc = ss.getSheetByName(CONFIG.SCORECARD_SHEET);
  let removed = 0;
  const names = sc.getRange(1, 1, Math.max(sc.getLastRow(), 1), 1).getValues();
  for (let r = names.length; r >= 2; r--) {
    if (String(names[r - 1][0]).trim().indexOf(CONFIG.TEST_MARKER) === 0) { sc.deleteRow(r); removed++; }
  }
  const left = sc.getRange(1, 1, Math.max(sc.getLastRow(), 1), 1).getValues().slice(1)
    .filter(function (r) { return String(r[0]).trim() !== ""; }).length;
  return "cleared " + rawRows + " RawResponses row(s); removed " + removed + " SuburbScorecard test row(s); " + left + " locations remain";
}

function nameArchiveSheet_(ss, form) {
  ss.getSheets().forEach(function (s) {
    const url = s.getFormUrl();
    if (!url || s.getName() === CONFIG.ARCHIVE_SHEET) return;
    try {
      if (FormApp.openByUrl(url).getId() === form.getId()) s.setName(CONFIG.ARCHIVE_SHEET);
    } catch (e) {
      Logger.log("Could not rename response tab '" + s.getName() + "': " + e.message);
    }
  });
}

function ensureTrigger_(ss) {
  const exists = ScriptApp.getProjectTriggers().some(function (t) {
    return t.getHandlerFunction() === CONFIG.TRIGGER_HANDLER;
  });
  if (!exists) ScriptApp.newTrigger(CONFIG.TRIGGER_HANDLER).forSpreadsheet(ss).onFormSubmit().create();
}

function writeLinks_(ss, formUrl, editUrl) {
  const range = ss.getSheetByName(CONFIG.START_SHEET).getRange(CONFIG.LINKS_RANGE);
  const current = range.getValues();
  const empty = current.every(function (r) { return r.join("").trim() === ""; });
  if (!empty && String(current[0][0]).trim() !== "Form links") return false;
  range.setValues([
    ["Form links", ""],
    ["Interview form (share this)", formUrl],
    ["Form editor (you only)", editUrl]
  ]);
  range.getCell(1, 1).setFontWeight("bold");
  return true;
}

// ---------------------------------------------------------------- form content

function withE_(choices) { return choices.concat([E_OPTION]); }

function mc_(form, title, choices, required, help) {
  const item = form.addMultipleChoiceItem().setTitle(title).setChoiceValues(choices).setRequired(required);
  if (help) item.setHelpText(help);
  return item;
}

function notes_(form, title, help) {
  const item = form.addParagraphTextItem().setTitle(title).setRequired(false);
  if (help) item.setHelpText(help);
}

function page_(form, title, help) {
  const item = form.addPageBreakItem().setTitle(title);
  if (help) item.setHelpText(help);
}

function buildForm_(form) {
  form.setTitle(CONFIG.FORM_TITLE)
    .setDescription(
      "Answers for our family's move (Mum, Dad and Me), one person per submission.\n" +
      "• There are no right or wrong answers.\n" +
      "• 'E — None of these / depends' is a real answer. Pick it and write what was said in that section's notes.\n" +
      "• To change answers, submit again for the same person; the sheet uses their latest entry.")
    .setCollectEmail(false)
    .setLimitOneResponsePerUser(false)
    .setShowLinkToRespondAgain(true)
    .setPublishingSummary(false)
    .setConfirmationMessage("Saved. Click 'Submit another response' for the next person.");

  mc_(form, "[Q0] Whose answers are these?", ["Mum", "Dad", "Me"], true);

  page_(form, "1 — Coorabell", "Thinking back to daily life in Coorabell.");
  mc_(form, "[Q1] What did you love most about daily life in Coorabell?", withE_([
    "A — Green views and quiet", "B — Being near the beach",
    "C — The village and its people", "D — The space and the garden"]), true);
  mc_(form, "[Q2] What was hardest about Coorabell day to day?", withE_([
    "A — Driving everywhere", "B — Being far from family",
    "C — Being far from doctors and the hospital", "D — Looking after the house and land"]), true);
  notes_(form, "[Q1-Q2 Notes] Notes (optional)");

  page_(form, "2 — Dealbreakers and living arrangement");
  mc_(form, "[Q3] What's the most you'd spend in total, including stamp duty and moving?", withE_([
    "A — $1.0m", "B — $1.25m", "C — $1.5m", "D — More, for the right place"]), false,
    "Me: leave blank if you're not contributing to the purchase.");
  mc_(form, "[Q4] What's the longest drive to the family in Glen Waverley you'd accept?", withE_([
    "A — 15 min", "B — 25 min", "C — 35 min", "D — 45 min or more"]), true);
  form.addTextItem()
    .setTitle("[Q4b] If D or E on Q4: your maximum drive in minutes (optional)")
    .setHelpText("E.g. 60, 75 or 90. Leave blank if there's no fixed limit.")
    .setValidation(FormApp.createTextValidation()
      .setHelpText("Enter a number of minutes, or leave blank.")
      .requireNumberGreaterThan(0).build())
    .setRequired(false);
  mc_(form, "[Q5] What's the longest drive to a public hospital emergency department (24-hour) you'd accept?", withE_([
    "A — 10 min", "B — 20 min", "C — 30 min", "D — It doesn't matter much"]), true,
    "A public hospital with a 24-hour emergency department, not an urgent-care clinic.");
  mc_(form, "[Q6] Stairs inside the home?", withE_([
    "A — None at all", "B — Fine if the bedroom and bathroom are downstairs", "C — Fine anywhere"]), true);
  mc_(form, "[Q7] Garden?", withE_([
    "A — Small, low upkeep", "B — Medium, room to grow things",
    "C — Large, lots of trees", "D — No garden is fine"]), true);
  mc_(form, "[Q7a] Are we planning for all three of us to live together?", [
    "Yes — living together", "No — parents only", "Not decided yet — depends on the place"], true);
  mc_(form, "[Q7b] Household space needed:", [
    "A — 3 bedrooms", "B — 3 bedrooms + a second living area", "C — 4 bedrooms",
    "D — A self-contained space (granny flat or separate unit)", "E — Not decided / depends (see notes)"], true);
  notes_(form, "[Q3-Q7b Notes] Notes (optional)");

  page_(form, "3 — What nature and community mean to you");
  mc_(form, "[Q8] When you picture nature near your new home, it's mostly:", withE_([
    "A — A green outlook from the house", "B — Bush walks within a short drive",
    "C — Hills and forest all around", "D — Your own garden"]), true);
  mc_(form, "[Q9] Which one thing would make you feel most at home in the community?", withE_([
    "A — A church or place of worship nearby", "B — Indian groceries and restaurants",
    "C — Friends who share your language or culture", "D — Friendly neighbours of any background"]), true);
  notes_(form, "[Q8-Q9 Notes] Notes (optional)");

  page_(form, "4 — Pick one", "Real places force trade-offs. Pick the one you'd actually choose.");
  mc_(form, "[Q10] Which would you choose?", withE_([
    "A — A forest street, 35 min from Glen Waverley",
    "B — A leafy suburban street, 15 min from Glen Waverley"]), true);
  mc_(form, "[Q11] Which would you choose?", withE_([
    "A — Flat suburban streets, beach 10 min away", "B — Hills and bush, beach an hour away"]), true);
  mc_(form, "[Q12] Which would you choose?", withE_([
    "A — A quiet street, driving 15 min to the shops and doctor",
    "B — A busier street, walking to the shops, doctor and station"]), true);
  mc_(form, "[Q13] Which would you choose?", withE_([
    "A — Indian shops and community in your own suburb, less green",
    "B — Very green, community a 30-min drive away"]), true);
  mc_(form, "[Q13b] Which would you choose? (optional)", withE_([
    "A — Scenic country or coastal town, 60–90 min from family",
    "B — Leafy metropolitan suburb within 35 min of family"]), false);
  mc_(form, "[Q13c] Which would you choose? (optional)", withE_([
    "A — Inland forest, hills and gardens",
    "B — Coastal or bay town with greenery and water walks"]), false);
  notes_(form, "[Q10-Q13c Notes] Notes (optional)");

  page_(form, "5 — Later on (optional)", "Thinking 10–15 years ahead.");
  mc_(form, "[Q14] If driving became hard in 10–15 years, you'd want to:", withE_([
    "A — Stay put and rely on taxis or family", "B — Walk to the shops and doctor",
    "C — Take the train or bus to family and the hospital", "D — Move again then"]), false);
  notes_(form, "[Q14 Notes] Notes (optional)");

  page_(form, "6 — Priorities",
    "How much does each of these matter to you?\n" +
    "A — Not needed · B — Nice to have · C — Important · D — Essential\n\n" +
    "Choose D (Essential) for no more than TWO items. The sheet flags more than two.");
  const levels = ["A — Not needed", "B — Nice to have", "C — Important", "D — Essential"];
  [
    ["[Q15.1] Nature and scenery", "Greenery, outlook, bush walks, hills or coastal nature."],
    ["[Q15.2] Near family in Glen Waverley", "An easy routine drive to family."],
    ["[Q15.3] Indian/South Asian community", "Groceries, restaurants, worship or cultural peers."],
    ["[Q15.4] Beach", "A walkable or swimmable beach or bay close by."],
    ["[Q15.5] Hospital nearby", "Quick access to a major public hospital."],
    ["[Q15.6] Train or bus", "A walkable station or reliable bus."],
    ["[Q15.7] Shops and doctor nearby", "Supermarket, pharmacy and GP within easy reach."],
    ["[Q15.8] Village character", "Quiet, friendly village feel."],
    ["[Q15.9] Price", "Staying comfortably under the budget."],
    ["[Q15.10] Easy trip to the city (work, outings)", "A convenient trip into Melbourne."]
  ].forEach(function (p) { mc_(form, p[0], levels, true, p[1]); });
  notes_(form, "[Q15 Notes] Notes (optional)", "If anything is Essential, note why.");
}
