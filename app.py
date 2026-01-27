import streamlit as st
import csv
import os
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Business Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("🤖 AI Business Chatbot")
st.caption("24/7 assistant + lead capture")

# ---------------- CHAT ----------------
question = st.text_input("Ask your question")

st.markdown("---")
st.markdown("### 📩 Get a call back")

name = st.text_input("Your Name")
phone = st.text_input("Phone Number")
email = st.text_input("Email (optional)")

if st.button("Submit"):
    if name and phone:
        file_exists = os.path.exists("leads.csv")

        with open("leads.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            # HEADER (only once)
            if not file_exists:
                writer.writerow([
                    "Date",
                    "Name",
                    "Phone",
                    "Email",
                    "Question"
                ])

            writer.writerow([
                datetime.now().strftime("%d-%m-%Y %H:%M"),
                name,
                f"'{phone}",   # 👈 forces TEXT in Excel
                email,
                question
            ])

        st.success("✅ Lead saved successfully!")
    else:
        st.error("Name and Phone are required")

# ---------------- DOWNLOAD ----------------
st.markdown("---")
st.markdown("### 📊 Download Leads")

if os.path.exists("leads.csv"):
    with open("leads.csv", "rb") as f:
        st.download_button(
            "⬇️ Download leads.csv",
            f,
            file_name="leads.csv",
            mime="text/csv"
        )
else:
    st.info("No leads yet")
