# 🌍 EarthGuardAI

## 🤖 AI Disaster Prediction & Emergency Alert System

EarthGuardAI is an educational Artificial Intelligence and Machine Learning project that analyzes environmental conditions and predicts a disaster-risk level using a Decision Tree Classifier.

The system uses weather parameters such as temperature, rainfall, and wind speed to estimate risk levels and provide safety alerts.

---

# ✨ Features

✅ AI-based Disaster Risk Prediction  
✅ Machine Learning Model (Decision Tree Classifier)  
✅ Weather Data Analysis  
✅ Risk Classification System  
✅ Simple Command-Line Interface (CLI)  
✅ Emergency Warning Messages  
✅ Historical Data Support  
✅ Lightweight Python Application  

---

# 🧠 AI/ML Model

**Machine Learning Algorithm:**
- Decision Tree Classifier

**Input Features:**
- Temperature (°C)
- Rainfall (mm)
- Wind Speed (km/h)

**Output:**
- Disaster Risk Level
  - LOW
  - MEDIUM
  - HIGH
  - VERY HIGH

---

# 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Machine Learning

---

# 📂 Project Structure
EarthGuardAI │ ├── main.py ├── model.py ├── history.py ├── requirements.txt ├── disaster_model.pkl ├── save_model.py ├── weather_data.csv ├── README.md └── LICENSE

---

# ⚙️ How to Run

### 1. Clone the repository

```bash
Open project folder
cd EarthGuardAI
Install dependencies
pip install -r requirements.txt
Run the application
python main.py
▶️ Output Example
🌍 EARTHGUARDAI
AI Disaster Prediction & Emergency Alert System

MAIN MENU

1. Check Disaster Risk
2. AI Model Information
3. About EarthGuardAI
4. Exit


Enter your choice: 1


Enter Temperature (°C): 42
Enter Rainfall (mm): 200
Enter Wind Speed (km/h): 90


🤖 EARTHGUARDAI RESULT

Temperature : 42 °C
Rainfall    : 200 mm
Wind Speed  : 90 km/h

🚨 Disaster Risk: HIGH

⚠️ WARNING:
High disaster risk detected!
Please follow official emergency instructions.
📌 Disclaimer
EarthGuardAI is a student/research project created for educational purposes.
It is not an official disaster warning system and should not replace government emergency services.
👨‍💻 Developer
Ritik Kumar
AI & Software Development Enthusiast
📜 License
This project is licensed under the MIT License.
