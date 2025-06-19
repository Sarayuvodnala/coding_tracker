import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect("coding_tracker.db")
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS coding_data (
    Date TEXT,
    Platform TEXT,
    Questions INTEGER,
    Time INTEGER
)
""")

# ✅ Optional: Insert sample data (you can remove this part if you want an empty database)
sample_data = [
    ("2025-06-17", "LeetCode", 3, 60),
    ("2025-06-18", "HackerRank", 2, 45),
    ("2025-06-19", "LeetCode", 4, 90)
]
cursor.executemany("INSERT INTO coding_data VALUES (?, ?, ?, ?)", sample_data)

# Commit and close
conn.commit()
conn.close()

print("✅ Database and table created successfully.")
