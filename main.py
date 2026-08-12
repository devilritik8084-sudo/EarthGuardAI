import os
import pandas as pd
import joblib

# Project path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_FILE = os.path.join(BASE_DIR, "models", "disaster_model.pkl")


# Load AI Model
try:
    model = joblib.load(MODEL_FILE)
    print("✅ AI Model Loaded Successfully!")
except Exception as e:
    print("❌ Model Loading Error:", e)
    exit()


print("=" * 55)
print("🌍 EARTHGUARDAI")
print("AI Disaster Prediction & Emergency Alert System")
print("=" * 55)


def check_risk():

    print("\n" + "=" * 55)
    print("🌦️ DISASTER RISK PREDICTION")
    print("=" * 55)

    try:
        temperature = float(input("Enter Temperature (°C): "))
        rainfall = float(input("Enter Rainfall (mm): "))
        wind_speed = float(input("Enter Wind Speed (km/h): "))

    except ValueError:
        print("❌ Please enter numbers only.")
        return


    # Input for AI model
    data = pd.DataFrame({
        "Temperature": [temperature],
        "Rainfall": [rainfall],
        "WindSpeed": [wind_speed]
    })


    # AI Prediction
    prediction = model.predict(data)


    risk = prediction[0]


    print("\n" + "-" * 55)
    print("🤖 EARTHGUARDAI RESULT")
    print("-" * 55)

    print(f"🌡️ Temperature : {temperature} °C")
    print(f"🌧️ Rainfall    : {rainfall} mm")
    print(f"💨 Wind Speed  : {wind_speed} km/h")

    print("\n🚨 Disaster Risk:", risk)


    if risk == "High" or risk == "HIGH":
        print("⚠️ WARNING: High disaster risk detected!")

    elif risk == "Medium" or risk == "MEDIUM":
        print("⚠️ CAUTION: Moderate disaster risk detected.")

    else:
        print("✅ LOW RISK: Conditions are safer.")


    print("-" * 55)



def model_information():

    print("\n" + "=" * 55)
    print("🤖 AI MODEL INFORMATION")
    print("=" * 55)

    print("Model      : Decision Tree Classifier")
    print("Input      : Temperature")
    print("             Rainfall")
    print("             Wind Speed")
    print("Output     : Disaster Risk Level")
    print("Technology : Python + Pandas + Scikit-learn")

    print("=" * 55)



def about_project():

    print("\n" + "=" * 55)
    print("🌍 ABOUT EARTHGUARDAI")
    print("=" * 55)

    print("Project Name : EarthGuardAI")
    print("Version      : 1.0")
    print("Developer    : Ritik Kumar")

    print("\nPurpose:")
    print("AI system to analyze weather conditions")
    print("and predict possible disaster risk.")

    print("\n⚠️ Educational project only.")
    print("Not an official emergency warning system.")

    print("=" * 55)



# Main Menu

while True:

    print("\n")
    print("=" * 55)
    print("              🌍 MAIN MENU")
    print("=" * 55)

    print("1. 🌦️ Check Disaster Risk")
    print("2. 🤖 AI Model Information")
    print("3. ℹ️ About EarthGuardAI")
    print("4. 🚪 Exit")


    choice = input("\nEnter your choice (1-4): ")


    if choice == "1":
        check_risk()

    elif choice == "2":
        model_information()

    elif choice == "3":
        about_project()

    elif choice == "4":
        print("🌍 Thank you for using EarthGuardAI!")
        break

    else:
        print("❌ Invalid Choice!")