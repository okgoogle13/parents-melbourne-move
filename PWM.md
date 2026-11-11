# Project PWM Workflows — Parents Melbourne MOVE

Active intelligence, research, and evaluation workflows tailored for `Parents Melbourne MOVE`.

> **Context:** Research record for choosing a suburb in or around Melbourne for the user's parents (the user lives separately now and will live with them after the move). Not software. `main` is the baseline; `PROJECT_STATE.md` records when it was last verified against the local Mac folder.

---

### 1. Fast Intel & Search
* **`quick "<query>"`**
  * **Goal**: Fast factual lookup (definitions, data points, council/local info).
  * **Model**: Sonar 2 (`-m sonar`)
  * **Cost**: 1 Pro search.
* **`ask-pwm "<query>"`**
  * **Goal**: Balanced multi-source search with synthesized web citations.
  * **Cost**: 1 Pro search.
* **`au-market "<item or service>"`**
  * **Goal**: Current Australian retail pricing, vendor terms, and availability.
  * **Cost**: 1 Pro search (`-s web`).

### 2. High-Stakes Councils & Reasoning
* **`jury "<dilemma or trade-offs>"`**
  * **Goal**: 3-provider executive jury (GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.1 Pro) evaluating options and trade-offs.
  * **Cost**: 4 Pro searches.
* **`council "<query>"`**
  * **Goal**: Parallel multi-model consensus audit.
  * **Cost**: 4 Pro searches.
* **`model-think "<prompt>"`**
  * **Goal**: Deep extended reasoning via Claude Sonnet 5 (model only, no search).
  * **Cost**: 1 Pro search (`-m claude_sonnet -t -s none`).

### 3. Deep Research Dossiers (Monthly Pool — High Impact)
*Consumes 1 Deep Research query from the scarce monthly pool (~5–10/month). Never use for simple factual lookups.*

* **`suburb-dossier "<suburb>"`**
  * **Goal**: 360° livability, aging-in-place walkability, topography, ED hospital access, and Glen Waverley transit dossier.
  * **Feeds**: SuburbScorecard columns M, N, P, Q, R, S, Z.
  * **Run**: `suburb-dossier "Ringwood"` (saves to `~/Documents/pwm-research/`)

* **`property-baseline "<suburb> [dwelling_type]"`**
  * **Goal**: Real estate settled sales baseline, p25/p50/p75 price bands, single-level downsizer stock, and local council rates.
  * **Feeds**: Budget feasibility, Price score (M), Victorian stamp duty estimates.
  * **Run**: `property-baseline "Ferntree Gully" "single-storey house"`

* **`diversity-recon "<suburb or LGA>"`** *(Tailored for `docs/diversitymeasurereviewgemini4argon.md`)*
  * **Goal**: Intercensal demographic audit (2022–2026), resolving post-lockdown Net Overseas Migration (NOM) surges, ACARA MySchool LBOTE % proxies, MESC vs Non-MESC separation, and Greater Melbourne (2GMEL) benchmark anchors.
  * **Feeds**: Diversity measure audit (M1–M8), Score P normalisation, and the 25-min grocery filter.
  * **Run**: `diversity-recon "Ferntree Gully"` or `diversity-recon "City of Knox"`

* **`community-audit "<suburb> [radius]"`**
  * **Goal**: Ground-level ethnic food infrastructure, dedicated Indian grocers within 25 min drive, places of worship, and senior community vibrancy.
  * **Feeds**: 25-min grocery hard filter (Y) and Indian community score (P).
  * **Run**: `community-audit "Berwick"`

* **`suburb-duel "<suburb_A> vs <suburb_B>"`**
  * **Goal**: Rigorous head-to-head decision matrix comparing two shortlist contenders across the 8 live S2 survey criteria to break family deadlocks.
  * **Feeds**: Family deliberation meetings and shortlist foundation reports.
  * **Run**: `suburb-duel "Frankston vs Berwick"`
