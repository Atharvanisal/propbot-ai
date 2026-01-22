import streamlit as st
import csv
from datetime import datetime

st.set_page_config(page_title="PropBot AI", layout="centered")

st.title("🏠 PropBot AI – Pune")
st.write("24/7 Property Assistant + Lead Capture")

user_msg = st.text_input("Looking for property in Pune?")

st.markdown("---")
st.subheader("📞 Schedule a Property Call")

name = st.text_input("Your Name")
phone = st.text_input("Phone Number")
email = st.text_input("Email (optional)")
property_type = st.selectbox(
    "Property Requirement",
    ["Buy", "Rent", "Commercial", "Investment"]
)

def save_lead():
    with open("leads.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            name,
            phone,
            email,
            property_type,
            user_msg,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])

if st.button("Submit"):
    if name and phone:
        save_lead()
        st.success("Thank you! Our team will contact you soon.")
    else:
        st.error("Please enter name and phone number")
