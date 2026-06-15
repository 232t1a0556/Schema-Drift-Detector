import json

with open("data/schema_v1.json") as f:
    old = json.load(f)

with open("data/schema_v2.json") as f:
    new = json.load(f)

added = []
removed = []

for table in old:

    old_cols = [c["name"] for c in old[table]]
    new_cols = [c["name"] for c in new[table]]

    for col in new_cols:
        if col not in old_cols:
            added.append(f"{table}.{col}")

    for col in old_cols:
        if col not in new_cols:
            removed.append(f"{table}.{col}")

print("Added:", added)
print("Removed:", removed)