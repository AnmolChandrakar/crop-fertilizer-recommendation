# train_model.py
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
dataset = pd.read_csv("Crop_recommendation.csv")

# Features & Labels
features = dataset.iloc[:, 0:7].values
labels = dataset.iloc[:, 7].values

# Train-Validation-Test split
x_rem, x_test, y_rem, y_test = train_test_split(features, labels, test_size=0.1, random_state=10)
x_train, x_val, y_train, y_val = train_test_split(x_rem, y_rem, test_size=0.1111, random_state=10)

# Feature Scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_val = scaler.transform(x_val)
x_test = scaler.transform(x_test)

# Train Model
model = svm.SVC(probability=True)
model.fit(x_train, y_train)

# Evaluation
print("Validation Report:")
print(classification_report(y_val, model.predict(x_val)))
print("Test Report:")
print(classification_report(y_test, model.predict(x_test)))

# Save model & scaler
pickle.dump(model, open('crop_model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

print("Model and scaler saved successfully.")
