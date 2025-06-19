import sqlite3

def create_table():
    conn = sqlite3.connect('tracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS coding_log (
                    date TEXT,
                    platform TEXT,
                    questions_solved INTEGER,
                    time_spent INTEGER
                )''')
    conn.commit()
    conn.close()

def add_entry(date, platform, questions, time):
    conn = sqlite3.connect('tracker.db')
    c = conn.cursor()
    c.execute("INSERT INTO coding_log VALUES (?, ?, ?, ?)", (date, platform, questions, time))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect('tracker.db')
    c = conn.cursor()
    c.execute("SELECT * FROM coding_log ORDER BY date DESC")
    data = c.fetchall()
    conn.close()
    return data
