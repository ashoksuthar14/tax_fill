import streamlit as st
from agents.extract_agent import ExtractAgent
from agents.fill_agent import FillAgent
import os

# Ensure directories exist
UPLOAD_DIR = './data/uploads/'
FILLED_DIR = './data/filled/'
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(FILLED_DIR, exist_ok=True)

# Streamlit UI for Crew AI Form Filler
st.title("Crew AI - Form Filler")

st.header("Step 1: Upload Form (PDF)")
uploaded_file = st.file_uploader("Choose a file", type=["pdf"])

if uploaded_file is not None:
    # Save the uploaded file to 'data/uploads/'
    save_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(save_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    st.header("Step 2: Enter Your Financial Details")

    # Collect user inputs
    income = st.text_input("Income")
    investments = st.text_input("Investments")
    insurance = st.text_input("Insurance")
    loan = st.text_input("Loan")
    expenses = st.text_input("Expenses")

    # Process the form submission
    if st.button("Fill Form"):
        user_data = {
            'income': income,
            'investments': investments,
            'insurance': insurance,
            'loan': loan,
            'expenses': expenses
        }

        # Step 1: Extract data using Crew AI
        extract_agent = ExtractAgent(pdf_path=save_path)
        extracted_data = extract_agent.extract_data()

        # Step 2: Fill the form with the user-provided data
        fill_agent = FillAgent(extracted_data, user_data)
        filled_form_path = fill_agent.fill_form()

        # Ensure the filled form is in the right directory
        filled_form_full_path = os.path.join(FILLED_DIR, os.path.basename(filled_form_path))

        # Display the result
        st.success(f"Form filled successfully! Saved at: {filled_form_full_path}")
        st.download_button(
            "Download Filled Form", 
            open(filled_form_full_path, 'rb').read(), 
            file_name="filled_form.pdf"
        )
