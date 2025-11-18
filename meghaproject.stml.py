import streamlit as st
import pickle
import numpy as np

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Loan Default Prediction",
   
)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = pickle.load(open("C:/Users/HP/Downloads/Megha_project1.pkl", "rb"))



# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title(" Navigation")
st.sidebar.success("Use this panel to navigate options")

st.sidebar.markdown("""
### About this App  
This app predicts whether a customer will **default on a loan** based on multiple financial and personal factors.
""")

# -----------------------------
# HEADER
# -----------------------------
st.markdown("<h1 style='text-align: center; color: #2E4053;'>💼 Loan Default Prediction System</h1>", 
            unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>Enter the loan details below</p>", 
            unsafe_allow_html=True)

# -----------------------------
# USER INPUT LAYOUT
# -----------------------------
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        loan_id = st.number_input("Loan ID", min_value=1)
        customer_id = st.number_input("Customer ID", min_value=1)
        gender = st.selectbox("Gender", ["Female (0)", "Male (1)"])
        age = st.number_input("Age", min_value=18, max_value=100)
        income = st.number_input("Income")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        loan_amount = st.number_input("Loan Amount")
        loan_term = st.number_input("Loan Term (Months)")
        credit_score = st.number_input("Credit Score")
        employment_type = st.selectbox("Employment Type", 
                                        ["Salaried (0)", "Self-Employed (1)", "Business (2)", "Others (3)"])
        marital_status = st.selectbox("Marital Status", ["Single (0)", "Married (1)", "Divorced (2)"])
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        num_of_dependents = st.number_input("Number of Dependents", min_value=0)
        existing_loan_count = st.number_input("Existing Loan Count", min_value=0)
        emi_per_month = st.number_input("EMI Per Month")
        loan_purpose = st.selectbox("Loan Purpose", 
                                    ["Personal (0)", "Education (1)", "Home (2)", "Business (3)", "Vehicle (4)"])
        loan_providing_date = st.number_input("Loan Providing Date (YYYYMMDD)", min_value=20200101)
        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# PREPARE INPUT
# -----------------------------
gender_val = 1 if gender == "Male (1)" else 0

input_data = np.array([[
    loan_id, customer_id, gender_val, age, income, loan_amount, loan_term,
    credit_score, 
    int(employment_type[-2]),   # extract 0/1/2/3
    int(marital_status[-2]),    # extract 0/1/2
    num_of_dependents, existing_loan_count, emi_per_month,
    int(loan_purpose[-2]),      # extract 0/1/2/3/4
    loan_providing_date
]])

# -----------------------------
# PREDICTION
# -----------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'> Click to Predict</h3>", unsafe_allow_html=True)

if st.button("Predict Loan Default"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Risk: The customer may default on the loan!")
    else:
        st.success("Low Risk: The customer is unlikely to default.")

