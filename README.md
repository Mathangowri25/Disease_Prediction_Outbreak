# 🏥 Prediction of Disease Outbreak  

## 📌 Overview  
This project is a **Disease Outbreak Prediction System** that leverages **machine learning** to predict the likelihood of diseases such as **Diabetes, Heart Disease, and Parkinson's Disease** based on user input. The system is built using **Streamlit** for the user interface and **scikit-learn** for machine learning model implementation.

## 🚀 Features  
- 🏥 **Predicts three diseases:**  
  - 🟠 **Diabetes**  
  - ❤️ **Heart Disease**  
  - 🟢 **Parkinson's Disease**  
- 📊 **Interactive Web Interface:** Built with **Streamlit** for ease of use.  
- 📉 **Data Visualization:** Uses **Matplotlib** and **Seaborn** for insightful visualizations.  
- ⚡ **Fast and Lightweight:** Runs efficiently using **scikit-learn** models.  

---

## 🛠️ Technologies Used  
- **Python** 🐍  
- **NumPy** – Data processing  
- **Pandas** – Data manipulation  
- **Matplotlib** – Data visualization  
- **Seaborn** – Advanced visualization  
- **Scikit-learn** – Machine learning models  
- **Streamlit** – Web application framework  

---

Here's an **enhanced project structure** that clearly shows where each model is used and how the files are organized:  

---
## 📂 **Enhanced Project Structure**  
```
📦 Disease Outbreak Prediction  
│-- 📜 README.md              # Project Documentation  
│-- 📜 app.py                 # Streamlit Web App (Main Application)  
│-- 📂 models                 # Directory for ML Models used for Saveing
│   │-- 📜 diabetes_model.sav   
│   │-- 📜 heart_model.sav       
│   │-- 📜 parkinsons_model.sav  
│-- 📂 datasets               # Contains raw & processed datasets  
│   │-- 📜 diabetes.csv          
│   │-- 📜 heart.csv              
│   │-- 📜 parkinsons.csv        
│-- 📂 images                 # Stores UI and result screenshots  
│   │-- 📜 diabetes.png           
│   │-- 📜 heart.png             
│   │-- 📜 parkinsons.png        
│-- 📂 Jupyter notebooks              # Jupyter Notebooks for Model Training  
│   │-- 📜 diabetes_training.ipynb     
│   │-- 📜 heart_training.ipynb      
│   │-- 📜 parkinsons_training.ipynb   
│-- 📜 requirements.txt        # Required dependencies  
│-- 📜 .gitignore              # Files to ignore in Git  
```

---

### 🛠 **Key Enhancements**
✔ **Models stored separately** (`models/`) for better organization.  
✔ **Datasets directory** (`datasets/`) to store CSV files used for training.  
✔ **Jupyter Notebooks folder** (`notebooks/`) for training documentation.  
✔ **Screenshots stored** in the (`images/`) folder for documentation purposes.  

---

This structure keeps everything modular, making it easier to maintain and extend in the future. Would you like any more improvements? 😊

---

## 🎯 How to Run  
### 1️⃣ Install Dependencies  
First, install the required libraries:  
```bash
pip install numpy pandas matplotlib seaborn scikit-learn streamlit
```

### 2️⃣ Run the Application  
```bash
streamlit run app.py
```

### 3️⃣ Open in Browser  
After running the command, the Streamlit app will open in your **default web browser**.

---

## 🏥 Disease Prediction Models  
### **1️⃣ Diabetes Prediction**  
Takes input such as glucose level, BMI, insulin, and more to predict diabetes.  

### **2️⃣ Heart Disease Prediction**  
Uses features like **age, cholesterol, blood pressure, chest pain type** to predict heart disease.  

### **3️⃣ Parkinson’s Disease Prediction**  
Uses this model analyzes vocal and movement-related parameters **to detect Parkinson's disease early**, helping in timely diagnosis and management. 🚀🔬.  

---

## 🖼️ Screenshots  
### 🟠 **Diabetes Prediction**
![Screenshot 2025-02-04 154637](https://github.com/user-attachments/assets/0ca00345-135b-4a53-9fdb-ec01370e5aed)


### ❤️ **Heart Disease Prediction**
![Screenshot 2025-02-04 154822](https://github.com/user-attachments/assets/e9bd696e-5e96-42b6-98d7-5a7c114c466a)


### 🟢 **Parkinson’s Disease Prediction**
![Screenshot 2025-02-04 154920](https://github.com/user-attachments/assets/4a7fc94f-fdfe-4613-b95d-8402199c86f2)


---

### **How It Works**  

1. **User Input:**  
   - The user selects a disease from the sidebar (Diabetes, Heart Disease, or Parkinson’s).  
   - The system provides an interactive form where users input health parameters like blood pressure, glucose level, cholesterol, etc.  

2. **Data Preprocessing:**  
   - Input values are converted into a structured format.  
   - Categorical variables (like gender, chest pain type, etc.) are encoded into numerical values.  
   - If required, data is standardized using a pre-trained **scaler** (for models that need normalized input).  

3. **Model Prediction:**  
   - The corresponding **machine learning model** (pre-trained and saved as `.sav` files) is loaded.  
   - The model takes the input data and predicts whether the person has the disease or not (binary classification: 0 = Negative, 1 = Positive).  

4. **Display of Results:**  
   - If the person is predicted to be **positive**, a success message with a ✅ symbol is shown.  
   - If negative, a ❌ message is displayed.  
   - Results are shown with an intuitive and user-friendly interface.   

### **Models Used**  
- **Diabetes Prediction:** Uses a trained **SVM (Support Vector Machine) model**.  
- **Heart Disease Prediction:** Uses a **Logistic Regression or Decision Tree model** trained on heart disease datasets.  
- **Parkinson’s Disease Prediction:** Uses **SVM with a linear kernel**, trained on vocal features to detect Parkinson’s.  

### **Future Enhancements**  
- Adding more diseases for prediction (e.g., Cancer, Stroke).  
- Implementing a feature to upload medical reports for automatic analysis.  
- Enhancing visualization with risk factor comparison charts.  
- Deploying the system online using cloud services like AWS, GCP, or Streamlit Sharing.
- The system can display graphs showing risk factors and trends based on input data.

This system provides an **easy-to-use** and **efficient** tool for early disease prediction, aiding users and medical professionals in making informed decisions. 🚀💡

---
