import streamlit as st
import pandas as pd
import joblib


# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="centered"
)


# -----------------------------------
# Load Saved Model
# -----------------------------------

@st.cache_resource
def load_model():
    return joblib.load(
        r"C:\Users\soura\OneDrive\Desktop\Intelligent-Loan-Approval-System\Model\loan_approval_model.pkl"
    )


model = load_model()


# -----------------------------------
# Application Title
# -----------------------------------

st.title("🏦 Loan Approval Prediction System")

st.write(
    "Enter the applicant's details to predict "
    "whether the loan is likely to be approved."
)


# -----------------------------------
# User Inputs
# -----------------------------------

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

married = st.selectbox(
    "Married",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Number of Dependents",
    [0.0, 1.0, 2.0, 3.0]
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

applicant_income = st.number_input(
    "Applicant Income",
    min_value=0,
    value=5000
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0.0,
    value=0.0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0.0,
    value=150.0
)

loan_amount_term = st.selectbox(
    "Loan Amount Term",
    [360.0, 180.0, 120.0, 480.0, 300.0, 240.0]
)

credit_history = st.selectbox(
    "Credit History",
    [1.0, 0.0]
)

property_area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)


# -----------------------------------
# Create Input DataFrame
# -----------------------------------

input_data = pd.DataFrame({
    "Gender": [gender],
    "Married": [married],
    "Dependents": [dependents],
    "Education": [education],
    "Self_Employed": [self_employed],
    "ApplicantIncome": [applicant_income],
    "CoapplicantIncome": [coapplicant_income],
    "LoanAmount": [loan_amount],
    "Loan_Amount_Term": [loan_amount_term],
    "Credit_History": [credit_history],
    "Property_Area": [property_area]
})


# -----------------------------------
# Display Input Data
# -----------------------------------

st.subheader("Applicant Information")

st.dataframe(input_data)


# -----------------------------------
# Prediction
# -----------------------------------

if st.button("Predict Loan Approval"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:

        st.success(
            "🎉 Loan is likely to be APPROVED!"
        )

    else:

        st.error(
            "❌ Loan is likely to be REJECTED."
        )