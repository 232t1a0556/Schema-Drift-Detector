import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE users_new (
    id INTEGER PRIMARY KEY,
    name TEXT,
    created_at TEXT,
    phone TEXT
)
""")

cur.execute("""
INSERT INTO users_new(id,name,created_at)
SELECT id,name,created_at
FROM users
""")

cur.execute("DROP TABLE users")
cur.execute("ALTER TABLE users_new RENAME TO users")

conn.commit()
conn.close()