import streamlit as st
import pandas as pd
import sqlite3

# --- DATABASE FETCH ---
def fetch_all():
    conn = sqlite3.connect("coding_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM coding_data")  # Adjust table name if needed
    data = cursor.fetchall()
    conn.close()
    return data

# --- PAGE TITLE ---
st.set_page_config(page_title="Daily Coding Tracker", layout="wide")
st.title("💻 Daily Coding Tracker Dashboard")

# --- LOAD & CLEAN DATA ---
data = fetch_all()
df = pd.DataFrame(data, columns=["Date", "Platform", "Questions", "Time (min)"])
df["Date"] = pd.to_datetime(df["Date"])

# --- FILTERING DATES ---
today = pd.to_datetime("today").normalize()
this_week = df[df["Date"] >= today - pd.Timedelta(days=7)]
this_month = df[df["Date"].dt.month == today.month]

# --- CALCULATE METRICS ---
total_questions_week = this_week["Questions"].sum()
total_time_month = this_month["Time (min)"].sum()
best_day_row = df.loc[df["Questions"].idxmax()]
best_day = best_day_row["Date"].strftime("%b %d, %Y")

# --- METRIC CARDS ---
st.markdown("### 📊 Weekly & Monthly Highlights")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("✅ Questions This Week", int(total_questions_week))

with col2:
    st.metric("⏱️ Time This Month", f"{int(total_time_month)} min")

with col3:
    st.metric("🏆 Best Day", best_day)

# --- RECENT ACTIVITY TABLE ---
st.markdown("### 📅 Recent Activity")
recent = df.sort_values("Date", ascending=False).head(10)
st.dataframe(recent, use_container_width=True)

# --- FOOTER ---
st.markdown("---")
st.caption("Built by Sarayu • Track your daily coding & grow 🚀")
