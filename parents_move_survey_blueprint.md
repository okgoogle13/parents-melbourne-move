# Family Move Priorities: Survey & Scoring Blueprint

## 1. Format & Platform Comparison

To replace or supplement your shared Excel workbook (`Parents_move_priorities_survey.xlsx`) while letting you enter all three interviews yourself and automatically run your multi-stage scoring model, here is how the six options compare:

| 

| **Option** | **Ease of Setup & Maintenance** | **Submitting 3 Labelled Responses (Mum, Dad, Me)** | **Automatic Response Collection** | **Scoring, Max-2-Essential Rule & Forced-Choice Corrections** | **Suburb Ranking & Filtering** | **Overall Fit for 3-Person Family Decision** | 
| **Google Forms + Google Sheets** *(Recommended)* | **High.** Takes \~20 mins to set up the Form; your existing Excel formulas translate directly to Google Sheets (`INDEX/MATCH`, `SUMPRODUCT`, `TEXTJOIN`). | **Seamless.** A required first question (`Whose answers are these?`) tags each submission; click *Submit another response* to run all three from one link. | **Automatic.** Every submission appends a timestamped row to `Form Responses 1` in real time. | **Full engine in Sheets; soft warning in Forms.** Google Forms cannot natively count "Essential" picks across 10 separate questions before submit, unless you use a rotated Grid trick (see Section 3.1). Sheets flags violations immediately and calculates all forced-choice transfers. | **Excellent.** Native `SUMPRODUCT` and `RANK` / `FILTER` formulas dynamically score and rank only passing suburbs. | **Best overall balance** of zero-cost cloud access, clean interview UI, and full spreadsheet formula power. | 
| **Form + Existing Excel Workbook** *(Hybrid Runner-Up)* | **Very High.** Zero formula migration—your existing `.xlsx` workbook is already built and tested. | **Seamless.** Any form (or Microsoft Forms) collects the 3 rows, or you paste/link them into `Survey!H5:J30`. | **Semi-automatic** (if pasting) or **Automatic** (if using **Microsoft Forms + Excel for the Web** on OneDrive). | **100% Native.** Your `Calc` and `Results` sheets already implement the exact `0/1/2/4` scoring, `Max 2 D's` check, and `0.02` margin forced-choice overrides. | **100% Native.** The `Suburb scorecard` tab is already pre-loaded with your 10 Melbourne suburbs and `Pass`/`Fails` logic. | **Best low-effort shortcut** if you just want a cleaner interview screen on your phone/tablet without rebuilding formulas. | 
| **Microsoft Forms + Excel** | **High** (if using OneDrive/M365). Same formula power as your current workbook. | **Seamless.** Identical `Whose answers are these?` radio button workflow. | **Automatic** only when the workbook is hosted in OneDrive/SharePoint (Desktop-only forms require manual sync/download). | **Full engine in Excel; no cross-question count in MS Forms.** Like Google Forms, MS Forms cannot count answers across 10 separate questions mid-form. | **Excellent.** Identical to your existing workbook. | **Great alternative** if your family already uses OneDrive/Office 365 rather than Google Drive. | 
| **Tally or Jotform + Google Sheets** | **Medium.** Requires a third-party account, configuring conditional logic blocks, and integrating a webhook/sync to Sheets. | **Seamless.** Supports hidden or visible respondent selector fields. | **Automatic** via native Google Sheets integration. | **Hard enforcement possible in Form.** Both Tally (via calculated fields/variables) and Jotform can count how many times `Essential` is picked in real time and **block submission** or hide the submit button if `Count > 2`. | **Requires Sheets.** Neither tool can handle your multi-person weighted matrix + suburb scorecard natively; you still need Sheets for the back-end math. | **Best front-end upgrade** if you want hard in-form enforcement of the "max 2 Essentials" rule, linked to the same Google Sheet. | 
| **Airtable or Notion Forms** | **Low–Medium.** Relational databases require restructuring your flat matrix into linked tables (`Respondents`, `Priorities`, `Suburbs`). | **Good.** Easy to tag records by respondent. | **Automatic** into the database table. | **Awkward.** Cross-row matrix math (normalizing each person's column to 100%, then running pairwise forced-choice weight transfers across rows) is brittle and unnatural in Notion/Airtable compared to a spreadsheet grid. | **Medium.** Requires rollups and formula fields that are harder to audit than spreadsheet cells. | **Overkill and poorly suited** for matrix-style cross-person weight normalization and pairwise overrides. | 
| **Simple Custom Web App (HTML/JS)** | **Medium.** Requires maintaining code if you change questions or add suburbs, though an AI assistant can generate a single-file app quickly. | **Seamless.** Can present a 3-tab switcher (`Mum` | `Dad` | `Me`) in one screen. | **Local storage or export** unless wired to a Google Sheet/database backend. | **100% Enforceable.** Can disable the `Essential` radio buttons once 2 are selected and compute everything instantly. | **High**, if coded into the UI, but harder for you to tweak ad-hoc numbers during house hunting. | **Fun for a self-contained calculator**, but harder to maintain over months of property inspections than a Google Sheet. | 

## 2. Recommended Approach & Why

### Primary Recommendation: Google Forms + Google Sheets

Your instinct to use **Google Forms + Google Sheets** is spot-on, with two practical design enhancements that make it rock-solid for your specific workflow:

1. **Why it wins for the interviews:** Sitting with Mum or Dad with a full spreadsheet open is visually overwhelming—it exposes other people's columns, letter codes (`A/B/C/D`), and formula checks. A Google Form on your phone or tablet lets you focus on one plain-English question at a time, read the options aloud naturally, and tap the answer without anyone seeing the draft weights or other responses.

2. **Why it wins for the scoring model:** Your scoring algorithm is genuinely sophisticated—it normalizes each person's `0/1/2/4` scores into individual percentage shares (`I20:K29`), weights them by decision influence (`Say in the decision`), checks four specific pairwise trade-offs (`Q10–Q13`) against the combined weights, transfers `MIN(Loser_wt, (Loser_wt - Winner_wt + 0.02)/2)` from the losing priority to the winning priority when Q15 contradicts Q10–Q13, applies manual percentage-point tweaks, re-normalizes to 100%, and evaluates suburbs against three numerical hard filters (`Budget`, `Glen Waverley drive`, `ED drive`). A spreadsheet is the right tool for that math.

3. **Why you should use a Lookup Bridge (`Cleaned_Answers`) in Sheets:** Instead of writing complex formulas that try to calculate directly on the raw `Form Responses 1` tab, add a `Cleaned_Answers` tab that pulls the **latest** submission for `Mum`, `Dad`, and `Me` into the exact three-column layout (`Mum`, `Dad`, `Me`) of your current `Survey` tab. That way:

   * If you re-submit a form for Dad after a follow-up chat, the sheet automatically uses Dad's newest row without breaking a single formula.

   * Your existing workbook logic (`Calc`, `Results`, `Suburb scorecard`) works with almost zero structural changes.

### Challenge / Shortcut Worth Considering

Before you spend 30 minutes building the Google Form from scratch, consider the **5-Minute Hybrid Option**: upload your existing `Parents_move_priorities_survey.xlsx` directly to Google Drive, open it as a **Google Sheet**, and create the **Google Form** linked to it. Because your existing workbook already has all the formulas written on `Calc`, `Results`, and `Suburb scorecard`, linking the Form into the `Survey` tab via a 1-line `XLOOKUP` formula gives you a working system in a fraction of the time.

## 3. Complete Google Forms + Google Sheets Blueprint

### Part 1: Google Form Design

#### Title & Plain-English Introduction

* **Form Title:** `Parents' Move — Priorities & Suburb Survey`

* **Form Description / Intro:**

  > *This form records answers for our family housing move (Mum, Dad, and Me). Answer each question in your own words first—there are no right or wrong answers. If none of the options quite fit, pick "None of these / depends" and jot down what was actually said in the Notes box right below it.*

#### Respondent Identifier (Top of Section 1)

* **Question 0:** `Whose answers are these?`

  * **Type:** Multiple choice (Required)

  * **Options:**

    * `Mum`

    * `Dad`

    * `Me`

#### Section-by-Section Question Mapping

To keep your downstream formulas clean and human-readable while still matching your `A / B / C / D / E` workbook structure, prefix each option with its letter (`A — ...`, `B — ...`, `C — ...`, `D — ...`, `E — None of these / depends`). That lets Google Sheets extract the letter code with `LEFT(cell, 1)` while showing the full readable answer during the interview!

##### Section 1: Warm-up

*Description: Thinking back to daily life in Coorabell.*

1. **Q1 — What did you love most about daily life in Coorabell?**

   * **Type:** Multiple choice (Required)

   * **Options:**

     * `A — Green views and quiet`

     * `B — Being near the beach`

     * `C — The village and its people`

     * `D — The space and the garden`

     * `E — None of these / depends (see notes)`

   * **Follow-up field:** `Q1 Notes / depends (optional)` — *Short answer (Optional)*

2. **Q2 — What was hardest about Coorabell day to day?**

   * **Type:** Multiple choice (Required)

   * **Options:**

     * `A — Driving everywhere`

     * `B — Being far from family`

     * `C — Being far from doctors and the hospital`

     * `D — Looking after the house and land`

     * `E — None of these / depends (see notes)`

   * **Follow-up field:** `Q2 Notes / depends (optional)` — *Short answer (Optional)*

##### Section 2: Dealbreakers

*Description: Hard limits that rule suburbs or houses out (the strictest answer across the three of us wins).*

3. **Q3 — What's the most you'd spend in total, including stamp duty and moving?**

   * *Helper text:* Leave blank if you are not contributing to the budget limit.

   * **Type:** Multiple choice *(Optional — so "Me" can leave it blank if not contributing, matching your workbook note)*

   * **Options:**

     * `A — $1.0m`

     * `B — $1.25m`

     * `C — $1.5m`

     * `D — More, for the right place`

     * `E — None of these / depends (see notes)`

   * **Follow-up field:** `Q3 Notes / depends (optional)` — *Short answer (Optional)*

4. **Q4 — What's the longest drive to the family in Glen Waverley you'd accept?**

   * **Type:** Multiple choice (Required)

   * **Options:**

     * `A — 15 min`

     * `B — 25 min`

     * `C — 35 min`

     * `D — 45 min or more`

     * `E — None of these / depends (see notes)`

   * **Follow-up field:** `Q4 Notes / depends (optional)` — *Short answer (Optional)*

5. **Q5 — What's the longest drive to a hospital emergency department you'd accept?**

   * *Helper text:* Measured to a public hospital with a 24-hour emergency department.

   * **Type:** Multiple choice (Required)

   * **Options:**

     * `A — 10 min`

     * `B — 20 min`

     * `C — 30 min`

     * `D — It doesn't matter much`

     * `E — None of these / depends (see notes)`

   * **Follow-up field:** `Q5 Notes / depends (optional)` — *Short answer (Optional)*

6. **Q6 — Stairs inside the home?**

   * **Type:** Multiple choice (Required)

   * **Options:**

     * `A — None at all`

     * `B — Fine if the bedroom and bathroom are downstairs`

     * `C — Fine anywhere`

     * `E — None of these / depends (see notes)` *(Note: Option D is `—` in your workbook, so omit D)*

   * **Follow-up field:** `Q6 Notes / depends (optional)` — *Short answer (Optional)*

7. **Q7 — Garden?**

   * **Type:** Multiple choice (Required)

   * **Options:**

     * `A — Small, low upkeep`

     * `B — Medium, room to grow things`

     * `C — Large, lots of trees`

     * `D — No garden is fine`

     * `E — None of these / depends (see notes)`

   * **Follow-up field:** `Q7 Notes / depends (optional)` — *Short answer (Optional)*

8. **Q7b — With all three of us living together, the home needs:**

   * **Type:** Multiple choice (Required)

   * **Options:**

     * `A — 3 bedrooms`

     * `B — 3 bedrooms + a second living area`

     * `C — 4 bedrooms`

     * `D — A self-contained space (granny flat or separate unit)`

     * `E — None of these / depends (see notes)`

   * **Follow-up field:** `Q7b Notes / depends (optional)` — *Short answer (Optional)*

##### Section 3: What it means

*Description: Defining what "nature" and "community" actually look like day to day.*

 9. **Q8 — When you picture nature near your new home, it's mostly:**

    * **Type:** Multiple choice (Required)

    * **Options:**

      * `A — A green outlook from the house`

      * `B — Bush walks within a short drive`

      * `C — Hills and forest all around`

      * `D — Your own garden`

      * `E — None of these / depends (see notes)`

    * **Follow-up field:** `Q8 Notes / depends (optional)` — *Short answer (Optional)*

10. **Q9 — Which one thing would make you feel most at home in the community?**

    * **Type:** Multiple choice (Required)

    * **Options:**

      * `A — A church or place of worship nearby`

      * `B — Indian groceries and restaurants`

      * `C — Friends who share your language or culture`

      * `D — Friendly neighbours of any background`

      * `E — None of these / depends (see notes)`

    * **Follow-up field:** `Q9 Notes / depends (optional)` — *Short answer (Optional)*

##### Section 4: Trade-offs

*Description: Pick one in each pair. Where these answers disagree with your general priority ratings in Section 6, these concrete choices take precedence.*

11. **Q10 — Trade-off 1: Which would you choose?**

    * **Type:** Multiple choice (Required)

    * **Options:**

      * `A — A forest street, 35 min from Glen Waverley`

      * `B — A leafy suburban street, 15 min from Glen Waverley`

      * `E — None of these / depends (see notes)`

    * **Follow-up field:** `Q10 Notes / depends (optional)` — *Short answer (Optional)*

12. **Q11 — Trade-off 2: Which would you choose?**

    * **Type:** Multiple choice (Required)

    * **Options:**

      * `A — Flat suburban streets, beach 10 min away`

      * `B — Hills and bush, beach an hour away`

      * `E — None of these / depends (see notes)`

    * **Follow-up field:** `Q11 Notes / depends (optional)` — *Short answer (Optional)*

13. **Q12 — Trade-off 3: Which would you choose?**

    * **Type:** Multiple choice (Required)

    * **Options:**

      * `A — A quiet street, driving 15 min to the shops and doctor`

      * `B — A busier street, walking to the shops, doctor and station`

      * `E — None of these / depends (see notes)`

    * **Follow-up field:** `Q12 Notes / depends (optional)` — *Short answer (Optional)*

14. **Q13 — Trade-off 4: Which would you choose?**

    * **Type:** Multiple choice (Required)

    * **Options:**

      * `A — Indian shops and community in your own suburb, less green`

      * `B — Very green, community a 30-min drive away`

      * `E — None of these / depends (see notes)`

    * **Follow-up field:** `Q13 Notes / depends (optional)` — *Short answer (Optional)*

##### Section 5: Later on

*Description: Thinking 10–15 years ahead (optional).*

15. **Q14 — If driving became hard in 10–15 years, you'd want to:**

    * **Type:** Multiple choice (Optional)

    * **Options:**

      * `A — Stay put and rely on taxis or family`

      * `B — Walk to the shops and doctor`

      * `C — Take the train or bus to family and the hospital`

      * `D — Move again then`

      * `E — None of these / depends (see notes)`

    * **Follow-up field:** `Q14 Notes / depends (optional)` — *Short answer (Optional)*

##### Section 6: Priorities (Q15.1 to Q15.10)

*Description: How much does each of these matter to you? IMPORTANT: Pick "D — Essential" for NO MORE THAN TWO items in total across all 10 priorities.*

Create **10 separate Multiple Choice questions** (all Required), each using the exact same 4 options:

* `A — Not needed`

* `B — Nice to have`

* `C — Important`

* `D — Essential`

The 10 questions are: 16. **Q15.1 — Nature and scenery** 17. **Q15.2 — Near family in Glen Waverley** 18. **Q15.3 — Indian/South Asian community** 19. **Q15.4 — Beach** 20. **Q15.5 — Hospital nearby** 21. **Q15.6 — Train or bus** 22. **Q15.7 — Shops and doctor nearby** 23. **Q15.8 — Village character** 24. **Q15.9 — Price** 25. **Q15.10 — Easy trip to the city (work, outings)**

* **Follow-up field at end of Section 6:** `Q15 Notes (optional)` — *Short answer (Optional)*

#### How to Enforce or Warn About the "Maximum 2 Essential Answers" Rule

Because Google Forms evaluates validation rules per question rather than summing across 10 separate multiple-choice questions, you have three practical ways to handle this rule:

1. **Method A — Self-Check Confirmation Checkbox at the bottom of Section 6 (Recommended for 10 separate questions):**

   * Add a **Required Checkboxes** question right after `Q15.10`:

     * **Question:** `Essential Cap Check: Count how many times you selected "D — Essential" above.`

     * **Single Option:** `I confirm I have selected "D — Essential" no more than 2 times (currently 0, 1, or 2).`

   * Since you are filling out the form yourself, this acts as a mandatory stop-and-count gate before you hit Submit, while Google Sheets also runs the automated `=IF(COUNTIF(...)>2, "Too many D's", "OK")` banner on the dashboard.

2. **Method B — Multiple-Choice Grid on One Screen (Visual Scan Upgrade):**

   * Put Q15.1–Q15.10 inside a single **Multiple-choice grid** (Rows = the 10 priorities, Columns = `A — Not needed`, `B — Nice to have`, `C — Important`, `D — Essential`).

   * In Google Sheets, a grid still creates 10 separate columns automatically! And in the Form UI, all 10 radio buttons sit in four vertical columns on one screen, so you can visually count at a glance whether column 4 (`D — Essential`) has more than two dots before clicking Submit.

3. **Method C — Hard Block via Tally.so (If you want strict software blocking):**

   * If you use **Tally** instead of Google Forms (still synced to the exact same Google Sheet), you can add a Tally `Calculated Field` that adds `+1` whenever any of Q15.1–Q15.10 equals `D — Essential`, and a conditional block that hides the Submit button and shows a red banner (`Please change at least one Essential back to Important`) whenever `Essential_Count > 2`.

### Part 2: Google Sheets Scoring Model

#### Linking the Form & Proposed Tab Architecture

1. In Google Forms, go to the **Responses** tab and click **Link to Sheets** -> **Create a new spreadsheet** (name it `Parents_Move_Scoring_Model`).

2. Keep the auto-generated `Form Responses 1` tab untouched (rename it to `Raw_Responses`), and add 6 structured tabs alongside a small `Settings` block:

   * `Raw_Responses` *(Auto-populated by Google Forms—never edit manually)*

   * `Cleaned_Answers` *(Extracts the latest submission for Mum, Dad, and Me into clean columns and converts options to letters & scores)*

   * `Filters` *(Calculates the strictest hard filter across Mum, Dad, and Me)*

   * `Priority_Weights` *(Calculates individual `0/1/2/4` scores, normalizes to 100%, and applies configurable decision influence)*

   * `Forced_Choice_Corrections` *(Evaluates Q10–Q13 by decision influence, calculates weight transfers, and outputs final re-normalized weights)*

   * `Suburb_Scorecard` *(Applies active hard filters and final weights to candidate suburbs and ranks passing suburbs)*

   * `Discussion_Summary` *(Executive results dashboard: submission status, agreements/conflicts, active filters, final priority ranks, and top suburbs)*

#### Tab-by-Tab Structure & Exact Google Sheets Formulas

##### Tab 1: `Raw_Responses`

Google Forms automatically populates columns in order:

* `Col A`: `Timestamp`

* `Col B`: `Whose answers are these?` (`Mum`, `Dad`, or `Me`)

* `Col C` onward: Each question and optional note field from your Form.

##### Tab 2: `Cleaned_Answers` (Plus Configurable Settings)

This tab bridges the dynamic form rows into a clean, fixed table so downstream formulas never break when a new response arrives.

**Top Settings Block (`A1:C10` — Manual Inputs in Yellow):**

* `B2`: `1` (Say in the decision — Mum)

* `B3`: `1` (Say in the decision — Dad)

* `B4`: `1` (Say in the decision — Me; lower to `0.5` if Mum/Dad should carry more weight)

* `B5`: `2` (Max D answers per person)

* `B6`: `0.06` (Estimated purchase costs as % of price)

* `B7`: `0.02` (Forced-choice margin)

* **Score Lookup Table (`E2:F5`):**

  * `E2:F2` -> `A` | `0`

  * `E3:F3` -> `B` | `1`

  * `E4:F4` -> `C` | `2`

  * `E5:F5` -> `D` | `4`

**1. Identifying the latest row for Mum, Dad, and Me (`Row 12`):** If someone submits twice (e.g. you update Dad's answers), use `XLOOKUP` with `search_mode = -1` (search bottom-to-top) to always grab their **most recent submission**:

* **Mum's latest row index (`C12`):**

  ```
  =IFERROR(XMATCH("Mum", Raw_Responses!$B:$B, 0, -1), "")
  
  ```

* **Dad's latest row index (`D12`):**

  ```
  =IFERROR(XMATCH("Dad", Raw_Responses!$B:$B, 0, -1), "")
  
  ```

* **Me latest row index (`E12`):**

  ```
  =IFERROR(XMATCH("Me", Raw_Responses!$B:$B, 0, -1), "")
  
  ```

**2. Extracting and converting `A/B/C/D/E` answers to clean letter codes (`Rows 15–39`):** List all 25 questions (`Q1` to `Q15.10`) in rows `15` to `39`, with column `B` storing the column number in `Raw_Responses` where that question lives:

* **Letter code for Mum (`Col C`, e.g., row 15):**

  ```
  =IF($C$12="", "", LEFT(INDEX(Raw_Responses!$A:$ZZ, $C$12, $B15), 1))
  
  ```

  *(Because every form option starts with `A — `, `B — `, `C — `, `D — `, or `E — `, `LEFT(..., 1)` cleanly extracts `"A"`, `"B"`, `"C"`, `"D"`, or `"E"`!)*

* Copy across to `Col D` (referencing `$D$12` for Dad) and `Col E` (referencing `$E$12` for Me).

* **Combined Notes (`Col F`):** For questions Q1–Q14 that have a paired Notes column at `$B15 + 1` in `Raw_Responses`:

  ```
  =TEXTJOIN(" | ", TRUE,
    IF($C$12="","", IF(INDEX(Raw_Responses!$A:$ZZ,$C$12,$B15+1)="","","Mum: "&INDEX(Raw_Responses!$A:$ZZ,$C$12,$B15+1))),
    IF($D$12="","", IF(INDEX(Raw_Responses!$A:$ZZ,$D$12,$B15+1)="","","Dad: "&INDEX(Raw_Responses!$A:$ZZ,$D$12,$B15+1))),
    IF($E$12="","", IF(INDEX(Raw_Responses!$A:$ZZ,$E$12,$B15+1)="","","Me: "&INDEX(Raw_Responses!$A:$ZZ,$E$12,$B15+1)))
  )
  
  ```

**3. Converting `A/B/C/D` answers to numeric scores & levels (`Cols G:L`):**

* **Numeric Level (`1, 2, 3, 4` for `A, B, C, D` — used for spread/conflict checks and ordered filters):**

  ```
  =IF(C15="", "", IFERROR(MATCH(C15, {"A","B","C","D"}, 0), ""))
  
  ```

* **Q15 Priority Score (`0, 1, 2, 4` for `A, B, C, D` in rows `30–39`):**

  ```
  =IF(C30="", "", IFERROR(VLOOKUP(C30, $E$2:$F$5, 2, FALSE), ""))
  
  ```

* **Essential Cap Check (`Row 41`):**

  * **Count of D's (`C41`):** `=COUNTIF(C30:C39, "D")`

  * **Status (`C42`):**

    ```
    =IF(COUNTA(C30:C39)=0, "Not started", IF(C41>$B$5, "Too many D's ("&C41&")", IF(COUNTA(C30:C39)<10, "Incomplete", "OK")))
    
    ```

##### Tab 3: `Filters` (Hard Filters — Strictest Answer Wins)

Maps each person's letter (`A/B/C/D`) for `Q3, Q4, Q5, Q6, Q7, Q7b` to its real-world value and selects the strictest constraint:

| **Row** | **Filter** | **Lookup Mapping (A, B, C, D)** | **Formula for Each Person (Cols B:D)** | **Strictest Winner Formula (Col E)** | 
| **Row 2** | **Total budget incl. costs (Q3)** | `A=1000000`, `B=1250000`, `C=1500000`, `D="No cap"` | `=SWITCH(Cleaned_Answers!C17, "A",1000000, "B",1250000, "C",1500000, "D","No cap", "")` | `=IF(COUNT(B2:D2)>0, MIN(B2:D2), IF(COUNTIF(B2:D2,"No cap")>0, "No cap", "Not answered"))` | 
| **Row 3** | **Max drive to Glen Waverley (Q4)** | `A=15`, `B=25`, `C=35`, `D=45` | `=SWITCH(Cleaned_Answers!C18, "A",15, "B",25, "C",35, "D",45, "")` | `=IF(COUNT(B3:D3)>0, MIN(B3:D3), "Not answered")` | 
| **Row 4** | **Max drive to ED (Q5)** | `A=10`, `B=20`, `C=30`, `D="No limit"` | `=SWITCH(Cleaned_Answers!C19, "A",10, "B",20, "C",30, "D","No limit", "")` | `=IF(COUNT(B4:D4)>0, MIN(B4:D4), IF(COUNTIF(B4:D4,"No limit")>0, "No limit", "Not answered"))` | 
| **Row 5** | **Stairs level (Q6)** *(1 = strictest)* | `A=1` (None), `B=2` (Downstairs bed/bath), `C=3` (Anywhere) | `=SWITCH(Cleaned_Answers!C20, "A",1, "B",2, "C",3, "")` | `=IF(COUNT(B5:D5)>0, CHOOSE(MIN(B5:D5), "None at all", "Fine if bedroom & bathroom downstairs", "Fine anywhere"), "Not answered")` | 
| **Row 6** | **Home size (Q7b)** *(4 = most space)* | `A=1` (3 bed), `B=2` (3 bed + 2nd living), `C=3` (4 bed), `D=4` (Self-contained space) | `=SWITCH(Cleaned_Answers!C22, "A",1, "B",2, "C",3, "D",4, "")` | `=IF(COUNT(B6:D6)>0, CHOOSE(MAX(B6:D6), "3 bedrooms", "3 bedrooms + 2nd living area", "4 bedrooms", "Self-contained space (granny flat/unit)"), "Not answered")` | 
| **Row 7** | **Garden (Q7)** *(Unordered—flag if different)* | Direct letter `A/B/C/D` | `=Cleaned_Answers!C21` | `=IF(COUNTA(B7:D7)=0, "Not answered", IF(COUNTUNIQUE(B7:D7)>1, "Answers differ — discuss", SWITCH(INDEX(B7:D7,1,MATCH("*",B7:D7,0)), "A","Small, low upkeep", "B","Medium, room to grow things", "C","Large, lots of trees", "D","No garden is fine", "See notes")))` | 

* **Estimated Max House Price (excluding 6% stamp duty/costs, `Cell F2`):**

  ```
  =IF(ISNUMBER(E2), E2 / (1 + Cleaned_Answers!$B$6), "—")
  
  ```

##### Tab 4: `Priority_Weights` (Individual Shares & Influence-Weighted Average)

Lists the 10 priorities (`Q15.1` to `Q15.10`) in `Rows 2–11`, with `Row 12` as `Totals`.

1. **Raw Scores (`0, 1, 2, 4`) for Mum (`Col C`), Dad (`Col D`), Me (`Col E`):**

   * Pull directly from `Cleaned_Answers` numeric score columns (`J30:L39`), or calculate directly:

     ```
     =IF(Cleaned_Answers!C30="", "", SWITCH(Cleaned_Answers!C30, "A",0, "B",1, "C",2, "D",4, ""))
     
     ```

   * **Total Points per Person (`Row 12`):** `C12 = SUM(C2:C11)`, `D12 = SUM(D2:D11)`, `E12 = SUM(E2:E11)`.

2. **Each Person's Priority Weight as a Share of 100% (`Cols F, G, H`):**

   * **Mum's Weight (`F2`):**

     ```
     =IF(OR(C2="", C$12=0), "", C2 / C$12)
     
     ```

   * **Dad's Weight (`G2`):**

     ```
     =IF(OR(D2="", D$12=0), "", D2 / D$12)
     
     ```

   * **Me Weight (`H2`):**

     ```
     =IF(OR(E2="", E$12=0), "", E2 / E$12)
     
     ```

3. **Active Decision Influence Total (`Cell I12`):**

   * Only counts the influence weight (`Say in the decision`) of respondents who have actually completed Q15, so partial submissions still calculate cleanly:

     ```
     =(C12>0)*Cleaned_Answers!$B$2 + (D12>0)*Cleaned_Answers!$B$3 + (E12>0)*Cleaned_Answers!$B$4
     
     ```

4. **Combined Weight Across Mum, Dad, and Me (`Col I`, rows `2–11`):**

   ```
   =IF($I$12=0, "",
     (IF(ISNUMBER(F2), Cleaned_Answers!$B$2 * F2, 0) +
      IF(ISNUMBER(G2), Cleaned_Answers!$B$3 * G2, 0) +
      IF(ISNUMBER(H2), Cleaned_Answers!$B$4 * H2, 0)) / $I$12
   )
   
   ```

##### Tab 5: `Forced_Choice_Corrections` (Q10–Q13 Overrides & Final Normalized Weights)

Replicates your exact pairwise trade-off logic from `Calc!A10:L14` and `Calc!N20:O29`.

**Part A: Pairwise Trade-Off Table (`Rows 2–5`)**

| **Row** | **Question** | **Trade-Off Description** | **A-Side Priority # (Col F)** | **B-Side Priority # (Col G)** | 
| **Row 2** | **Q10** | Forest street (35m to GW) vs. Leafy suburban (15m to GW) | `1` *(Nature)* | `2` *(Near family in GW)* | 
| **Row 3** | **Q11** | Flat & beach 10m away vs. Hills & bush (beach 1hr) | `4` *(Beach)* | `1` *(Nature)* | 
| **Row 4** | **Q12** | Quiet street (drive 15m) vs. Busier street (walk to shops/station) | `8` *(Village character)* | `7` *(Shops & doctor nearby)* | 
| **Row 5** | **Q13** | Indian shops in suburb vs. Very green (community 30m drive) | `3` *(Indian community)* | `1` *(Nature)* | 

* **Influence-Weighted `A` Votes (`Col C`, e.g., `C2` for Q10 at `Cleaned_Answers` row 25):**

  ```
  =(Cleaned_Answers!C25="A")*Cleaned_Answers!$B$2 + (Cleaned_Answers!D25="A")*Cleaned_Answers!$B$3 + (Cleaned_Answers!E25="A")*Cleaned_Answers!$B$4
  
  ```

* **Influence-Weighted `B` Votes (`Col D`, e.g., `D2`):**

  ```
  =(Cleaned_Answers!C25="B")*Cleaned_Answers!$B$2 + (Cleaned_Answers!D25="B")*Cleaned_Answers!$B$3 + (Cleaned_Answers!E25="B")*Cleaned_Answers!$B$4
  
  ```

* **Winning Pick (`Col E`):**

  ```
  =IF(C2+D2=0, "", IF(C2>D2, "A", IF(D2>C2, "B", "Split")))
  
  ```

* **Winner Priority ID (`Col H`):** `=IF(E2="A", F2, IF(E2="B", G2, ""))`

* **Loser Priority ID (`Col I`):** `=IF(E2="A", G2, IF(E2="B", F2, ""))`

* **Winner Initial Combined Weight (`Col J`):**

  ```
  =IF(H2="", "", INDEX(Priority_Weights!$I$2:$I$11, H2))
  
  ```

* **Loser Initial Combined Weight (`Col K`):**

  ```
  =IF(I2="", "", INDEX(Priority_Weights!$I$2:$I$11, I2))
  
  ```

* **Weight Transfer (`Col L` — moves winner ahead of loser by `Forced-choice margin` `0.02`):**

  ```
  =IF(OR(H2="", NOT(ISNUMBER(J2)), NOT(ISNUMBER(K2))), 0,
    IF(J2 < K2 + Cleaned_Answers!$B$7,
      MIN(K2, (K2 - J2 + Cleaned_Answers!$B$7) / 2),
      0
    )
  )
  
  ```

**Part B: Final Corrected & Normalized Priority Table (`Rows 9–18` for Priorities `1–10`)**

* `Col A`: Priority ID (`1` to `10`)

* `Col B`: Priority Name

* `Col C`: Combined Weight from Q15 (`=Priority_Weights!I2`)

* `Col D`: **Net Forced-Choice Correction:**

  ```
  =IF(C9="", "", SUMIF($H$2:$H$5, A9, $L$2:$L$5) - SUMIF($I$2:$I$5, A9, $L$2:$L$5))
  
  ```

* `Col E`: **Your Manual Tweak (± percentage points, e.g., `3` for +3% — Manual Input):** Leave blank or `0` by default.

* `Col F`: **Raw Final Weight (floored at 0):**

  ```
  =IF(C9="", "", MAX(0, C9 + D9 + N(E9)/100))
  
  ```

* `Col G`: **Final Normalized Weight (Always sums to 100%):**

  ```
  =IF(OR(F9="", SUM($F$9:$F$18)=0), "", F9 / SUM($F$9:$F$18))
  
  ```

* `Col H`: **Final Priority Rank (`1` to `10`):**

  ```
  =IF(G9="", "", RANK(G9, $G$9:$G$18))
  
  ```

##### Tab 6: `Suburb_Scorecard`

Pulls active filters into `Row 4` (`B4 = Filters!E2` Budget, `D4 = Filters!E3` Max GW drive, `F4 = Filters!E4` Max ED drive, `H4 = Cleaned_Answers!$B$6` Est. costs `0.06`) and pulls the 10 Final Normalized Weights (`Forced_Choice_Corrections!G9:G18`) into `H6:Q6`.

For each suburb in `Rows 8–21` (pre-loaded with Blackburn, Ringwood, Heidelberg, Eltham, Upper Ferntree Gully, Glen Waverley, Mentone, Frankston, Altona, Williamstown, plus blank reserve rows):

* `Col A`: Suburb Name *(Manual)*

* `Col B`: House Price (`Price (house)`) *(Manual)*

* `Col C`: Price Basis *(Manual)*

* `Col D`: **Price + Est. Costs (Auto):**

  ```
  =IF(B8="", "", B8 * (1 + $H$4))
  
  ```

* `Col E`: Drive to Glen Waverley (min) *(Manual)*

* `Col F`: Drive to nearest 24-hr public ED (min) *(Manual)*

* `Col G`: **Hard Filter Pass/Fail Status (Auto):**

  ```
  =IF(A8="", "",
    IF(OR(
      AND(ISNUMBER($B$4), ISNUMBER(D8), D8>$B$4),
      AND(ISNUMBER($D$4), ISNUMBER(E8), E8>$D$4),
      AND(ISNUMBER($F$4), ISNUMBER(F8), F8>$F$4)
    ),
    "Fails: " & TEXTJOIN(", ", TRUE,
      IF(AND(ISNUMBER($B$4), ISNUMBER(D8), D8>$B$4), "budget", ""),
      IF(AND(ISNUMBER($D$4), ISNUMBER(E8), E8>$D$4), "Glen Waverley drive", ""),
      IF(AND(ISNUMBER($F$4), ISNUMBER(F8), F8>$F$4), "hospital drive", "")
    ),
    IF(OR(B8="", E8="", F8=""), "Need data", "Pass"))
  )
  
  ```

* `Cols H:Q`: **0–10 Suburb Scores for each of the 10 Priorities** *(Manual input)*

* `Col R`: **Scores Entered Check (Auto):**

  ```
  =IF(A8="", "", COUNT(H8:Q8) & "/10")
  
  ```

* `Col S`: **Weighted Suburb Score 0–10 (Auto):**

  ```
  =IF(OR(A8="", COUNT(H8:Q8)<10, COUNT($H$6:$Q$6)<10), "", SUMPRODUCT(H8:Q8, $H$6:$Q$6))
  
  ```

* `Col T`: **Rank Among Passing Suburbs Only (Auto):**

  ```
  =IF(AND(G8="Pass", ISNUMBER(S8)),
    SUMPRODUCT(($G$8:$G$21="Pass") * ISNUMBER($S$8:$S$21) * ($S$8:$S$21 > S8)) + 1,
    ""
  )
  
  ```

#### Manual Inputs vs. Automatic Calculations Summary

| **Entered Manually by You** | **Calculated Automatically by Google Sheets** | 
| **1. Three Google Form Submissions:** Completed once for `Me`, once for `Mum`, and once for `Dad`. | **1. Latest Response Extraction:** Pulls the newest submission for each person and strips option text down to `A/B/C/D/E` and numeric values. | 
| **2. Model Settings (`Cleaned_Answers`):** Decision influence weights (`1, 1, 1`), Max `D` answers (`2`), Purchase cost % (`6%`), Forced-choice margin (`2%`). | **2. Validation & Status Checks:** Counts answered questions (`of 25`) and flags if anyone picked more than two `D — Essential` items. | 
| **3. Optional Weight Tweaks (`Forced_Choice_Corrections` Col E):** Any `±` percentage-point adjustments after family discussion. | **3. Hard Filters (`Filters`):** Evaluates strictest budget, drive times, stairs, and space rules, plus maximum pre-cost purchase price. | 
| **4. Suburb Raw Data (`Suburb_Scorecard`):** Candidate suburb names, house prices, routine drive times to Glen Waverley and nearest 24-hr ED, and `0–10` ratings across the 10 factors. | **4. Weights, Overrides & Suburb Rankings:** Computes individual and combined shares, applies Q10–Q13 weight transfers, re-normalizes to 100%, flags `Pass`/`Fails` per suburb, and ranks passing suburbs. | 

### Part 3: Results Presentation & `Discussion_Summary` Dashboard

#### Recommended Visual Format: Dedicated `Discussion_Summary` Tab with Conditional Formatting + 1 Bar Chart

Avoid building an external Looker Studio dashboard (which adds sync lag and maintenance overhead). Instead, build your `Discussion_Summary` tab directly in Google Sheets using clean tables, **conditional formatting**, and **in-cell `SPARKLINE` bars**. That keeps everything in one place when you sit down with Mum and Dad.

#### Layout of the `Discussion_Summary` Tab

1. **Top Status Bar (Submission & Q15 Validation Banner):**

   * Shows a 3-card status strip for **Mum**, **Dad**, and **Me**:

     * **Submitted?** `=IF(Cleaned_Answers!C12="", "⏳ Pending", "✅ Submitted (" & COUNTA(Cleaned_Answers!C15:C39) & "/25)")`

     * **Q15 Essential Check:** Pulls `OK` (Green fill) or `Too many D's` / `Incomplete` (Red/Amber fill).

2. **Block 1: Active Hard Filters & Inspection Checklist:**

   * Displays the 6 filters (`Budget ceiling`, `Max drive to Glen Waverley`, `Max drive to ED`, `Stairs`, `Home size`, `Garden`), the winning constraint, who set the strictest limit (`Mum A · Dad B · Me C`), and the implied **Max Purchase Price before 6% costs**.

3. **Block 2: Final Priority Ranking (with In-Cell Bar Charts):**

   * Sorted automatically from Rank 1 to Rank 10 using:

     ```
     =SORT(Forced_Choice_Corrections!B9:H18, 7, TRUE)
     
     ```

   * Add an in-cell visual bar column next to Final Weight (`Col G`):

     ```
     =SPARKLINE(G9, {"charttype","bar"; "max",MAX($G$9:$G$18); "color1","#2E6B4E"})
     
     ```

4. **Block 3: Agreed vs. Conflicting Answers (Discussion Generator):**

   * Automatically flags items where a mathematical average isn't enough and the family needs a 5-minute conversation:

     * **Ordered Dealbreakers (`Q3, Q4, Q5, Q6, Q7b`):** Flagged if `MAX(levels) - MIN(levels) >= 2` (a 2+ step gap between family members):

       ```
       =IF(MAX(Cleaned_Answers!G17:I17)-MIN(Cleaned_Answers!G17:I17)>=2, "⚠️ Big gap (2+ steps apart) — discuss together", "✅ Aligned")
       
       ```

     * **Pairwise Trade-Offs & Garden (`Q7, Q10–Q13`):** Flagged whenever **Mum and Dad pick different options** (`Cleaned_Answers!C21 <> Cleaned_Answers!D21`), or when the weighted trade-off ends in a `"Split"`.

     * **Q15 Priorities (`Q15.1–Q15.10`):** Flagged whenever `MAX(levels) - MIN(levels) >= 2` (e.g., one person says `D — Essential` and another says `A — Not needed` or `B — Nice to have`), plus a prompt to ask anyone who rated an item `D — Essential` why it is non-negotiable for them.

5. **Block 4: Top-Ranked Passing Suburbs & "Why They Rank Highly":**

   * Automatically lists all passing suburbs in rank order using `FILTER` and `SORT`:

     ```
     =IFERROR(SORT(FILTER({Suburb_Scorecard!T8:T21, Suburb_Scorecard!A8:A21, Suburb_Scorecard!D8:F21, Suburb_Scorecard!S8:S21}, Suburb_Scorecard!G8:G21="Pass", ISNUMBER(Suburb_Scorecard!S8:S21)), 1, TRUE), "Complete suburb drive times and 0–10 scores to see passing ranks.")
     
     ```

   * **"Why It Ranks Highly" Formula (Top 2 Contributing Factors per Suburb):** For each suburb row on `Suburb_Scorecard`, calculate each factor's weighted contribution (`Score * Final_Weight`), and use this formula to automatically name the suburb's top two strengths:

     ```
     =INDEX($H$7:$Q$7, 1, MATCH(LARGE(INDEX(H8:Q8 * $H$6:$Q$6, 0), 1), INDEX(H8:Q8 * $H$6:$Q$6, 0), 0))
      & " (" & INDEX(H8:Q8, 1, MATCH(LARGE(INDEX(H8:Q8 * $H$6:$Q$6, 0), 1), INDEX(H8:Q8 * $H$6:$Q$6, 0), 0)) & "/10) & " &
      INDEX($H$7:$Q$7, 1, MATCH(LARGE(INDEX(H8:Q8 * $H$6:$Q$6, 0), 2), INDEX(H8:Q8 * $H$6:$Q$6, 0), 0))
      & " (" & INDEX(H8:Q8, 1, MATCH(LARGE(INDEX(H8:Q8 * $H$6:$Q$6, 0), 2), INDEX(H8:Q8 * $H$6:$Q$6, 0), 0)) & "/10)"
     
     ```

6. **Recommended Conditional Formatting Rules:**

   * **Hard Filter Status (`Suburb_Scorecard!G8:G21`):**

     * Text is exactly `"Pass"` -> Soft green fill (`#D9EAD3`), dark green text.

     * Text starts with `"Fails:"` -> Soft red fill (`#F4CCCC`), dark red text.

     * Text is `"Need data"` -> Soft yellow fill (`#FFF2CC`), dark amber text.

   * **Discussion Flags (`Discussion_Summary`):**

     * Text contains `"Discuss"` or `"Big gap"` or `"differ"` -> Soft amber fill (`#FCE5CD`).

### Part 4: Step-by-Step Build Order & Test Plan

#### Step-by-Step Build Order

1. **Step 1 — Import or Create the Google Sheet (5 mins):**

   * *Fastest route:* Upload `Parents_move_priorities_survey.xlsx` to Google Drive and open it as a Google Sheet. Its existing `Start here`, `Survey`, `Results`, `Suburb scorecard`, and `Calc` tabs will convert with `INDEX/MATCH`, `SUMPRODUCT`, and `TEXTJOIN` intact.

   * *Clean-slate route:* Create a new Google Sheet with the 7 tabs (`Raw_Responses`, `Cleaned_Answers`, `Filters`, `Priority_Weights`, `Forced_Choice_Corrections`, `Suburb_Scorecard`, `Discussion_Summary`).

2. **Step 2 — Build the Google Form (15 mins):**

   * In your Google Sheet, click **Tools -> Create a new form**.

   * Add `Whose answers are these?` (`Mum`, `Dad`, `Me`) as Question 1, then create Sections 1–6 using the exact `A — ...`, `B — ...`, `C — ...`, `D — ...`, `E — ...` option text from Part 1 above.

   * In Form **Settings -> Presentation**, turn ON **Show link to submit another response** and turn OFF *Collect email addresses* and *Limit to 1 response*.

3. **Step 3 — Wire `Cleaned_Answers` to `Raw_Responses` (10 mins):**

   * Add the `XMATCH(..., -1)` lookup formulas for `Mum`, `Dad`, and `Me` so `Cleaned_Answers` pulls the most recent row for each person and extracts `LEFT(answer, 1)`.

   * *(If using your imported Excel workbook, simply put the `LEFT(INDEX(Raw_Responses!..., XMATCH("Mum", ...)), 1)` formulas directly into `Survey!H5:J30`—then your existing `Calc`, `Results`, and `Suburb scorecard` tabs will work automatically!)*

4. **Step 4 — Verify Downstream Tabs & Conditional Formatting (5 mins):**

   * Check that `Filters`, `Priority_Weights`, `Forced_Choice_Corrections`, `Suburb_Scorecard`, and `Discussion_Summary` link cleanly to `Cleaned_Answers`.

#### End-to-End Test Plan (3 Fake Submissions)

Before interviewing Mum and Dad, submit these three test responses through your live Google Form link to verify every edge case in your model:

| **Test Input / Check** | **Fake Response 1: Me** | **Fake Response 2: Mum** | **Fake Response 3: Dad** | **Expected Model Output to Verify** | 
| **Q3 Budget** | *(Blank — testing optional non-contributor)* | `B — $1.25m` | `C — $1.5m` | **Strictest Budget = `$1,250,000`** (`Max purchase price ≈ $1,179,245` after 6% costs). Confirms blank `Me` doesn't zero out `MIN()`. | 
| **Q4 Glen Waverley Drive** | `C — 35 min` | `B — 25 min` | `C — 35 min` | **Strictest GW Drive = `25 min`** (matches your workbook example on `Start here!A28`). | 
| **Q5 Hospital ED Drive** | `C — 30 min` | `B — 20 min` | `D — It doesn't matter much` | **Strictest ED Drive = `20 min`** (and flags `Q5 Hospital drive — big gap (Mum B, Dad D, Me C)` because `D(4) - B(2) = 2`). | 
| **Q6 Stairs & Q7b Space** | `B` (Stairs), `B` (Space) | `A — None at all` (Stairs), `C — 4 bedrooms` (Space) | `C` (Stairs), `D — Self-contained space` (Space) | **Stairs = `None at all`** (`MIN=1`); **Home Size = `Self-contained space`** (`MAX=4`). | 
| **Q10 Trade-Off Override** | `B — Leafy suburban, 15m from GW` | `B — Leafy suburban, 15m from GW` | `A — Forest street, 35m from GW` | **B wins (`2` vs `1`).** If `Nature (Q15.1)` has a higher combined weight than `Near family in GW (Q15.2)`, verify `Forced_Choice_Corrections` transfers `(Nature_wt - GW_wt + 0.02)/2` from Nature to GW! | 
| **Q15 Essential Cap Check** | Pick **2** `D — Essential` (`Q15.1 Nature`, `Q15.9 Price`) | Pick **3** `D — Essential` *(deliberate violation test)* | Pick **1** `D — Essential` (`Q15.1 Nature`) | `Me` = `OK`; `Dad` = `OK`; **`Mum` = `Too many D's (3)`** flagged in red on the dashboard. | 
| **Suburb Scorecard Filter & Rank** | Enter test drive times (`GW=20, ED=15`) & 0–10 scores for **Ringwood** (`$1.045m`) and **Blackburn** (`$1.60m`) | — | — | **Blackburn** shows `Fails: budget` (`$1.696m > $1.25m`) and has **blank Rank**. **Ringwood** (`$1.108m <= $1.25m`) shows `Pass` and **Rank = `1`**. | 

Once all checks pass, delete the 3 test rows from `Raw_Responses` (select rows `2:4` -> right-click -> **Delete rows 2–4**, not just Clear, so Google Forms resets cleanly) and submit your own real response (`Me`) first.

## 4. Risks, Limitations & Questions to Resolve Before Building

### Key Risks & Technical Gotchas to Watch For

1. **Never edit `Raw_Responses` in place or reference fixed rows like `Raw_Responses!C2`:** When Google Forms receives a new submission, it **inserts a brand-new row** at the bottom of `Raw_Responses`, which shifts direct cell references (`C2`, `C3`) or leaves them pointing at old test rows. Using `XMATCH("Mum", Raw_Responses!$B:$B, 0, -1)` in `Cleaned_Answers` completely eliminates this bug and automatically grabs the latest submission if you re-interview someone.

2. **Simultaneous Forced-Choice Adjustments Involving `Nature and scenery` (`Priority #1`):**

   * Look closely at `Calc!F11:G14` in your workbook: **three** of your four trade-off questions (`Q10`, `Q11`, and `Q13`) pit another factor against **`Priority #1 (Nature and scenery)`**:

     * `Q10`: Nature (`#1`) vs. Near family in Glen Waverley (`#2`)

     * `Q11`: Beach (`#4`) vs. Nature (`#1`)

     * `Q13`: Indian community (`#3`) vs. Nature (`#1`)

   * Each row (`Q10, Q11, Q13`) calculates its transfer against the *initial* combined weight (`L20:L29`), and then `N20` sums all transfers together (`SUMIF(Winners) - SUMIF(Losers)`). If Nature loses two or three trade-offs at once, its weight is reduced by the sum of all those transfers (floored at `0%` by `MAX(0, ...)`). That is already handled cleanly by your formula (`MAX(0, L20+N20+...)` followed by re-normalization to 100%), so keep that exact two-step normalization in Google Sheets.

3. **Price Filter vs. Q15.9 Price Weight Double-Counting:**

   * Both `Price` (`Q3` & `Q15.9`) and `Glen Waverley drive` (`Q4` & `Q15.2`) act as **hard filters** *and* **scored priorities**. Make sure that when you score passing suburbs `0–10` on `Price` (`Suburb_Scorecard!P8:P21`), you score them on a clear relative scale (e.g., `10 = well under budget / great value for a 4-bed home`, `5 = right at the budget ceiling`) so a cheaper suburb like Upper Ferntree Gully or Ringwood gets credit for saving money below the hard cap.

### Questions to Resolve Before We Build It

1. **Keep the imported Excel tabs vs. build a clean 7-tab Google Sheet?** Would you rather upload your existing `.xlsx` into Google Sheets and simply add the `Raw_Responses` + `XLOOKUP` bridge into `Survey!H5:J30` (preserving your exact layout), or do you prefer the separated 7-tab architecture (`Raw_Responses`, `Cleaned_Answers`, `Filters`, `Priority_Weights`, `Forced_Choice_Corrections`, `Suburb_Scorecard`, `Discussion_Summary`)?

2. **Q15 Question Format in Google Forms:** Do you prefer **10 separate multiple-choice questions** (one after another, with the confirmation checkbox at the bottom), or a **single 10-row Multiple-Choice Grid** so you can visually see the `D — Essential` column all at once while interviewing?

3. **Notes Field Placement:** In the workbook, `E = none of these / depends` applies to `Q1–Q14`. Do you want an optional `Notes / depends` short-answer box after **every single question (`Q1–Q14`)**, or **one `Section Notes` box at the bottom of each section** to keep the Form shorter on screen?