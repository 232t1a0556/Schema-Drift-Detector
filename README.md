### TEAM NAME : Team 9 (DE-04)

### TEAM MEMBERS:
1.G.Bhanu Sudeepthi
2.B.Lahari
3.M.Venkata Rama Chandana
4.G.Gowthami

# Schema Drift Detector

## Overview

Schema Drift Detector is a Python-based Data Engineering project that identifies changes between database schema versions and analyzes their impact on downstream systems.

The project captures schema snapshots, compares versions, detects drift, and generates impact analysis reports through a Streamlit dashboard.

---

## Features

- Schema Snapshot Generation
- Schema Drift Detection
- Added Column Detection
- Removed Column Detection
- Breaking Change Identification
- Impact Analysis
- Report Generation
- Streamlit Dashboard

---

## Technologies Used

- Python
- SQLite
- Streamlit
- JSON
- Pytest

---

## Project Structure

schema-drift-detector/

├── app.py

├── data/

│ ├── test.db

│ ├── schema_v1.json

│ └── schema_v2.json

├── outputs/

│ └── drift_report.md

├── src/

│ ├── db_setup.py

│ ├── schema_capture.py

│ ├── schema_capture_v2.py

│ ├── alter_db.py

│ ├── drift_detector.py

│ └── llm_helper.py

├── tests/

│ └── test_basic.py

└── README.md

---

## Workflow

### Step 1: Create Database

```bash
python src/db_setup.py

### Demo Video
Google drive link:
https://drive.google.com/file/d/1cITyss0YM53iMhGOMio4xZBzERAuhxo4/view?usp=drivesdk
