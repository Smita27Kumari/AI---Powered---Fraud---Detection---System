import joblib
import pandas as pd
import streamlit as st

model = joblib.load("fraud_model.pkl")

st.title("💳 Fraud Detection System")
st.write("Enter transaction details.")

step = st.number_input("Step", min_value=0, value=1)

transaction_type = st.selectbox(
    "Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"]
)

amount = st.number_input("Amount", min_value=0.0, value=0.0)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0, value=0.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0, value=0.0)
oldbalanceDest = st.number_input(
    "Old Balance Destination", min_value=0.0, value=0.0
)
newbalanceDest = st.number_input(
    "New Balance Destination", min_value=0.0, value=0.0
)

if st.button("Predict"):
  data = pd.DataFrame([{
      "step": step,
      "type": transaction_type,
      "amount": amount,
      "nameOrig": "C1234567890",
      "oldbalanceOrg": oldbalanceOrg,
      "newbalanceOrig": newbalanceOrig,
      "nameDest": "C9876543210",
      "oldbalanceDest": oldbalanceDest,
      "newbalanceDest": newbalanceDest,
  }])

  # Prediction aur Probability dono nikalein
  prediction = model.predict(data)[0]
  probability = model.predict_proba(data)[0][
      1
  ]  # Class 1 (Fraud) ki probability (0 se 1 ke beech)
  fraud_percentage = probability * 100

  st.divider()

  # 1. Final Result
  if prediction == 1:
    st.error("🚨 Fraudulent Transaction")
  else:
    st.success("✅ Legitimate Transaction")

  # 2. Fraud Probability aur Progress Bar
  st.subheader(f"Fraud Probability: {fraud_percentage:.2f}%")
  st.progress(float(probability))

  # 3. Risk Level Category
  if fraud_percentage >= 75:
    st.error("🔴 Risk Level: **HIGH RISK** (Turant block ya verify karein)")
  elif fraud_percentage >= 30:
    st.warning("🟡 Risk Level: **MEDIUM RISK** (Additional OTP/verification zaroori hai)")
  else:
    st.info("🟢 Risk Level: **LOW RISK** (Transaction safe lag rahi hai)")