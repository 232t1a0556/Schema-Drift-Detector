import streamlit as st
import json
import os

st.set_page_config(
    page_title="Schema Drift Detector",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Schema Drift Detector")

# Load schema files
try:
    with open("data/schema_v1.json", "r") as f:
        old_schema = json.load(f)

    with open("data/schema_v2.json", "r") as f:
        new_schema = json.load(f)

except FileNotFoundError:
    st.error(
        "schema_v1.json or schema_v2.json not found inside data folder."
    )
    st.stop()

added = []
removed = []

# Compare schemas
for table in old_schema:

    old_cols = [c["name"] for c in old_schema[table]]

    if table in new_schema:
        new_cols = [c["name"] for c in new_schema[table]]
    else:
        new_cols = []

    # Added columns
    for col in new_cols:
        if col not in old_cols:
            added.append((table, col))

    # Removed columns
    for col in old_cols:
        if col not in new_cols:
            removed.append((table, col))

st.header("Detected Drift")

if added or removed:

    st.success("Schema Drift Found")

    if added:
        st.subheader("✅ Added Columns")

        for table, col in added:
            st.success(f"{table}.{col}")

    if removed:
        st.subheader("❌ Removed Columns")

        for table, col in removed:
            st.error(f"{table}.{col}")

    if st.button("Analyze Drift"):

        report = []

        for table, col in removed:

            report.append(
                f"BREAKING: Column '{col}' removed from '{table}' table.\n"
                f"Impact: Downstream pipelines may fail.\n"
                f"Recommended: Add migration script and update ETL jobs.\n"
            )

        for table, col in added:

            report.append(
                f"ADDITIVE: Column '{col}' added to '{table}' table.\n"
                f"Impact: Existing pipelines remain unaffected.\n"
                f"Recommended: Update documentation and mappings.\n"
            )

        final_report = "\n".join(report)

        st.subheader("Impact Analysis")

        st.text(final_report)

        os.makedirs("outputs", exist_ok=True)

        with open(
            "outputs/drift_report.md",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(final_report)

        st.success(
            "Report saved to outputs/drift_report.md"
        )

else:

    st.info("No Schema Drift Detected")