# 🌍 EarthGuardAI

## 🤖 AI Disaster Prediction & Emergency Alert System

EarthGuardAI is an educational Artificial Intelligence and Machine Learning project that analyzes environmental conditions and predicts disaster risk levels using a Machine Learning model.

The system uses weather parameters such as temperature, rainfall, and wind speed to estimate possible disaster risk and provides alert messages to users.

---

# ✨ Features

✅ AI-based Disaster Risk Prediction  
✅ Machine Learning powered analysis  
✅ Decision Tree Classifier model  
✅ Weather condition analysis  
✅ Risk classification system  
✅ Simple command-line interface (CLI)  
✅ Emergency warning messages  
✅ Lightweight and easy to run  
✅ Educational AI/ML research project  

---

# 🧠 AI/ML Model

### Machine Learning Algorithm
- Decision Tree Classifier

### Input Parameters
The model takes three environmental inputs:

- 🌡️ Temperature (°C)
- 🌧️ Rainfall (mm)
- 💨 Wind Speed (km/h)

### Prediction Output

The system predicts:

- 🟢 LOW Risk
- 🟡 MEDIUM Risk
- 🟠 HIGH Risk
- 🔴 VERY HIGH Risk

---

# 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Machine Learning
- CSV Data Processing

---

# 📂 Project Structure
EarthGuardAI │ ├── main.py ├── model.py ├── history.py ├── requirements.txt ├── disaster_model.pkl ├── save_model.py ├── weather_data.csv ├── README.md └── LICENSE

---

# ⚙️ How to Run

## 1. Clone the repository

```bash
git clone https://github.com/devilritik8084-sudo/EarthGuardAI.git
2. Open the project folder
cd EarthGuardAI
3. Install required libraries
pip install -r requirements.txt
4. Run the application
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
📊 Example Prediction Logic
Example input:
Temperature: 42°C
Rainfall: 200mm
Wind Speed: 90km/h
Output:
Disaster Risk: HIGH
🎯 Project Purpose
EarthGuardAI was created to explore the application of Artificial Intelligence and Machine Learning in environmental risk analysis.
The project demonstrates how AI models can analyze weather-related data and classify possible risk levels.
⚠️ Disclaimer
EarthGuardAI is a student/research project created for educational purposes.
It is not an official disaster warning system and should not replace government emergency services or professional weather authorities.
👨‍💻 Developer
Ritik Kumar
AI & Software Development Enthusiast
📜 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this project according to the MIT License terms.
