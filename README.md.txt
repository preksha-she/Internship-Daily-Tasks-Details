## 📌 Project Overview

This repository documents my structured learning journey during a **Data Science & Artificial Intelligence Internship**.

The internship was designed to build strong foundational knowledge in:

- Python programming  
- Data structures  
- File handling  
- Data cleaning  
- Data visualization  
- Exploratory Data Analysis (EDA)  
- Feature engineering  
- Statistics and probability  
- Statistics: Distributions
– SQL for Data Science
-Git Advanced
- Mini Project 1: Exploratory Data Analysis (EDA)
-Introduction to Machine Learning
-Review I & Problem Statement Selection
 -Brainstorming & Project Deep Dive
-Multivariate Linear Regression 
-Logistic Regression 
-Decision Tree (ID3 Algorithm)
- Support Vector Machines (SVM)



The learning progressed step-by-step from programming fundamentals to machine learning preparation.

---

# 📅 Learning Breakdown

## 📍 Day 1 – Development Environment Setup

- Python installation and verification  
- VS Code configuration  
- GitHub repository setup  
- Execution of first Python program  

---

## 📍 Day 2 – Python Fundamentals

- Variables and data types (`int`, `float`, `str`, `bool`)  
- Type conversion  
- User input handling  
- Conditional statements  
- Arithmetic operations  

---

## 📍 Day 3 – Lists and Tuples

- Data storage using lists and tuples  
- Indexing and slicing  
- List methods  
- Understanding mutability and immutability  

---

## 📍 Day 4 – Dictionaries and Sets

- Key-value data structures  
- Dictionary operations  
- Set operations  
- Duplicate removal using sets  

---

## 📍 Day 5 – Functions and Modules

- Function definition and usage  
- Parameters and return values  
- Variable scope  
- Creating and importing custom modules  

---

## 📍 Day 6 – File Handling and Exception Handling

- Reading and writing files  
- Using `with open()` for safe file management  
- Working with CSV files  
- Implementing `try-except` blocks  

---

## 📍 Day 7 – Structured File Processing

- Handling `.txt`, `.csv`, and `.xlsx` files  
- Managing structured data  
- Persistent data storage  

---

## 📍 Day 8 – NumPy Fundamentals

- Array creation and manipulation  
- Broadcasting  
- Vectorized operations  
- Reshaping and transpose  
- Basic statistical functions  

---

## 📍 Day 9 – Pandas Series

- Series creation and indexing  
- Data filtering using boolean masking  
- Handling missing values  
- Vectorized string operations  

---

## 📍 Day 10 – Data Cleaning

- Identifying and handling missing values  
- Removing duplicate records  
- Data type conversion  
- String standardization  
- Dataset validation  

---

## 📍 Day 11 – Data Visualization

- Line plots  
- Scatter plots  
- Bar charts  
- Customizing plots  
- Working with subplots  

---

## 📍 Day 12 – Visualization Dashboard

- Correlation analysis  
- Comparative bar charts  
- Multi-plot dashboards  
- Structured data presentation  

---

## 📍 Day 13 – Exploratory Data Analysis (EDA)

- Univariate analysis  
- Bivariate analysis  
- Correlation interpretation  
- Outlier detection  
- Insight extraction  

---

## 📍 Day 14 – Feature Engineering

- Label Encoding  
- One-Hot Encoding  
- Feature Scaling (Standardization & Normalization)  
- Polynomial features  
- Impact on model performance  

---

## 📍 Day 15 – Statistics: Probability

- Introduction to probability concepts  
- Sample space and events  
- Addition and multiplication rules  
- Independent and dependent events  
- Conditional probability  
- Conceptual understanding of Bayes’ Theorem  

This strengthened statistical thinking required for machine learning and predictive modeling.

---

📍 Day 16 – Statistics: Distributions

Explored the shape of data and its impact on analysis and ML model selection.

Practiced identifying skewness and detecting outliers using Z-scores.

Simulated the Central Limit Theorem, observing how sample means form a bell curve even from messy, skewed data.

Understood how these concepts help in statistical inference and improve data-driven decision-making.
---


📍  Day 17 – SQL Fundamentals (SELECT, WHERE, GROUP BY, JOIN, Python Integration)

## 🎯 Objective
Set up your first local SQLite database and learn how to:
- Retrieve specific data using `SELECT`
- Filter records using `WHERE`
- Aggregate results using `GROUP BY`
- Combine tables using `JOIN`
- Connect SQL with Python for analysis

---

📍 Day 19 - Git Advanced – Branching & Merge Conflict Resolution

- Develop new features  
- Fix bugs  
- Experiment with ideas  
- Refactor code

📍 Day 20 – Mini Project 1: Exploratory Data Analysis (EDA)

- Examine and understand raw datasets
- Perform justified data cleaning and preprocessing
- Explore patterns through statistical summaries and visualization
- Communicate findings clearly and professionally

📍Day 21 – Introduction to Machine Learning

Clearly explain Machine Learning  
✔ Differentiate ML from traditional programming  
✔ Identify supervised vs unsupervised vs reinforcement learning  
✔ Map real-world problems to the correct ML category  
✔ Avoid beginner-level conceptual mistakes

 📍Day 22 – Review I & Problem Statement Selection

