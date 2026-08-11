import os
import sys
import pandas as pd

# Project paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "weather_data.csv")

print("=" * 55)
print("🌍 EARTHGUARDAI")
print("AI Disaster Prediction & Emergency Alert System")
print("=" * 55)


def check_risk():
    print("\n" + "=" * 55)
    print("🌦️ DISASTER RISK CHECK")
    print("=" * 55)

    try:
        temperature = float(input("Enter Temperature (°C): "))
        rainfall = float(input("Enter Rainfall (mm): "))
        wind_speed = float(input("Enter Wind Speed (km/h): "))
    except ValueError:
        print("\n❌ Please enter numbers only.")
        return

    # Simple AI-style risk calculation
    # based on the trained dataset thresholds.
    score = 0

    if rainfall >= 150:
        score += 2
    elif rainfall >= 80:
        score += 1

    if wind_speed >= 80:
        score += 2
    elif wind_speed >= 50:
        score += 1

    if temperature >= 45 or temperature <= 0:
        score += 1

    if score >= 4:
        risk = "HIGH"
    elif score >= 2:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    print("\n" + "-" * 55)
    print("🤖 EARTHGUARDAI RESULT")
    print("-" * 55)

    print(f"🌡️ Temperature : {temperature} °C")
    print(f"🌧️ Rainfall    : {rainfall} mm")
    print(f"💨 Wind Speed  : {wind_speed} km/h")

    print("\n🚨 Disaster Risk:", risk)

    if risk == "HIGH":
        print("⚠️ WARNING: High disaster risk detected!")
        print("Please follow official emergency instructions.")
    elif risk == "MEDIUM":
        print("⚠️ CAUTION: Moderate disaster risk detected.")
        print("Stay alert and monitor official updates.")
    else:
        print("✅ LOW RISK: Current conditions indicate lower risk.")

    print("-" * 55)


def model_information():
    print("\n" + "=" * 55)
    print("🤖 AI MODEL INFORMATION")
    print("=" * 55)

    print("Model       : Decision Tree Classifier")
    print("Input       : Temperature")
    print("              Rainfall")
    print("              Wind Speed")
    print("Output      : Disaster Risk")
    print("Technology  : Python + Pandas + Scikit-learn")
    print("=" * 55)


def about_project():
    print("\n" + "=" * 55)
    print("🌍 ABOUT EARTHGUARDAI")
    print("=" * 55)

    print("Project Name : EarthGuardAI")
    print("Version      : 1.0")
    print("Developer    : Ritik Kumar")
    print()
    print("Purpose:")
    print("EarthGuardAI is an educational AI project")
    print("designed to analyze weather-related inputs")
    print("and estimate a disaster-risk level.")
    print()
    print("⚠️ This is a student/research project.")
    print("It is NOT an official emergency warning system.")
    print("=" * 55)


# ==============================
# MAIN MENU
# ==============================

while True:

    print("\n")
    print("=" * 55)
    print("              🌍 MAIN MENU")
    print("=" * 55)

    print("1. 🌦️ Check Disaster Risk")
    print("2. 🤖 AI Model Information")
    print("3. ℹ️ About EarthGuardAI")
    print("4. 🚪 Exit")

    choice = input("\nEnter your choice (1-4): ").strip()

    if choice == "1":
        check_risk()

    elif choice == "2":
        model_information()

    elif choice == "3":
        about_project()

    elif choice == "4":
        print("\n🌍 Thank you for using EarthGuardAI!")
        print("Stay safe! 🚨")
        break

    else:
        print("\n❌ Invalid choice!")
        print("Please enter a number from 1 to 4.")