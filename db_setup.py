# db_setup.py

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, DateTime, inspect
import json
import os
from datetime import datetime

# -----------------------------
# 1. Create SQLite Database
# -----------------------------
DB_NAME = "test.db"
engine = create_engine(f"sqlite:///{DB_NAME}")

metadata = MetaData()

# -----------------------------
# 2. Define Tables
# -----------------------------
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String),
    Column("created_at", DateTime, default=datetime.utcnow)
)

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer),
    Column("amount", Integer),
    Column("status", String)
)

# -----------------------------
# 3. Create Tables in DB
# -----------------------------
def setup_database():
    metadata.create_all(engine)
    print("Database and tables created successfully.")

# -----------------------------
# 4. Save Schema Snapshot (v1)
# -----------------------------
def save_schema_snapshot(filename="schema_v1.json"):
    inspector = inspect(engine)

    schema = {
        "tables": {}
    }

    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        schema["tables"][table_name] = [
            {
                "name": col["name"],
                "type": str(col["type"])
            }
            for col in columns
        ]

    with open(filename, "w") as f:
        json.dump(schema, f, indent=4)

    print(f"Schema snapshot saved to {filename}")

# -----------------------------
# 5. Run Setup
# -----------------------------
if __name__ == "__main__":
    setup_database()
    save_schema_snapshot()