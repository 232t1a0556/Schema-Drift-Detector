from sqlalchemy import create_engine, inspect
import json

# Connect to SQLite database
engine = create_engine("sqlite:///data/test.db")

inspector = inspect(engine)

schema = {}

# Read all tables and columns
for table in inspector.get_table_names():

    schema[table] = []

    for col in inspector.get_columns(table):

        schema[table].append({
            "name": col["name"],
            "type": str(col["type"])
        })

# Save first snapshot
with open("data/schema_v1.json", "w") as f:
    json.dump(schema, f, indent=4)

print("schema_v1.json created successfully")