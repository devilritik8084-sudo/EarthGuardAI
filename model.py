import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ==============================
# 🌍 EarthGuardAI - AI Model
# ==============================

print("=" * 55)
print("🌍 EarthGuardAI")
print("AI Disaster Prediction Model")
print("=" * 55)

# Project path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "weather_data.csv")

# Check dataset
if not os.path.exists(DATA_FILE):
    print("\n❌ Dataset not found!")
    print("Expected file:")
    print(DATA_FILE)
    raise SystemExit

# Load dataset
df = pd.read_csv(DATA_FILE)

print("\n✅ Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", list(df.columns))

# Required columns
required = ["temperature", "rainfall", "wind_speed", "risk"]

for column in required:
    if column not in df.columns:
        print(f"\n❌ Missing column: {column}")
        print("Required columns:")
        print(required)
        raise SystemExit

# Input and target
X = df[["temperature", "rainfall", "wind_speed"]]
y = df["risk"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create AI model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("\n🤖 AI Model trained successfully!")
print(f"📊 Model Accuracy: {accuracy * 100:.2f}%")

# ==============================
# User Prediction
# ==============================

print("\n" + "=" * 55)
print("🌦️ ENTER CURRENT WEATHER DATA")
print("=" * 55)

try:
    temperature = float(input("Enter Temperature (°C): "))
    rainfall = float(input("Enter Rainfall (mm): "))
    wind_speed = float(input("Enter Wind Speed (km/h): "))

except ValueError:
    print("\n❌ Please enter numbers only.")
    raise SystemExit

# Prediction
user_data = pd.DataFrame(
    [[temperature, rainfall, wind_speed]],
    columns=["temperature", "rainfall", "wind_speed"]
)

result = model.predict(user_data)[0]

print("\n" + "=" * 55)
print("🚨 EARTHGUARDAI PREDICTION")
print("=" * 55)

print("🌡️ Temperature:", temperature, "°C")
print("🌧️ Rainfall:", rainfall, "mm")
print("💨 Wind Speed:", wind_speed, "km/h")
print("\n🤖 AI Disaster Risk:", result)

if str(result).lower() == "high":
    print("🚨 WARNING: High disaster risk detected!")
elif str(result).lower() == "medium":
    print("⚠️ CAUTION: Medium disaster risk detected.")
else:
    print("✅ LOW RISK: No major risk detected.")

print("\n" + "=" * 55)
print("EarthGuardAI analysis completed.")
print("=" * 55)