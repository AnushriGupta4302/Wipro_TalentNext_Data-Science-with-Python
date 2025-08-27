'''
Ques-1)
Perform Exploratory Data Analysis for the dataset Mall Customers. 
The dataset can be downloaded from https://www.kaggle.com/datasets give code using matplotlib
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Mall_Customers.csv")
print("Shape:", df.shape)
print(df.head())
print(df.info())
print(df.describe())

gender_counts = df["Gender"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Gender Distribution")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=15, color="skyblue", edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age Distribution of Customers")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["Annual Income (k$)"], bins=15, color="lightgreen", edgecolor="black")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Count")
plt.title("Annual Income Distribution")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["Spending Score (1-100)"], bins=15, color="salmon", edgecolor="black")
plt.xlabel("Spending Score")
plt.ylabel("Count")
plt.title("Spending Score Distribution")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df["Age"], df["Spending Score (1-100)"], color="purple", alpha=0.6)
plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.title("Age vs Spending Score")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df["Annual Income (k$)"], df["Spending Score (1-100)"], color="orange", alpha=0.6)
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.title("Annual Income vs Spending Score")
plt.show()

plt.figure(figsize=(8,5))
df.boxplot(column="Annual Income (k$)", by="Gender")
plt.title("Annual Income by Gender")
plt.suptitle("")
plt.show()

plt.figure(figsize=(8,5))
df.boxplot(column="Spending Score (1-100)", by="Gender")
plt.title("Spending Score by Gender")
plt.suptitle("")
plt.show()



'''
Ques-2)
Perform Exploratory Data Analysis for the dataset salary_data. 
The dataset can be downloaded from https://www.kaggle.com/datasets give code using matplotlib
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_Data.csv")   # make sure file is in your working directory
print("Shape:", df.shape)
print(df.head())
print(df.info())
print(df.describe())

plt.figure(figsize=(8,5))
plt.hist(df["YearsExperience"], bins=10, color="skyblue", edgecolor="black")
plt.xlabel("Years of Experience")
plt.ylabel("Count")
plt.title("Distribution of Years of Experience")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["Salary"], bins=10, color="lightgreen", edgecolor="black")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.title("Distribution of Salaries")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df["YearsExperience"], df["Salary"], color="orange", alpha=0.7)
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Years of Experience vs Salary")
plt.show()

plt.figure(figsize=(8,5))
plt.boxplot(df["YearsExperience"], vert=False, patch_artist=True)
plt.title("Boxplot of Years of Experience")
plt.show()

plt.figure(figsize=(8,5))
plt.boxplot(df["Salary"], vert=False, patch_artist=True)
plt.title("Boxplot of Salary")
plt.show()


'''
Ques-3)
Perform Exploratory Data Analysis for the dataset Social Network Ads. 
The dataset can be downloaded from https://www.kaggle.com/datasets
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Social_Network_Ads.csv")  
print("Shape:", df.shape)
print(df.head())
print(df.info())
print(df.describe(include="all"))

if "User ID" in df.columns:
    df = df.drop(columns=["User ID"])
gender_counts = df["Gender"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Gender Distribution")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=10, color="skyblue", edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age Distribution")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["EstimatedSalary"], bins=10, color="lightgreen", edgecolor="black")
plt.xlabel("Estimated Salary")
plt.ylabel("Count")
plt.title("Estimated Salary Distribution")
plt.show()

purchase_counts = df["Purchased"].value_counts()

plt.figure(figsize=(6,6))
plt.bar(purchase_counts.index.astype(str), purchase_counts.values, color=["red","green"])
plt.xlabel("Purchased (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.title("Purchase Distribution")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df["Age"], df["Purchased"], color="purple", alpha=0.6)
plt.xlabel("Age")
plt.ylabel("Purchased (0/1)")
plt.title("Age vs Purchased")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df["EstimatedSalary"], df["Purchased"], color="orange", alpha=0.6)
plt.xlabel("Estimated Salary")
plt.ylabel("Purchased (0/1)")
plt.title("Estimated Salary vs Purchased")
plt.show()

colors = df["Purchased"].map({0:"blue", 1:"red"})

plt.figure(figsize=(8,6))
plt.scatter(df["Age"], df["EstimatedSalary"], c=colors, alpha=0.7)
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.title("Age vs Salary (Red = Purchased, Blue = Not Purchased)")
plt.show()