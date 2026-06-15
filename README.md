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

1. **Database Setup**
   - Create a sample SQLite database.
   - Create initial tables (`users`, `orders`).

2. **Schema Snapshot Capture**
   - Extract the database schema using SQLAlchemy.
   - Store the schema as `schema_v1.json`.

3. **Schema Drift Simulation**
   - Modify the database schema.
   - Example: Add a new column (`phone`) to the `users` table.

4. **Capture Updated Schema**
   - Extract the modified schema.
   - Store it as `schema_v2.json`.

5. **Drift Detection**
   - Compare `schema_v1.json` and `schema_v2.json`.
   - Identify:
     - Added columns
     - Removed columns
     - Data type changes

6. **Impact Analysis**
   - Analyze detected schema changes.
   - Classify the risk level (Low, Medium, High).
   - Determine whether changes are breaking or non-breaking.

7. **Report Generation**
   - Generate a detailed drift report.
   - Save the report in `outputs/drift_report.md`.

8. **Visualization Dashboard**
   - Display detected schema drift through a Streamlit web interface.
   - Show impact analysis and recommendations.

9. **Version Tracking**
   - Store schema snapshots in GitHub.
   - Maintain change history for future comparisons.

10. **Future Enhancement**
    - Integrate LLM APIs (Gemini/Groq/OpenAI) for intelligent impact analysis.
    - Add email/Slack alerts for detected schema drift.
    - Schedule automated schema monitoring jobs.

#### Demo Link
https://www.loom.com/share/e991cec774224f05b48c1885119f6999

Sample Data :- https://github.com/232t1a0556/Schema-Drift-Detector/tree/main/sample%20data

Test Cases :- https://github.com/232t1a0556/Schema-Drift-Detector/blob/main/Testcases.md
