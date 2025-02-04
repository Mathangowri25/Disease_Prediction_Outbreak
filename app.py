import streamlit as st
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Set colorful background
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Load trained models
diabetes_model_path = "/mnt/data/diabetes_model.sav"
parkinsons_model_path = "/mnt/data/Parkinsons_model.sav"
heart_model_path = "/mnt/data/heart_disease_model.sav"
heart_data_path = "/mnt/data/heart.csv"

diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))
parkinsons_model = pickle.load(open(parkinsons_model_path, 'rb'))

st.title("🩺 Disease Prediction System")
st.markdown("---")

# Sidebar selection with color
st.sidebar.header("🔍 Select Disease")
disease = st.sidebar.selectbox("Choose a Disease", ["Diabetes", "Parkinson's", "Heart Disease"], index=0)

if disease == "Diabetes":
    st.header("🟠 Diabetes Prediction")
    st.markdown("Fill the details below to predict Diabetes:")

    pregnancies = st.number_input("🤰 Pregnancies", min_value=0, step=1)
    glucose = st.number_input("🩸 Glucose Level", min_value=0)
    blood_pressure = st.number_input("❤️ Blood Pressure", min_value=0)
    skin_thickness = st.number_input("🩹 Skin Thickness", min_value=0)
    insulin = st.number_input("💉 Insulin Level", min_value=0)
    bmi = st.number_input("⚖️ BMI", min_value=0.0, format="%.2f")
    dpf = st.number_input("🧬 Diabetes Pedigree Function", min_value=0.0, format="%.3f")
    age = st.number_input("🎂 Age", min_value=0, step=1)
    
    if st.button("🔮 Predict Diabetes", key="diabetes"):
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
        prediction = diabetes_model.predict(input_data)
        st.success("✅ Diabetes Positive" if prediction[0] == 1 else "❌ Diabetes Negative")
    
    # Visualization
    st.write("### Feature Distribution")
    df = pd.DataFrame(input_data, columns=["Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness", "Insulin", "BMI", "DPF", "Age"])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, ax=ax)
    st.pyplot(fig)

elif disease == "Parkinson's":
    st.header("🟢 Parkinson's Prediction")
    st.markdown("Fill the details below to predict Parkinson's:")

    fo = st.number_input("🎵 MDVP:Fo(Hz)")
    fhi = st.number_input("📈 MDVP:Fhi(Hz)")
    flo = st.number_input("📉 MDVP:Flo(Hz)")
    jitter_percent = st.number_input("🔬 Jitter(%)")
    shimmer = st.number_input("✨ Shimmer")
    nhr = st.number_input("📡 NHR")
    hnr = st.number_input("🔊 HNR")
    rpde = st.number_input("🌀 RPDE")
    dfa = st.number_input("📏 DFA")
    spread1 = st.number_input("📊 Spread1")
    spread2 = st.number_input("📊 Spread2")
    d2 = st.number_input("🔢 D2")
    ppe = st.number_input("🎭 PPE")
    
    if st.button("🔮 Predict Parkinson's", key="parkinsons"):
        input_data = np.array([[fo, fhi, flo, jitter_percent, shimmer, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])
        prediction = parkinsons_model.predict(input_data)
        st.success("✅ Parkinson's Positive" if prediction[0] == 1 else "❌ Parkinson's Negative")
    
    # Visualization
    st.write("### Feature Distribution")
    df = pd.DataFrame(input_data, columns=["Fo", "Fhi", "Flo", "Jitter %", "Shimmer", "NHR", "HNR", "RPDE", "DFA", "Spread1", "Spread2", "D2", "PPE"])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, ax=ax)
    st.pyplot(fig)

elif disease == "Heart Disease":
    st.header("❤️ Heart Disease Prediction")
    st.markdown("Fill the details below to predict Heart Disease:")

    age = st.number_input("🎂 Age", min_value=0, step=1)
    sex = st.selectbox("⚤ Sex", ["Male", "Female"])
    chest_pain_type = st.selectbox("💔 Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
    resting_blood_pressure = st.number_input("❤️ Resting Blood Pressure (mm Hg)", min_value=0)
    cholesterol = st.number_input("🩸 Serum Cholesterol (mg/dl)", min_value=0)
    blood_sugar = st.selectbox("🩹 Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
    electrocardiographic = st.selectbox("📊 Electrocardiographic Results", ["Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy"])
    maximum_heart_rate = st.number_input("💓 Maximum Heart Rate Achieved", min_value=0)
    exercise_induced_angina = st.selectbox("🏃 Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.number_input("📉 Oldpeak (depression induced by exercise relative to rest)", min_value=0.0, format="%.2f")
    slope = st.selectbox("🔺 Slope of Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    vessels = st.selectbox("🫀 Number of Major Vessels Colored by Fluoroscopy", [0, 1, 2, 3])
    thalassemia = st.selectbox("🧬 Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

    # Convert categorical values to numerical representation
    sex = 1 if sex == "Male" else 0
    blood_sugar = 1 if blood_sugar == "Yes" else 0
    exercise_induced_angina = 1 if exercise_induced_angina == "Yes" else 0
    slope = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}[slope]
    electrocardiographic = {"Normal": 0, "Having ST-T wave abnormality": 1, "Showing probable or definite left ventricular hypertrophy": 2}[electrocardiographic]
    chest_pain_type = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}[chest_pain_type]
    thalassemia = {"Normal": 0, "Fixed Defect": 1, "Reversible Defect": 2}[thalassemia]

    if st.button("🔮 Predict Heart Disease", key="heart_disease"):
        input_data = np.array([[age, sex, chest_pain_type, resting_blood_pressure, cholesterol, blood_sugar, electrocardiographic,
                                maximum_heart_rate, exercise_induced_angina, oldpeak, slope, vessels, thalassemia]])

        heart_disease_model = pickle.load(open(heart_model_path, 'rb'))
        prediction = heart_disease_model.predict(input_data)

        st.success("✅ Heart Disease Positive" if prediction[0] == 1 else "❌ Heart Disease Negative")
    
    # Visualization
    st.write("### Feature Distribution")
    df = pd.DataFrame(input_data, columns=["Age", "Sex", "Chest Pain Type", "Resting BP", "Cholesterol", "Blood Sugar", "ECG", 
                                           "Max Heart Rate", "Exercise Induced Angina", "Oldpeak", "Slope", "Vessels", "Thalassemia"])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, ax=ax)
    st.pyplot(fig)
