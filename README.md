# 🔐 AI-Powered Financial Fraud Detection System

An AI/ML-based web application that detects potentially fraudulent financial transactions using a machine learning model. The project provides a simple Streamlit interface where users can enter transaction details and receive a fraud prediction.

## 📌 Project Overview

Financial fraud is a major challenge for banks and financial institutions. This project uses machine learning to analyze transaction-related features and identify whether a transaction is likely to be **fraudulent or legitimate**.

The system is designed as a beginner-friendly end-to-end ML project covering:

- Data preprocessing
- Exploratory data analysis
- Machine learning model training
- Fraud prediction
- Model serialization
- Streamlit web application
- GitHub project deployment

## 🚀 Features

- 🔍 Fraudulent transaction detection
- 📊 Transaction data analysis
- 🤖 Machine learning-based prediction
- 🌐 Interactive Streamlit interface
- 📈 Fraud probability display
- 💻 Easy-to-use transaction input form
- 📁 Trained model integration

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Seaborn**
- **Streamlit**
- **Jupyter Notebook**
- **Git & GitHub**

## 📂 Project Structure

```text
AI-Fraud-Detection-System/
│
├── app.py
├── Fraud_Detection_System.ipynb
├── fraud_detection_pipeline.pkl
├── requirements.txt
├── README.md
├── logs.txt
└── sample_data/
```

## 📊 Dataset

The project uses a financial transaction dataset containing features such as:

- `step`
- `type`
- `amount`
- `nameOrig`
- `oldbalanceOrg`
- `newbalanceOrig`
- `nameDest`
- `oldbalanceDest`
- `newbalanceDest`
- `isFraud`

The target variable is:

```text
isFraud
```

where:

- `0` → Legitimate transaction
- `1` → Fraudulent transaction

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/AI-Fraud-Detection-System.git
```

Move into the project directory:

```bash
cd AI-Fraud-Detection-System
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Streamlit Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔎 How It Works

1. User enters transaction details.
2. The application prepares the input data.
3. The trained machine learning pipeline processes the transaction.
4. The model predicts whether the transaction is fraudulent.
5. The application displays the prediction and fraud probability when supported.

## 📈 Model

The trained model is saved as a `.pkl` file and loaded by the Streamlit application.

The model pipeline handles the required preprocessing and prediction steps for the transaction data.

## 🌐 Deployment

This project can be deployed using **Streamlit Community Cloud**.

Basic deployment steps:

1. Upload the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Select `app.py` as the main file.
5. Deploy the application.

## 📌 Example Prediction

The application provides results such as:

```text
✅ Transaction Appears Legitimate
```

or

```text
🚨 Potential Fraudulent Transaction Detected
```

## 🎯 Future Improvements

- Improve model accuracy and fraud detection performance
- Handle class imbalance using advanced techniques
- Add real-time transaction monitoring
- Add interactive fraud analytics dashboards
- Compare multiple machine learning algorithms
- Add authentication and user management
- Deploy the system on a production cloud platform

## 👩‍💻 Author

**Smita Kumari**

B.Tech Computer Science & Engineering

AI/ML & Software Development Project

## 📜 License

This project is intended for educational and demonstration purposes.
