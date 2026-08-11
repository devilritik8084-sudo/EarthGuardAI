import os
import csv
from datetime import datetime

HISTORY_FILE = os.path.join(
    os.path.dirname(__file__),
    "data",
    "prediction_history.csv"
)


def save_prediction(temperature, rainfall, wind_speed, risk):

    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)

    file_exists = os.path.exists(HISTORY_FILE)

    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Time",
                "Temperature",
                "Rainfall",
                "Wind Speed",
                "Risk Level"
            ])

        now = datetime.now()

        writer.writerow([
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S"),
            temperature,
            rainfall,
            wind_speed,
            risk
        ])

    print("✅ Prediction saved to history!")


def show_history():

    if not os.path.exists(HISTORY_FILE):
        print("\n📂 No prediction history found.")
        return

    print("\n" + "=" * 60)
    print("📜 EARTHGUARD AI - PREDICTION HISTORY")
    print("=" * 60)

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:

        reader = csv.reader(file)

        for row in reader:
            print(" | ".join(row))

    print("=" * 60)


if __name__ == "__main__":
    show_history()