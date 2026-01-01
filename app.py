import streamlit as st
import pandas as pd
import pickle


with open("bank.pkl", "rb") as f:
    saved = pickle.load(f)

model = saved["model"]
onehot = saved["onehot"]
scaler = saved["scaler"]

def get_age_group(age):
    if age <= 30:
        return "Young"
    elif age <= 50:
        return "Adult"
    else:
        return "Senior"

def get_balance_group(balance):
    if balance < 0:
        return "Negative"
    elif balance < 5000:
        return "Low"
    elif balance < 20000:
        return "Medium"
    else:
        return "High"

st.set_page_config(page_title="Bank Deposit Prediction", layout="centered")
st.title("🏦 Bank Deposit Prediction App")
st.write("Predict whether a customer will subscribe to a term deposit")


age = st.number_input("Age", 18, 100)
balance = st.number_input("Balance")
day = st.number_input("Day", 1, 31)
campaign = st.number_input("Campaign Contacts", 1)
pdays = st.number_input("Pdays (-1 if none)")
previous = st.number_input("Previous Contacts", 0)

job = st.selectbox("Job", [
    "admin.","technician","services","management","retired",
    "student","blue-collar","self-employed","entrepreneur",
    "housemaid","unemployed","unknown"
])

marital = st.selectbox("Marital Status", ["married","single","divorced"])
education = st.selectbox("Education", ["primary","secondary","tertiary","unknown"])
default = st.selectbox("Default", ["yes","no"])
housing = st.selectbox("Housing Loan", ["yes","no"])
loan = st.selectbox("Personal Loan", ["yes","no"])
contact = st.selectbox("Contact Type", ["cellular","telephone","unknown"])
month = st.selectbox("Month", [
    "jan","feb","mar","apr","may","jun",
    "jul","aug","sep","oct","nov","dec"
])
poutcome = st.selectbox("Previous Outcome", ["success","failure","unknown"])

if st.button("Predict"):

    
    age_group = get_age_group(age)
    balance_group = get_balance_group(balance)

    input_df = pd.DataFrame([{
        "age": age,
        "balance": balance,
        "day": day,
        "campaign": campaign,
        "pdays": pdays,
        "previous": previous,
        "job": job,
        "marital": marital,
        "education": education,
        "default": default,
        "housing": housing,
        "loan": loan,
        "contact": contact,
        "month": month,
        "poutcome": poutcome,
        "age_group": age_group,
        "balance_group": balance_group
    }])

    num_cols = ["age","balance","day","campaign","pdays","previous"]
    cat_cols = [
        "job","marital","education","default","housing","loan",
        "contact","month","poutcome","age_group","balance_group"
    ]

   
    cat_encoded = onehot.transform(input_df[cat_cols])
    cat_df = pd.DataFrame(
        cat_encoded,
        columns=onehot.get_feature_names_out(cat_cols)
    )

   
    combined_df = pd.concat(
        [input_df[num_cols].reset_index(drop=True),
         cat_df.reset_index(drop=True)],
        axis=1
    )

   
    final_input = scaler.transform(combined_df)

    prediction = model.predict(final_input)[0]

    if prediction == 1:
        st.success("✅ Customer WILL subscribe to the deposit")
    else:
        st.warning("❌ Customer will NOT subscribe to the deposit")
