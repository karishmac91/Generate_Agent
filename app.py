import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/recommend"

st.set_page_config(page_title="Recommendation UI", layout="centered")
st.title("🔍 Recommendation System")

# Input field
applicant_id = st.text_input("Enter Applicant ID")

if st.button("Get Recommendation"):
    if not applicant_id.strip():
        st.warning("Please enter a valid Applicant ID.")
    else:
        try:
            response = requests.get(f"{API_URL}/{applicant_id}")
            if response.status_code == 200:
                data = response.json()

                try:
                    raw_recommendation = data["recommendation"]["tasks_output"][0]["raw"]
                    st.success("✅ Recommendation fetched successfully!")
                    st.markdown(f"**📋 Recommendation:**\n\n{raw_recommendation}")
                except (KeyError, IndexError, TypeError):
                    st.warning("⚠️ Could not extract the recommendation message.")
                    st.json(data)

            else:
                st.error(f"❌ Error: {response.status_code} - {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("⚠️ Could not connect to the FastAPI server. Is it running?")
