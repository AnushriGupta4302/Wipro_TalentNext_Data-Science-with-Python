'''
Use Case: Perform the Outlier detection for the given dataset i.e. datasetExample
Dataset: datasetExample.csv
Perform the following task
Load the data in the DataFrame.
Detection of Outliers
'''
import pandas as pd
df = pd.read_csv("datasetExample.csv")  # ensure file is in the same folder
print("First 5 rows:")
print(df.head())
def detect_outliers_iqr(data):
    outliers = {}
    for col in data.select_dtypes(include='number').columns:  # only numeric columns
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outlier_rows = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
        if not outlier_rows.empty:
            outliers[col] = outlier_rows
    return outliers
outliers_found = detect_outliers_iqr(df)
for col, rows in outliers_found.items():
    print(f"\nOutliers in column '{col}':")
    print(rows)