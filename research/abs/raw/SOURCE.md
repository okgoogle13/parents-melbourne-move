# ABS 2021 Census General Community Profile (GCP) Raw Data Provenance

## Source Archives

1. **`2021_GCP_SAL_for_VIC_short-header.zip`**
   - **Geography:** Victoria — Suburbs and Localities (SAL), ASGS Edition 3 (2021), Place of Usual Residence (`PUR`)
   - **Download URL:** `https://www.abs.gov.au/census/find-census-data/datapacks/download/2021_GCP_SAL_for_VIC_short-header.zip`
   - **Download Date:** 2026-11-11
   - **SHA-256:** `050855f7ab05f592b571e1a781bcb5a55d2c10c6d93a8a6b0ed63e65c6ab50cf`

2. **`2021_GCP_GCCSA_for_VIC_short-header.zip`**
   - **Geography:** Victoria — Greater Capital City Statistical Areas (GCCSA), ASGS Edition 3 (2021), Place of Usual Residence (`PUR`)
   - **Download URL:** `https://www.abs.gov.au/census/find-census-data/datapacks/download/2021_GCP_GCCSA_for_VIC_short-header.zip`
   - **Download Date:** 2026-11-11
   - **SHA-256:** `75bc220a6e47f8e5f6b32779e2d58b235a20a7055b9245acf51c425f19b3cbb9`

## Committed Raw CSV Files (`research/abs/raw/`)

Extracted unmodified from the two archives above for tables `G01` (Selected Person Characteristics), `G09A–G09H` (Country of Birth of Person by Age by Sex), and `G13A–G13E` (Language Used at Home by Proficiency in Spoken English by Sex):

- `2021Census_G01_VIC_SAL.csv`, `2021Census_G09A_VIC_SAL.csv` .. `2021Census_G09H_VIC_SAL.csv`, `2021Census_G13A_VIC_SAL.csv` .. `2021Census_G13E_VIC_SAL.csv`
- `2021Census_G01_VIC_GCCSA.csv`, `2021Census_G09A_VIC_GCCSA.csv` .. `2021Census_G09H_VIC_GCCSA.csv`, `2021Census_G13A_VIC_GCCSA.csv` .. `2021Census_G13E_VIC_GCCSA.csv`

## Note on Northern Ireland in ABS 2021 GCP Table `G09`

In the ABS 2021 Census GCP DataPack (`Metadata_2021_GCP_DataPack_R1_R2.xlsx` and `2021_GCP_Sequential_Template_R2.xlsx`), Table `G09` lists the top 50 Country of Birth responses from the 2016 Census. Among the United Kingdom constituent countries:
- `P_England_Tot` (`G09F`), `P_Scotland_Tot` (`G09H`), and `P_Wales_Tot` (`G09H`) have separate columns.
- **Northern Ireland has no separate column in `G09`** (unlike Place of Enumeration Profile Table `P09`, which includes `N_Ireland_P`).
- Per ABS footnote `(d)` on Table `G09` (*"Born elsewhere: Includes countries not identified individually, 'Inadequately described', and 'At sea'. Excludes not stated"*), persons born in **Northern Ireland** (along with Channel Islands, Isle of Man, and `United Kingdom, nfd`) are aggregated inside **`P_Elsewhere_Tot`** (`G09H`) and cannot be subtracted separately from `G09`.

