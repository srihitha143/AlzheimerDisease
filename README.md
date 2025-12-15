# 🔬 Alzheimer’s Disease Risk Prediction

## 📌 Project Overview

This project provides a machine learning-based clinical assistance tool for the early screening of Alzheimer’s Disease. By analyzing a comprehensive set of patient data—including medical history, cognitive assessments (MMSE), and lifestyle factors—the system estimates the likelihood of Alzheimer's with high precision.

The goal is to support healthcare providers with data-driven insights to slow disease progression and improve patient quality of life through early intervention.

-----

## 🚀 Key Features

  * **Comprehensive Risk Assessment:** Evaluates medical history, behavioral symptoms (e.g., confusion, disorientation), and lifestyle indicators (e.g., sleep quality, BMI).
  * **Clinical-Grade AI:** Utilizes a fine-tuned XGBoost model for binary classification (High Risk vs. Low Risk).
  * **Interactive Streamlit Dashboard:** A user-friendly interface designed for medical professionals and researchers to input patient data and receive immediate risk probabilities.
  * **Interpretive Results:** Categorizes risk into levels (Very High, High, Mild, Low) with tailored clinical advice for each.

-----

## 📊 Dataset & Features

The model is trained on `alzheimers_disease_data.csv`, focusing on features that correlate most strongly with cognitive decline:

| Category | Key Features Included |
| :--- | :--- |
| **Demographic** | Age, Gender, Ethnicity, BMI |
| **Clinical Measures** | MMSE (Mini-Mental State Exam), Functional Assessment, ADL (Activities of Daily Living) |
| **Medical History** | Family History, Hypertension, Diabetes, Depression, Head Injury |
| **Behavioral** | Memory Complaints, Confusion, Disorientation, Personality Changes |
| **Lifestyle** | Smoking, Alcohol Consumption, Sleep Quality |

-----

## 🛠️ Machine Learning Pipeline

1.  **Exploratory Data Analysis (EDA):** Performed in `alzheimerdisease.py` to identify key indicators and clean clinical data.
2.  **Preprocessing:** Includes handling missing values and scaling numerical features using `StandardScaler`.
3.  **Model Selection:** XGBoost was chosen for its superior performance in handling tabular clinical data.
4.  **Serialization:** The final model (`best_model.pkl`) and feature scaler (`scaler.pkl`) are integrated directly into the web application.

-----

## ⚙️ Installation & Usage

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/alzheimers-risk-prediction.git
    cd alzheimers-risk-prediction
    ```

2.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application:**

    ```bash
    streamlit run app.py
    ```

-----

## 📂 Repository Structure

  * `app.py`: The Streamlit web application script with custom UI/UX.
  * `alzheimerdisease.py`: Core logic for data analysis and model training.
  * `best_model.pkl`: The trained XGBoost classifier.
  * `scaler.pkl`: The StandardScaler object for data normalization.
  * `selected_features.json`: A mapping of features used during the prediction phase.
  * `Alzheimer's Disease Classification.pptx`: Presentation detailing project goals and methodology.

    project done by : Nakka Srihitha
