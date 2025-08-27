'''
Ques-1)
Use-Case: House Price Prediction
Dataset melb_data.csv
The dataset can be downloaded melb data.csv Kaggle
Perform the following tasks:
1. Load the data in dataframe (Pandas)
2. Handle inappropriate data
3. Handle the missing data
4. Handle the categorical data
'''

import pandas as pd
import numpy as np
df = pd.read_csv("melb_data.csv")
print("Initial Shape:", df.shape)
print(df.head())
df = df.drop_duplicates()

cols_to_drop = ['Address', 'SellerG', 'Date']  
df = df.drop(columns=[c for c in cols_to_drop if c in df.columns], errors='ignore')

print("Shape after dropping irrelevant columns:", df.shape)

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])
print("\nMissing values after imputation:\n", df.isnull().sum().sum())

df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

print("\nShape after encoding:", df_encoded.shape)
print(df_encoded.head())

X = df_encoded.drop("Price", axis=1)   
y = df_encoded["Price"]                

print("\nFinal X shape:", X.shape)
print("Final y shape:", y.shape)