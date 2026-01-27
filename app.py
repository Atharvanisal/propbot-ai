
import streamlit as st
import csv
import os
from datetime import datetime
from transformers import pipeline

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Pune Property AI",
    page_icon="🏠",
    layout="centered"
)

# ---------- LOAD AI MODEL (FREE) ----------
@st.cache_resource
def load_ai():
    return pipeline("text-generation", model="gpt2")

ai = load_ai()

# ---------- TITLE ----------
st.title("🏠 Pune Property AI Chatbot")
st.caption("24/7 Real Estate Assistant + Lead Capture")

# ---------- CHAT ----------
st.markdown("### 🤖 Ask about Pune properties")

user_question = st.text_input("Example: 2BHK flat in Wakad under 70 lakh")

if user_question:
    with st.spinner("Thinking..."):
        response = ai(
            f"You are a real estate assistant in Pune. Answer briefly:\n{user_question}",
            max_length=80
        )
        st.success(response[0]["generated_text"])

# ---------- LEAD FORM ----------
st.markdown("---")
st.markdown("### 📞 Get a Call / WhatsApp")

name = st.text_input("Your Name")
phone = st.text_input("Phone Number")
email = st.text_input("Email (optional)")

if st.button("Submit"):
    if name and phone:
        file_exists = os.path.isfile("leads.csv")
        with open("leads.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Name", "Phone", "Email", "Date"])
            writer.writerow([name, phone, email, datetime.now().strftime("%Y-%m-%d %H:%M")])

        st.success("✅ Thank you! We will contact you shortly.")
        st.markdown(f"""
        👉 **Call:** [📞 {phone}](tel:{phone})  
        👉 **WhatsApp:** [💬 Chat](https://wa.me/91{phone})
        """)
    else:
        st.error("Please enter Name and Phone Number")

