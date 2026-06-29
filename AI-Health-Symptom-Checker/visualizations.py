import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Create output folder for charts
os.makedirs("reports", exist_ok=True)

def plot_symptom_bar(user_symptoms, all_symptoms):
    """Bar chart of user's entered symptoms."""
    values = [1 if s in user_symptoms else 0 for s in all_symptoms]
    labels = [s.replace("_", " ").title() for s in all_symptoms]

    colors = ["#e74c3c" if v == 1 else "#95a5a6" for v in values]

    plt.figure(figsize=(12, 5))
    bars = plt.bar(labels, values, color=colors, edgecolor="black")
    plt.title("Your Reported Symptoms", fontsize=16, fontweight="bold")
    plt.ylabel("Present (1) / Absent (0)")
    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, 1.3)

    for bar, val in zip(bars, values):
        if val == 1:
            plt.text(bar.get_x() + bar.get_width()/2, 1.05, "✓",
                     ha="center", fontsize=13, color="#27ae60", fontweight="bold")

    plt.tight_layout()
    plt.savefig("reports/symptom_bar.png", dpi=150)
    plt.show()
    print("  ✅ Symptom bar chart saved.")

def plot_disease_heatmap(df, all_symptoms):
    """Heatmap showing symptom patterns per disease."""
    disease_avg = df.groupby("disease")[all_symptoms].mean()
    disease_avg.columns = [c.replace("_", " ").title() for c in disease_avg.columns]

    plt.figure(figsize=(14, 7))
    sns.heatmap(
        disease_avg,
        annot=True, fmt=".1f",
        cmap="YlOrRd",
        linewidths=0.5,
        cbar_kws={"label": "Avg Occurrence"}
    )
    plt.title("Symptom Patterns by Disease", fontsize=16, fontweight="bold")
    plt.ylabel("Disease")
    plt.xlabel("Symptom")
    plt.tight_layout()
    plt.savefig("reports/disease_heatmap.png", dpi=150)
    plt.show()
    print("  ✅ Disease heatmap saved.")

def plot_disease_distribution(df):
    """Pie chart of disease distribution in dataset."""
    counts = df["disease"].value_counts()

    plt.figure(figsize=(9, 9))
    wedges, texts, autotexts = plt.pie(
        counts,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=140,
        colors=sns.color_palette("Set2", len(counts))
    )
    for text in autotexts:
        text.set_fontsize(9)

    plt.title("Disease Distribution in Dataset", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.savefig("reports/disease_pie.png", dpi=150)
    plt.show()
    print("  ✅ Disease distribution pie chart saved.")

def plot_confidence_gauge(confidence):
    """Horizontal bar showing confidence score."""
    fig, ax = plt.subplots(figsize=(8, 2))

    ax.barh(["Confidence"], [100], color="#ecf0f1", edgecolor="gray", height=0.5)
    color = "#27ae60" if confidence >= 70 else "#e67e22" if confidence >= 45 else "#e74c3c"
    ax.barh(["Confidence"], [confidence], color=color, edgecolor="gray", height=0.5)

    ax.set_xlim(0, 100)
    ax.set_xlabel("Confidence (%)")
    ax.set_title(f"Prediction Confidence: {confidence}%", fontsize=14, fontweight="bold")
    ax.axvline(x=confidence, color="black", linestyle="--", linewidth=1)

    plt.tight_layout()
    plt.savefig("reports/confidence_gauge.png", dpi=150)
    plt.show()
    print("  ✅ Confidence gauge saved.")

def generate_all_charts(user_symptoms, all_symptoms, df, confidence):
    print("\n📊 Generating visualizations...")
    plot_symptom_bar(user_symptoms, all_symptoms)
    plot_disease_distribution(df)
    plot_disease_heatmap(df, all_symptoms)
    plot_confidence_gauge(confidence)
    print("  All charts saved in the 'reports/' folder.\n")
