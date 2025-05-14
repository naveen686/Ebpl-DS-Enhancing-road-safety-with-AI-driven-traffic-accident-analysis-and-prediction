import streamlit as st
import numpy as np
import pickle

st.title("🚦 Traffic Accident Severity Prediction")

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# Get user input
age = st.selectbox("Age Band of Driver", ['Under 18', '18-30', '31-50', 'Above 51'])
sex = st.selectbox("Sex of Driver", ['Male', 'Female'])
day = st.selectbox("Day of Week", ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
weather = st.selectbox("Weather Condition", ['Clear', 'Raining', 'Fog', 'Windy'])

# Encode inputs manually (must match training)
age_map = {'Under 18': 0, '18-30': 1, '31-50': 2, 'Above 51': 3}
sex_map = {'Male': 0, 'Female': 1}
day_map = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
weather_map = {'Clear': 0, 'Raining': 1, 'Fog': 2, 'Windy': 3}

# Create input array with dummy values for missing features
input_data = np.array([[
    age_map[age],
    sex_map[sex],
    day_map[day],
    weather_map[weather],
    0, 1, 0, 1, 2, 1  # Dummy values for missing 6 features
]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    severity = ['Fatal Injury', 'Serious Injury', 'Slight Injury']
    st.success(f"Predicted Accident Severity: {severity[prediction[0]]}")
    from pyngrok import ngrok

# Kill existing tunnels
ngrok.kill()

# Start Streamlit in background
# get_ipython().system_raw('streamlit run app.py &')

# Connect to ngrok
public_url = ngrok.connect(port='8501')
print("Streamlit App URL:", public_url)
