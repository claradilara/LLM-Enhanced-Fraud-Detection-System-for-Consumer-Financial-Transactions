

# 💳 LLM-Enhanced Fraud Detection System
### Consumer Financial Transactions | Big Data | GenAI

## 📌 Project Overview
Financial institutions process millions of consumer transactions daily, where fraudulent activity is rare but highly costly.
Traditional fraud detection models can flag suspicious behavior but often lack interpretability, making investigation and compliance difficult.

This project implements an end-to-end fraud detection pipeline that combines:
- Behavioral feature engineering on consumer transaction data
- Cost-aware machine learning for fraud detection
- A Large Language Model (LLM) layer that translates model outputs into human-readable explanations

The system is designed to reflect real-world banking constraints such as anonymized features, extreme class imbalance, and explainability requirements.

---

## 🧠 System Architecture
Raw Transactions  
→ Feature Engineering  
→ Fraud Detection Model  
→ Fraud Probability  
→ LLM-Based Explanation  
→ Analyst-Readable Output  

---

## 🗂️ Repository Structure
fraud-detection-llm/
├── data/
│ ├── raw/ # Local only (not committed)
│ └── processed/ # Local only (not committed)
│
├── notebooks/
│ ├── EDA.ipynb
│ ├── Feature_Engineering.ipynb
│ ├── Model_Training.ipynb
│ └── LLM_Explanation_Demo.ipynb
│
├── src/
│ └── llm_explainer.py
│
├── README.md
├── requirements.txt
└── .gitignore

---

## 💾 Data
This project uses the IEEE-CIS Fraud Detection dataset.
Due to size and licensing constraints, raw and processed datasets are not stored in this repository.

To run locally:
1. Download the dataset from Kaggle
2. Place files under `data/raw/`
3. Run notebooks in order

---

## ⚙️ Feature Engineering
Engineered features capture key fraud signals:
- Abnormal transaction amounts
- Transaction velocity and burst behavior
- Time since previous transaction
- Missing identity and device signals
- Time-of-day risk indicators

Missing values arise naturally from behavioral features and are handled using median imputation.

---

## 🤖 Fraud Detection Model
A cost-aware Logistic Regression model is trained as a transparent baseline.
Evaluation focuses on Precision–Recall metrics due to extreme class imbalance.

Threshold tuning is used to balance fraud recall and investigation cost.

---

## ✨ LLM-Based Fraud Explanations
An explanation layer converts model scores and transaction-level features into analyst-friendly narratives.

Some fraud cases are driven by a single dominant signal (e.g., missing identity data).
Explanations intentionally reflect actual feature values rather than artificially inflating narratives.

See `notebooks/LLM_Explanation_Demo.ipynb` for examples.

---

## 🚀 Technologies
Python, Pandas, NumPy, Scikit-learn, Jupyter Notebook, Large Language Models

---

## 📌 Disclaimer
This project is for educational and demonstration purposes only.

---

## 👩‍💻 Author
Dilara  
Data Science | Risk Modeling | GenAI


===================== requirements.txt =====================

pandas
numpy
scikit-learn
matplotlib
jupyter


======================= .gitignore =========================

# Data (NEVER COMMIT)
data/
*.csv
*.parquet

# Jupyter
.ipynb_checkpoints/

# Python
__pycache__/
*.pyc
