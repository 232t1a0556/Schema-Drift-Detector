import os

def save_report(drift, analysis):
    os.makedirs("outputs", exist_ok=True)

    with open("outputs/drift_report.md", "w", encoding="utf-8") as f:
        f.write("# Schema Drift Report\n\n")
        f.write("## Detected Drift\n")

        for item in drift:
            f.write(f"- {item}\n")

        f.write("\n## Analysis\n")
        f.write(analysis)

    print("Report Generated")