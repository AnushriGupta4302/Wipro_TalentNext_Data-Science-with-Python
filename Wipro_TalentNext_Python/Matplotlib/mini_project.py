'''
Ques :
Use Case: Diabetes Prediction
Perform Exploratory Data Analysis for the Diabetes Dataset.
Dataset: Diabetes.csv
The dataset can be downloaded from https://www.kaggle.com/datasets
Perform the following tasks
1. Load the data in the DataFrame
2. Data Pre-processing
3. Handle the Categorical Data
4. Perform Uni-variate Analysis
5. Perform Bi-variate Analysis
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Diabetes.csv")   
print("Shape of dataset:", df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())

cols_with_zero_invalid = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
for col in cols_with_zero_invalid:
    df[col] = df[col].replace(0, np.nan)

df.fillna(df.median(), inplace=True)

print("\nOutcome Value Counts:")
print(df["Outcome"].value_counts())

df.hist(figsize=(12,10), bins=15, color="skyblue", edgecolor="black")
plt.suptitle("Univariate Analysis - Histograms", fontsize=16)
plt.show()

outcome_counts = df["Outcome"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(outcome_counts, labels=["No Diabetes (0)", "Diabetes (1)"], autopct='%1.1f%%',
        colors=["lightgreen","salmon"], startangle=90)
plt.title("Diabetes Outcome Distribution")
plt.show()

colors = df["Outcome"].map({0:"blue", 1:"red"})
plt.figure(figsize=(8,6))
plt.scatter(df["Glucose"], df["BMI"], c=colors, alpha=0.6)
plt.xlabel("Glucose")
plt.ylabel("BMI")
plt.title("Glucose vs BMI (Red = Diabetes, Blue = No Diabetes)")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df["Age"], df["Glucose"], c=colors, alpha=0.6)
plt.xlabel("Age")
plt.ylabel("Glucose")
plt.title("Age vs Glucose (Red = Diabetes, Blue = No Diabetes)")
plt.show()

plt.figure(figsize=(8,6))
df.boxplot(column="Insulin", by="Outcome")
plt.title("Insulin Levels by Outcome")
plt.suptitle("")
plt.show()

plt.figure(figsize=(8,6))
df.boxplot(column="BMI", by="Outcome")
plt.title("BMI by Outcome")
plt.suptitle("")
plt.show()