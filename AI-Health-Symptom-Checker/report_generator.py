import datetime
import os

os.makedirs("reports", exist_ok=True)

# AI-style suggestions per disease
SUGGESTIONS = {
    "Flu": [
        "Rest and stay hydrated — drink at least 8 glasses of water/day.",
        "Take paracetamol to manage fever and body aches.",
        "Avoid contact with others to prevent spreading the virus.",
        "Consult a doctor if fever exceeds 103°F or lasts more than 3 days."
    ],
    "Common Cold": [
        "Gargle with warm salt water to soothe your sore throat.",
        "Use steam inhalation for nasal congestion.",
        "Rest well and avoid cold beverages.",
        "Over-the-counter antihistamines may help reduce symptoms."
    ],
    "Typhoid": [
        "Visit a doctor immediately — typhoid requires antibiotic treatment.",
        "Drink boiled or filtered water only.",
        "Eat light, easily digestible food (khichdi, soups).",
        "Maintain strict hygiene and wash hands frequently."
    ],
    "Dengue": [
        "Monitor platelet count — visit a hospital if you feel very weak.",
        "Stay well hydrated with ORS, coconut water, or papaya leaf juice.",
        "Avoid aspirin or ibuprofen; use paracetamol for fever only.",
        "Rest under a mosquito net to avoid spreading dengue further."
    ],
    "Food Poisoning": [
        "Stop eating solid food temporarily; sip clear fluids.",
        "ORS (Oral Rehydration Salt) solution helps with dehydration.",
        "Avoid dairy, caffeine, and spicy foods until fully recovered.",
        "If vomiting or diarrhea persists beyond 48 hours, see a doctor."
    ],
    "Migraine": [
        "Rest in a quiet, dark room and avoid screen exposure.",
        "Apply a cold or warm compress on your forehead.",
        "Stay hydrated and avoid caffeine triggers.",
        "Keep a headache diary to identify and avoid your triggers."
    ],
    "Pneumonia": [
        "⚠️  Seek medical attention immediately — pneumonia can be serious.",
        "Take prescribed antibiotics for the full course.",
        "Rest completely and avoid physical exertion.",
        "Use a humidifier to ease breathing."
    ],
    "Asthma": [
        "Use your prescribed inhaler as directed by your doctor.",
        "Avoid triggers: dust, smoke, pollen, or pet dander.",
        "Practice breathing exercises like pursed-lip breathing.",
        "Carry your rescue inhaler at all times."
    ],
    "Gastritis": [
        "Avoid spicy, oily, and acidic foods temporarily.",
        "Eat smaller meals at regular intervals.",
        "Antacids can provide short-term relief.",
        "Avoid NSAIDs (like ibuprofen) as they irritate the stomach lining."
    ],
    "Gastroenteritis": [
        "Stay hydrated with ORS solution to replace lost fluids.",
        "Stick to bland foods: bananas, rice, toast, and boiled potatoes.",
        "Avoid dairy products until symptoms resolve.",
        "Wash hands thoroughly to prevent spreading the infection."
    ],
    "Strep Throat": [
        "Consult a doctor — strep throat usually needs antibiotics.",
        "Gargle with warm salt water 3-4 times a day.",
        "Drink warm fluids like herbal tea or soup.",
        "Rest your voice and avoid cold drinks."
    ],
    "Malaria": [
        "⚠️  See a doctor immediately for blood test confirmation.",
        "Antimalarial medication must be prescribed by a doctor.",
        "Use mosquito repellent and sleep under mosquito nets.",
        "Stay hydrated and rest completely."
    ],
    "Tension Headache": [
        "Take a break from screens and rest your eyes.",
        "Apply a warm compress to your neck and shoulders.",
        "Practice neck stretches and stress-relief techniques.",
        "Over-the-counter pain relievers like paracetamol can help."
    ],
    "Bronchitis": [
        "Stay hydrated and use a humidifier.",
        "Avoid smoke and air pollutants.",
        "Rest and avoid strenuous activity.",
        "See a doctor if you have a high fever or cough lasts more than 3 weeks."
    ],
    "Angina": [
        "⚠️  Seek emergency medical care if chest pain is severe.",
        "Rest immediately when pain occurs.",
        "Avoid physical exertion until evaluated by a doctor.",
        "Follow prescribed cardiac medications strictly."
    ],
}

DEFAULT_SUGGESTIONS = [
    "Consult a qualified healthcare professional for proper diagnosis.",
    "Rest adequately and stay hydrated.",
    "Monitor your symptoms and seek help if they worsen."
]

def generate_report(user_symptoms, predicted_disease, confidence, model_accuracy):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    suggestions = SUGGESTIONS.get(predicted_disease, DEFAULT_SUGGESTIONS)

    report = f"""
╔══════════════════════════════════════════════════════════════╗
║           AI HEALTH SYMPTOM CHECKER — HEALTH REPORT          ║
╚══════════════════════════════════════════════════════════════╝

  Report Generated : {now}
  Model Accuracy   : {model_accuracy:.1f}%

──────────────────────────────────────────────────────────────
  SYMPTOMS REPORTED
──────────────────────────────────────────────────────────────
  {", ".join([s.replace("_", " ").title() for s in user_symptoms])}

──────────────────────────────────────────────────────────────
  PREDICTION RESULT
──────────────────────────────────────────────────────────────
  Possible Condition : {predicted_disease}
  Confidence Score   : {confidence}%

──────────────────────────────────────────────────────────────
  AI-GENERATED HEALTH SUGGESTIONS
──────────────────────────────────────────────────────────────
"""
    for i, tip in enumerate(suggestions, 1):
        report += f"  {i}. {tip}\n"

    report += """
──────────────────────────────────────────────────────────────
  ⚠️  DISCLAIMER
──────────────────────────────────────────────────────────────
  This report is generated by an AI model for educational
  purposes only. It is NOT a substitute for professional
  medical advice, diagnosis, or treatment. Always consult
  a qualified healthcare provider for medical concerns.

══════════════════════════════════════════════════════════════
"""

    # Save to file
    path = "reports/health_report.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(report)

    print(report)
    print(f"  📄 Report saved to '{path}'")
    return report
