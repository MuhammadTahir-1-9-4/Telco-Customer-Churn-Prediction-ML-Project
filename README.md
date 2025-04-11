# Telco Customer Churn Prediction Project 🚀

This project focuses on predicting customer churn for a telecom company using machine learning techniques. The goal is to help the company proactively retain customers who are likely to leave, based on their historical data.

### 📊 Dataset
The dataset contains customer details such as:
- Demographics
- Account information
- Service subscriptions
- Contract details
- Payment methods
- Tenure and usage patterns

### 📂 Project Structure
- **Telco Customer Churn Analysis (EDA).ipynb**  
  Comprehensive exploratory data analysis to understand trends, correlations, and important features.
  
- **Model Building.ipynb**  
  Model training, evaluation, and selection. Achieved a high accuracy using supervised learning models.

### 🔍 Exploratory Data Analysis (EDA)
- Distribution of churned vs. retained customers
- Impact of services like Online Security, Tech Support, and Contract Type on churn
- Analysis of tenure, monthly charges, and total charges
- Correlation heatmaps and visual insights

### 🧠 Model Building, Evaluation & Explainability
- Data preprocessing and feature engineering
- Train-test split and balancing techniques
- Model training and evaluation using:
  - Accuracy
  - Precision, Recall, F1-Score
  - Confusion Matrix
  - Classification Report
- **Model Explainability with SHAP:**
  - SHAP Summary Plot (Global Feature Importance)
  - SHAP Beeswarm Plot for Class 1 (Churn)
  - SHAP Bar Plot for Class 1 (Churn)
  - Visual interpretation of feature impacts on model predictions
  
### 📈 Model Performance
**Classification Report:**

               precision    recall  f1-score   support

           0       0.97      0.94      0.95       553
           1       0.95      0.97      0.96       611

    accuracy                            0.96      1164
    macro avg       0.96      0.96      0.96      1164
    weighted avg    0.96      0.96      0.96      1164

✅ **Accuracy:** 95.6%

### 🚀 Deployment
The model is deployed using **Streamlit** for interactive customer churn prediction.  
👉 [Streamlit Live App](https://telco-customer-churn-prediction-ml-project.streamlit.app/)

### 📌 Conclusion
- Achieved excellent performance with ~96% accuracy.
- Identified key factors contributing to customer churn.
- Deployed a user-friendly web app for real-time predictions.

### 🧩 Future Improvements
- Incorporate real-time data streams
- Implement automated re-training

### 🤝 Let's Connect!
If you find this project interesting, feel free to connect with me:
- 🔗 [LinkedIn](https://www.linkedin.com/in/muhammad-tahir-data/)
- 🌟 Star the repo if you liked it!


