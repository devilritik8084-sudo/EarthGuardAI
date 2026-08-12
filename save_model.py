import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("../data/weather_data.csv")

# Features
X = data[["Temperature", "Rainfall", "WindSpeed"]]

# Target
y = data["Risk Level"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save trained model
with open("../models/disaster_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")