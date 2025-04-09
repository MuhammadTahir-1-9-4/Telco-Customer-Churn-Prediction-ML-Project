# Telco Customer Churn Prediction 🚀

Welcome to the Telco Customer Churn Prediction project!  
In this project, I analyzed Telco customer data to identify factors contributing to customer churn and built a predictive model to help the business reduce churn and retain customers.

## 📌 Project Overview

- **Author:** Muhammad Tahir  
- **Date:** 30 March 2025
- **Goal:** Predict customer churn using machine learning models and provide actionable insights.

## 📊 Dataset

The dataset contains customer information like demographics, account details, and services subscribed.  
Target variable: **Churn** (Yes/No)

**Key features include:**
- Customer demographics (gender, senior citizen status, dependents)
- Account information (tenure, contract type, payment method)
- Services availed (internet service, online security, tech support)
- Charges (monthly charges, total charges)

## 🧩 Project Workflow

### 1. Exploratory Data Analysis (EDA)
- Explored distributions of key variables.
- Visualized relationships between features and churn.
- Identified high-risk segments:
  - Month-to-month contracts.
  - Electronic check payments.
  - Short-tenure customers.
  - Higher monthly charges increase churn probability.

### 2. Data Preprocessing
- Cleaned the dataset (removed unnecessary columns).
- Encoded categorical variables using **LabelEncoder**.
- Addressed class imbalance using **SMOTEENN** (combination of over- and under-sampling).

### 3. Model Building
- Selected **Random Forest Classifier** for its robustness and interpretability.
- Performed hyperparameter tuning using **GridSearchCV** to improve performance.

### 4. Model Evaluation
- Evaluated model performance using:
  - **Accuracy Score**
  - **Confusion Matrix**
  - **Classification Report (Precision, Recall, F1-score)**
- Final model achieved solid results in classifying churn vs. non-churn.

### 5. Model Saving
- Serialized the final model using **pickle** for future predictions.

## 🛠️ Tools & Technologies
- Python 🐍
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- imbalanced-learn (SMOTEENN)
- Pickle

## 📂 Repository Structure

```
├── Telco Customer Churn Analysis (EDA).ipynb  # EDA and insights
├── Model Building.ipynb                       # Model training and evaluation
├── Telco-customer-churn(cleaned).csv          # Cleaned dataset
└── README.md                                  # Project documentation
```

## 🚀 Future Work
- Test with more advanced models (XGBoost, LightGBM).
- Integrate SHAP for explainability.

## 🤝 Let's Connect!
If you liked this project or have suggestions, feel free to connect!
