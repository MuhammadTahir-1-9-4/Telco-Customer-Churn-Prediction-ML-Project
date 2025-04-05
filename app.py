import streamlit as st
import pickle
import pandas as pd


MODEL_PATH = 'Churn_model.pkl'
COLUMNS_PATH = 'trained_columns.pkl'

model = pickle.load(open(MODEL_PATH, 'rb'))
model_columns = pickle.load(open(COLUMNS_PATH, 'rb'))


st.sidebar.title("About this app")
st.sidebar.info(
    """
    **Telco Customer Churn Prediction App**  
    - Predict if a customer will churn.  
    - Built with a Random Forest Model.  
    - Created by Muhammad Tahir.  
    """
)

st.sidebar.markdown("---")
st.sidebar.caption("🚀 Model trained on Telco Customer dataset using scikit-learn.")


st.title("📊 Telco Customer Churn Prediction")
st.write("Fill out customer details below to check if they are likely to churn.")

# input fields
gender = st.selectbox('Gender', ['Male', 'Female'])
senior_citizen = st.selectbox('Senior Citizen', ['No', 'Yes'])
partner = st.selectbox('Partner', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['Yes', 'No'])
tenure = st.slider('Tenure (Months)', 0, 72, 12)
internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
payment_method = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Credit card (automatic)', 'Bank transfer (automatic)'])
monthly_charges = st.number_input('Monthly Charges', min_value=0.0)
total_charges = st.number_input('Total Charges', min_value=0.0)
online_security = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])
device_protection = st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'])
tech_support = st.selectbox('Tech Support', ['Yes', 'No', 'No internet service'])

# prepare input dictionary with all columns initialized to zero
input_dict = dict.fromkeys(model_columns, 0)

# function to encode categorical features
def encode_feature(feature, value, prefix=None):
    column_name = f"{prefix}_{value}" if prefix else feature
    if column_name in input_dict:
        input_dict[column_name] = 1

# map binary features
input_dict['gender'] = 1 if gender=='Male' else 0
input_dict['SeniorCitizen'] = 1 if senior_citizen=='Yes' else 0
input_dict['Partner'] = 1 if partner=='Yes' else 0
input_dict['Dependents'] = 1 if dependents=='Yes' else 0
input_dict['tenure'] = tenure
input_dict['MonthlyCharges'] = monthly_charges
input_dict['TotalCharges'] = total_charges

# encode categorical features
encode_feature('InternetService', internet_service, 'InternetService')
encode_feature('Contract', contract, 'Contract')
encode_feature('PaymentMethod', payment_method, 'PaymentMethod')
encode_feature('OnlineSecurity', online_security, 'OnlineSecurity')
encode_feature('DeviceProtection', device_protection, 'DeviceProtection')
encode_feature('TechSupport', tech_support, 'TechSupport')

# encode tenure groups
if tenure < 12:
    encode_feature('tenure_group', '0-12', 'tenure_group')
elif tenure < 24:
    encode_feature('tenure_group', '13-24', 'tenure_group')
else:
    encode_feature('tenure_group', '25+', 'tenure_group')

# fill missing columns with 0
        
input_dict['StreamingTV_No internet service'] = 0
input_dict['StreamingMovies_No internet service'] = 0

# convert to DataFrame
input_df = pd.DataFrame([input_dict])
input_df = input_df.reindex(columns=model_columns, fill_value=0)

if st.button('Predict'):
    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1] * 100

    if prediction == 1:
        st.error(f"⚠️ This customer is likely to churn.\n\n**Model confidence: {prob:.2f}%**")
    else:
        st.success(f"✅ This customer is not likely to churn.\n\n**Model confidence: {prob:.2f}%**")

    st.markdown("### Why this prediction?")
    explanation = ""
    if senior_citizen == 'Yes':
        explanation += "- Senior citizens have a higher churn rate. ❗\n"
    if contract == 'Month-to-month':
        explanation += "- Month-to-month contract, more likely to churn. ❗\n"
    else:
        explanation += "- Long-term contract indicates loyalty. ✅\n"
    if internet_service == 'Fiber optic':
        explanation += "- Fiber optic customers churn more, possibly due to cost. ❗\n"
    if payment_method == 'Electronic check':
        explanation += "- Electronic check users have a higher churn rate. ❗\n"
    if online_security == 'No':
        explanation += "- No online security, which increases churn risk. ❗\n"
    if device_protection == 'No':
        explanation += "- Lacking device protection. ❗\n"
    if tech_support == 'No':
        explanation += "- No tech support, increasing churn risk. ❗\n"
    if monthly_charges > 70:
        explanation += "- Higher monthly charges are linked to churn. ❗\n"
    if tenure < 12:
        explanation += "- Low tenure (new customer), higher churn risk. ❗\n"
    if dependents == 'No':
        explanation += "- No dependents, higher likelihood of switching services. ❗\n"
    if partner == 'No':
        explanation += "- Single customers are more likely to churn. ❗\n"
    
    st.info(explanation)
