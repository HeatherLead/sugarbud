import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

file_path = "model/labelDataset.xlsx"

df = pd.read_excel(file_path)

df = df.drop_duplicates()
df = df.dropna(thresh=len(df.columns) * 0.8) 
df.fillna(df.select_dtypes(include=['number']).mean(), inplace=True)

target_col = "Disease"
X = df.drop(columns=[target_col])  
y = df[target_col]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42 , class_weight="balanced")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred , zero_division=0))

df.to_excel("model/cleaned_labeled_dataset.xlsx", index=False)
print("Cleaned dataset saved as cleaned_labeled_dataset.xlsx")
