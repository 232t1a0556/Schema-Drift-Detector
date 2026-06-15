import sqlite3

conn = sqlite3.connect("data/test.db")
cursor = conn.cursor()

# Create new table without email
cursor.execute("""
CREATE TABLE users_new(
    id INTEGER PRIMARY KEY,
    name TEXT,
    created_at TEXT,
    phone TEXT
)
""")

# Copy existing data
cursor.execute("""
INSERT INTO users_new(id,name,created_at)
SELECT id,name,created_at
FROM users
""")

# Remove old table
cursor.execute("DROP TABLE users")

# Rename new table
cursor.execute(
    "ALTER TABLE users_new RENAME TO users"
)

conn.commit()
conn.close()

print("Schema Drift Simulated")