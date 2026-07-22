import streamlit as st
import pandas as pd
import joblib
from pathlib import Path



st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="centered"
)



BASE_DIR = Path(r"Intelligent-Loan-Approval-System/App/app.py").resolve().parent.parent

MODEL_PATH = BASE_DIR / "Model" / "loan_approval_model.pkl"




@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()



st.title("🏦 Loan Approval Prediction System")

st.write(
    "Enter the applicant's details to predict "
    "whether the loan is likely to be approved."
)



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
    [0, 1, 2, 3]
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
    [360, 180, 120, 480, 300, 240]
)

credit_history = st.selectbox(
    "Credit History",
    [1.0, 0.0]
)

property_area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)



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



st.subheader("Applicant Information")

st.dataframe(input_data)




if st.button("Predict Loan Approval"):

    try:

        prediction = model.predict(input_data)

        if prediction[0] == 1:

            st.success(
                "🎉 Loan is likely to be APPROVED!"
            )

        else:

            st.error(
                "❌ Loan is likely to be REJECTED."
            )

    except Exception as e:

        st.error(f"Prediction Error: {e}")