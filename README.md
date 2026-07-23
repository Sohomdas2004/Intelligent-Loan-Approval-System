# 🏦 Intelligent Loan Approval System

An end-to-end Machine Learning application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant financial and personal information.

The project demonstrates the complete machine learning workflow — from data preprocessing and model training to deploying the trained model through an interactive Streamlit web application.

---

## 📌 Project Overview

Loan approval is an important decision-making process in the financial sector. Traditionally, loan applications are evaluated manually, which can be time-consuming and inconsistent.

This project uses **Machine Learning classification techniques** to analyze applicant information and generate a loan approval prediction.

The application accepts applicant details such as:

* Applicant income
* Co-applicant income
* Loan amount
* Loan term
* Credit history
* Education
* Employment information
* Marital status
* Property area
* Other applicant-related details

Based on these inputs, the trained Machine Learning model predicts whether the loan application is likely to be approved or rejected.

> ⚠️ This project is intended for educational and demonstration purposes. It should not be used as the sole basis for real-world financial or lending decisions.

---

## 🎯 Project Objectives

* Build a Machine Learning model for loan approval prediction.
* Perform data preprocessing and feature transformation.
* Train and evaluate a classification model.
* Save the trained model for future predictions.
* Develop an interactive web application using Streamlit.
* Deploy the Machine Learning model as a user-friendly application.

---

## 🧠 Machine Learning Workflow

```text
Raw Dataset
     │
     ▼
Data Loading
     │
     ▼
Data Cleaning & Preprocessing
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Feature Engineering
     │
     ▼
Model Training
     │
     ▼
Model Evaluation
     │
     ▼
Model Serialization
     │
     ▼
Streamlit Application
     │
     ▼
Loan Approval Prediction
```

---

## 🏗️ Project Architecture

```text
User Input
    │
    ▼
Streamlit Web Application
    │
    ▼
Input Validation & Preprocessing
    │
    ▼
Saved Machine Learning Model
    │
    ▼
Prediction
    │
    ▼
Loan Approved / Loan Rejected
```

---

## 📂 Project Structure

```text
Intelligent-Loan-Approval-System/
│
├── App/
│   └── app.py
│       └── Streamlit application
│
├── Data/
│   └── Dataset files
│       └── Dataset used for training and analysis
│
├── Model/
│   └── loan_approval_model.pkl
│       └── Serialized trained Machine Learning model
│
├── Notebook/
│   └── Machine Learning notebook
│       ├── Data exploration
│       ├── Data preprocessing
│       ├── Feature engineering
│       ├── Model training
│       └── Model evaluation
│
├── requirements.txt
│
└── README.md
```

---

## 🛠️ Technologies Used

### Programming Language

* **Python**

### Machine Learning

* **Scikit-learn**
* Classification algorithms
* Model evaluation techniques

### Data Processing

* **Pandas**
* **NumPy**

### Data Visualization

* **Matplotlib**
* **Seaborn**

### Model Deployment

* **Streamlit**

### Model Serialization

* **Joblib**

---

## 🔄 Application Workflow

### 1. User Enters Applicant Information

The user provides relevant information about the loan applicant through the Streamlit interface.

### 2. Input Preprocessing

The application converts the input into the format expected by the trained model.

The same preprocessing logic used during model training must be maintained during prediction to ensure consistent results.

### 3. Model Loading

The trained Machine Learning model is loaded from the `Model` directory.

```python
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)
```

### 4. Prediction

The model analyzes the applicant's features and generates a prediction.

### 5. Result Display

The application displays the final prediction:

```text
Loan Approved
```

or

```text
Loan Rejected
```

---

## 🚀 How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Sohomdas2004/Intelligent-Loan-Approval-System.git
```

```bash
cd Intelligent-Loan-Approval-System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application

```bash
streamlit run App/app.py
```

The application will then open in your browser.

---

## 📊 Machine Learning Features

The model uses applicant-related features to determine the probability of loan approval.

Typical features include:

| Feature            | Description                |
| ------------------ | -------------------------- |
| Gender             | Applicant gender           |
| Married            | Marital status             |
| Dependents         | Number of dependents       |
| Education          | Education level            |
| Self Employed      | Employment status          |
| Applicant Income   | Applicant's income         |
| Coapplicant Income | Co-applicant's income      |
| Loan Amount        | Requested loan amount      |
| Loan Term          | Duration of the loan       |
| Credit History     | Applicant's credit history |
| Property Area      | Location category          |

---

## 💾 Model Serialization

After training, the Machine Learning model is saved as a `.pkl` file.

```text
Model/
└── loan_approval_model.pkl
```

This allows the application to load the trained model without retraining it every time the application starts.

This separation between **model training** and **model inference** makes the application more efficient and suitable for deployment.

---

## 🧪 Model Development Process

The project follows a standard Machine Learning pipeline:

1. Load the dataset.
2. Explore the dataset.
3. Identify missing values.
4. Clean and preprocess the data.
5. Convert categorical data into numerical form.
6. Prepare features and target variables.
7. Split the dataset into training and testing data.
8. Train the classification model.
9. Evaluate the model.
10. Save the trained model.
11. Load the model inside the Streamlit application.
12. Generate predictions from user input.

---

## 💡 Key Learning Outcomes

Through this project, the following concepts were implemented:

* Data preprocessing
* Handling categorical features
* Feature engineering
* Supervised Machine Learning
* Classification
* Model evaluation
* Model serialization using Pickle
* File path management using `pathlib`
* Streamlit application development
* Machine Learning model deployment

---



## 👨‍💻 Author

**Sohom Das**

Computer Science / Information Technology Student

Interested in:

* Machine Learning
* Data Science
* Python Development
* Software Development

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is intended for educational and learning purposes.

