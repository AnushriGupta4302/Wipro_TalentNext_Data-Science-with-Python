'''
Ques-1)
Perform Data Preprocessing on melb_data.csv dataset with statistical perspective. 
The dataset can be downloaded from https://www.kaggle.com/datasets/gunjanpathak/melb-data?resource=download
'''

import pandas as pd
import numpy as np

df = pd.read_csv("melb_data.csv")
print("\n--- Basic Info ---")
print(df.info())
print("\n--- Missing Values (in %) ---")
print((df.isnull().sum() / len(df) * 100).sort_values(ascending=False))
print("\n--- Descriptive Statistics ---")
print(df.describe(include="all").T)
print("\n--- Skewness of Numerical Features ---")
print(df.skew(numeric_only=True))

if "Price" in df.columns:
    print("\n--- Correlation with Price ---")
    print(df.corr(numeric_only=True)['Price'].sort_values(ascending=False))

numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

categorical_cols = df.select_dtypes(exclude=[np.number]).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
df_scaled = df_encoded.copy()
for col in numeric_cols:
    mean = df_scaled[col].mean()
    std = df_scaled[col].std()
    if std != 0:
        df_scaled[col] = (df_scaled[col] - mean) / std

print("\nFinal dataset shape after preprocessing:", df_scaled.shape)
print(df_scaled.head())