Clearly understand which ML tools apply to which problems  
✔ Select a project aligned with their skill level  
✔ Define a clear problem statement  
✔ Transition confidently into independent project work

---

📍Days 23–25,26 – Brainstorming & Project Deep Dive

Finalized a well-scoped project idea  
✔ Defined measurable success criteria  
✔ Identified appropriate modeling approaches  
✔ Designed a preliminary data flow architecture  
✔ Aligned project ambition with realistic constraints  

📍Days 27 -Multivariate Linear Regression – Salary Prediction

This project focuses on building a multivariate (multiple) linear regression model using the hiring.csv dataset to predict candidate salaries based on three key factors: years of experience, written test score, and interview score. The objective was to develop a machine learning solution that can assist the HR department in making data-driven salary decisions for future candidates. The dataset was loaded and analyzed to understand how each feature contributes to salary prediction, followed by basic preprocessing to ensure data quality. A multiple linear regression model was then trained using all three input variables together, and predictions were generated for new candidates to simulate real-world HR decision-making. Through this project, I gained a deeper understanding of how multiple independent variables collectively influence a dependent variable and learned how regression models can be applied in practical business scenarios. This task improved my skills in data analysis, model building, and interpreting prediction results using Python, Pandas, NumPy, and Scikit-learn.

📍Days 28 -Logistic Regression Projects

This repository contains multiple examples demonstrating the implementation of **Logistic Regression using Python and Scikit-learn** for different classification problems.

The first project uses the **Iris dataset** to classify different species of flowers. The dataset is loaded using Scikit-learn and converted into a pandas DataFrame for easier analysis. The features and target variable are separated, and the data is split into training and testing sets using `train_test_split`. A Logistic Regression model is trained and used to predict the flower species. The performance of the model is evaluated using **accuracy score and classification report**.

The second project focuses on **insurance purchase prediction based on age**. The dataset is loaded using pandas and visualized using **matplotlib** to understand the relationship between age and whether a person buys insurance. The dataset is split into training and testing sets, and a Logistic Regression model is trained to predict the result. The probability of buying insurance is calculated using `predict_proba`, and the **sigmoid curve** is used to show how logistic regression models probabilities. The model performance is evaluated using **accuracy score**.

The third project is **Employee Retention Prediction** using an HR dataset. The dataset includes features such as satisfaction level, number of projects, monthly working hours, promotion in the last five years, department, and salary level. **Exploratory Data Analysis (EDA)** is performed using visualizations like bar charts and boxplots to understand patterns related to employee turnover. After preprocessing the data and converting categorical variables into numerical form, a Logistic Regression model is trained using scikit-learn. The dataset is divided into training and testing sets, and the model predicts whether an employee will **stay in the company or leave**, helping demonstrate how machine learning can assist in employee retention analysis.

📍Days 29-# Decision Tree (ID3 Algorithm)

In this task, I learned the fundamentals of the Decision Tree algorithm using the ID3 method. I created a dataset with features such as outlook, temperature, humidity, and wind to predict whether football can be played. The data was processed using Python libraries like pandas and scikit-learn. Categorical values were converted into numerical format using LabelEncoder so that the model could understand the data. After preparing the dataset, I trained a DecisionTreeClassifier model using the entropy criterion and tested it with sample input. Through this work, I understood how the Decision Tree algorithm classifies data based on conditions and how the ID3 algorithm uses entropy to make decisions. I also learned how to preprocess data, train a machine learning model, and make predictions.

📍Days 32 - Support Vector Machines (SVM)

## Overview
Today I learned about **Support Vector Machines (SVM)**, a supervised machine learning algorithm used for **classification and regression**. SVM works by finding the best **decision boundary (hyperplane)** that separates different classes in a dataset.

## Key Concepts
- **Hyperplane:** Decision boundary that separates classes.
- **Support Vectors:** Data points closest to the hyperplane.
- **Margin:** Distance between the hyperplane and the nearest data points.
- **Kernel Trick:** Helps SVM handle non-linear data.

## Conclusion
SVM is a powerful algorithm that works well for **high-dimensional data** and provides strong classification performance.

---
📅 *Machine Learning Journey – Day 32*

# 🛠 Technologies Used

- Python  
- NumPy  
- Pandas  
- Matplotlib  
- CSV & Excel handling  

---

# 🎯 Skills Developed

- Strong Python programming foundation  
- Data structure management  
- Data cleaning and preprocessing  
- Data visualization and dashboard creation  
- Exploratory data analysis  
- Feature engineering techniques  
- Statistical reasoning and probability fundamentals  
- Machine learning data preparation  

---

# 🏆 Internship Outcome

This internship provided a structured progression from programming basics to core data science concepts.

It strengthened analytical thinking, problem-solving ability, and readiness for real-world machine learning workflows.

- Structuring and executing data analysis projects independently  
- Cleaning and preprocessing real-world datasets  
- Selecting suitable machine learning frameworks (Supervised, Unsupervised, etc.)  
- Handling collaboration challenges such as branching and merge conflicts  
- Translating technical insights into clear, professional communication 

---

## 👩‍💻 Author

**Preksha Shetty**  

📅 February 2026
