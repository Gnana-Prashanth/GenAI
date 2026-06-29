"""
╔══════════════════════════════════════════════════════════════╗
║           AI HEALTH SYMPTOM CHECKER                          ║
║           Built with Python, ML, NumPy, Pandas,              ║
║           Matplotlib, Seaborn & Generative AI Concepts       ║
╚══════════════════════════════════════════════════════════════╝
"""

import numpy as np
import pandas as pd

from symptom_checker import load_and_train, get_user_symptoms, predict_disease, ALL_SYMPTOMS
from visualizations import generate_all_charts
from report_generator import generate_report


def print_banner():
    print("\n" + "="*62)
    print("   🏥  AI HEALTH SYMPTOM CHECKER")
    print("   Internship Major Project — Think Champ Pvt Ltd")
    print("="*62)


def show_data_insights(df):
    """Show basic Pandas + NumPy analysis of the dataset."""
    print("\n📂 Dataset Overview (Pandas + NumPy Analysis):")
    print(f"   • Total records   : {len(df)}")
    print(f"   • Total symptoms  : {len(ALL_SYMPTOMS)}")
    print(f"   • Unique diseases : {df['disease'].nunique()}")
    print(f"   • Diseases        : {', '.join(df['disease'].unique())}")

    # NumPy statistical analysis
    symptom_data = df[ALL_SYMPTOMS].values
    print(f"\n   NumPy Statistics on symptom columns:")
    print(f"   • Mean symptom occurrence : {np.mean(symptom_data):.3f}")
    print(f"   • Std deviation           : {np.std(symptom_data):.3f}")
    print(f"   • Total symptom reports   : {int(np.sum(symptom_data))}")

    # Most common symptoms
    symptom_counts = df[ALL_SYMPTOMS].sum().sort_values(ascending=False)
    print(f"\n   Top 3 most reported symptoms:")
    for sym, count in symptom_counts.head(3).items():
        print(f"   • {sym.replace('_', ' ').title()}: {int(count)} cases")


def main():
    print_banner()

    # Step 1 — Load dataset and train model
    print("\n⏳ Loading dataset and training ML model...")
    model, df, accuracy = load_and_train()
    print(f"   ✅ Model trained! Accuracy on test set: {accuracy:.1f}%")

    # Step 2 — Show data insights
    show_data_insights(df)

    # Step 3 — Get symptoms from user
    user_symptoms = get_user_symptoms()
    print(f"\n   ✅ Symptoms recorded: {', '.join([s.replace('_',' ').title() for s in user_symptoms])}")

    # Step 4 — Predict disease
    print("\n🔍 Analyzing symptoms...")
    predicted_disease, confidence, _ = predict_disease(model, user_symptoms)
    print(f"\n   🩺 Possible Condition : {predicted_disease}")
    print(f"   📊 Confidence Score   : {confidence}%")

    # Step 5 — Generate visualizations
    generate_all_charts(user_symptoms, ALL_SYMPTOMS, df, confidence)

    # Step 6 — Generate health report
    print("\n📋 Generating your health report...")
    generate_report(user_symptoms, predicted_disease, confidence, accuracy)

    print("\n✅ All done! Check the 'reports/' folder for your charts and report.")
    print("="*62 + "\n")


if __name__ == "__main__":
    main()
