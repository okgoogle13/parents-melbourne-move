# Questionnaire page tests (Playwright, Chromium)

Copied 31 Oct 2026 from the claude.ai session that built page code version 14. Each script loads `page.html` from the current directory.

Run from a temp directory (not the repo root):

    cp "<repo>/Our Next Home — questionnaire page v15 (Claude artifact source).html" page.html
    node "<repo>/tools/questionnaire_tests/regression.test.js"   # ladder paths, branching, steps, export→import round trip, v13 rejected; expect "FAILS: 0"
    node "<repo>/tools/questionnaire_tests/import.test.js"       # WhatsApp prefixes, invisible characters, backticks, old versions rejected
    node "<repo>/tools/questionnaire_tests/r86.test.js"          # R8.6 bushfire question: shown only for R8.4 = B/C, X otherwise; expect "FAILS: 0"

Needs Node and `playwright` with Chromium (`npm i playwright && npx playwright install chromium` in the temp directory if not already available). Tests write screenshots (p4.png, p5.png, p6.png, p5b.png) to the current directory.
Update the expectations when questions, options or PAGE_VERSION change (e.g. "v13 rejected" assumes PAGE_VERSION 14).
