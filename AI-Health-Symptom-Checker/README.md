# 🏥 AI Health Symptom Checker
**Internship Major Project — Think Champ Pvt Ltd**

---

## 📁 Project Structure

```
AI_Health_Symptom_Checker/
│
├── app.py                  ← Main entry point (run this)
├── symptom_checker.py      ← ML model: load data, train, predict
├── visualizations.py       ← Charts using Matplotlib & Seaborn
├── report_generator.py     ← AI-based health report generator
├── dataset.csv             ← Symptom-disease training dataset
├── requirements.txt        ← Python dependencies
├── reports/
│   ├── health_report.txt   ← Generated health report
│   ├── symptom_bar.png     ← Bar chart of your symptoms
│   ├── disease_pie.png     ← Disease distribution in dataset
│   ├── disease_heatmap.png ← Heatmap of symptom patterns
│   └── confidence_gauge.png← Prediction confidence bar
└── README.md               ← This file
```

---

## ⚙️ Setup & Installation

### 1. Make sure Python is installed
```bash
python --version   # should be 3.8+
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the project
```bash
python app.py
```

---

## 🚀 How It Works

1. **Dataset is loaded** from `dataset.csv` using Pandas
2. **ML Model (Random Forest)** is trained on symptom data
3. **You enter your symptoms** from a list
4. **The model predicts** the most likely disease + confidence score
5. **Charts are generated** and saved in `reports/`
6. **A health report** with AI suggestions is saved and displayed

---

## 🧪 Technologies Used

| Technology     | Usage                                      |
|----------------|--------------------------------------------|
| Python         | Core programming                           |
| NumPy          | Statistical analysis on symptom data       |
| Pandas         | Dataset loading, cleaning, analysis        |
| Matplotlib     | Bar chart, pie chart, confidence gauge     |
| Seaborn        | Heatmap of symptom-disease patterns        |
| Scikit-learn   | Random Forest Classifier (ML model)        |
| Generative AI  | Rule-based AI health suggestions per disease|

---

## ⚠️ Disclaimer
This tool is for **educational purposes only**. It is NOT a substitute for professional medical advice.
