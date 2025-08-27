'''
Ques-1)
Use Case: Sales Prediction
Create a model which will predict the sales based on campaigning expenses.
Dataset: Advertising.csv
The dataset can be downloaded from https://www.kaggle.com/datasets
Perform the following task.
Load the data in the DataFrame.
Perform Data Preprocessing
Handle Categorical Data
Perform Exploratory Data Analysis
Build the model using Multiple Linear Regression
Use the appropriate evaluation metrics
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("Advertising.csv")
print("Shape:", df.shape)
print(df.head())

if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

print("\nMissing values:\n", df.isnull().sum())

print("\nStatistical Summary:\n", df.describe())

sns.pairplot(df, x_vars=['TV','Radio','Newspaper'], y_vars='Sales', height=4, aspect=1, kind='scatter')
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Coefficients:")
print("Intercept:", model.intercept_)
coef_df = pd.DataFrame(model.coef_, X.columns, columns=["Coefficient"])
print(coef_df)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n--- Evaluation Metrics ---")
print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)
print("R² Score:", r2)

plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, color="blue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()


'''
Ques-2)
Use Case: Diabetes Prediction
Consider the PIMA Indians diabetes dataset. Create a Model for diabetes prediction based on the features mentioned in the dataset.
Dataset: PIMA Indians diabetes dataset.
The dataset can be downloaded from https://www.kaggle.com/datasets
Perform the following tasks.
Load the data in the DataFrame
Perform Data Preprocessing
Perform Exploratory Data Analysis
Build the model using Logistic Regression and K-Nearest Neighbour
Use the appropriate evaluation metrics
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("diabetes.csv")
print("Shape of dataset:", df.shape)
print(df.head())
print("\nMissing values:\n", df.isnull().sum())

cols_with_zero_invalid = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
for col in cols_with_zero_invalid:
    df[col].replace(0, np.nan, inplace=True)

df.fillna(df.median(), inplace=True)

print("\nStatistical Summary:\n", df.describe())

plt.figure(figsize=(6,4))
sns.countplot(x="Outcome", data=df, palette="coolwarm")
plt.title("Diabetes Outcome Distribution")
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

df.hist(bins=20, figsize=(12,8))
plt.suptitle("Feature Distributions", y=1.02)
plt.show()

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y)

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred_log))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_log))
print("Classification Report:\n", classification_report(y_test, y_pred_log))

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_knn))
print("Classification Report:\n", classification_report(y_test, y_pred_knn))

plt.bar(["Logistic Regression", "KNN"], 
        [accuracy_score(y_test, y_pred_log), accuracy_score(y_test, y_pred_knn)], 
        color=["blue","green"])
plt.ylabel("Accuracy")
plt.title("Model Comparison")
plt.show()
