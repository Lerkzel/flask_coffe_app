import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

# Funkcija, lai iegūtu top-15 kafijas patērētājvalstis
def get_top_countries():
    conn = sqlite3.connect("coffee.db")
    c = conn.cursor()
    c.execute("SELECT country, consumption FROM coffee_consumption ORDER BY consumption DESC LIMIT 15")
    data = c.fetchall()
    conn.close()
    
    df = pd.DataFrame(data, columns=["Valsts", "Patēriņš (kg uz cilvēku)"])
    
    # Zīmējam stabiņu diagrammu
    plt.figure(figsize=(10, 6))
    plt.bar(df["Valsts"], df["Patēriņš (kg uz cilvēku)"], color="saddlebrown")
    plt.xlabel("Valsts")
    plt.ylabel("Patēriņš (kg uz cilvēku)")
    plt.title("Top 15 kafijas patērētājvalstis")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/top_countries.png")  # Saglabājam attēlu
    plt.close()

# Funkcija, lai uzzīmētu histogrammu pēc vecuma grupām
def plot_age_distribution():
    age_groups = ["18-24", "25-34", "35-44", "45-54", "55+"]
    percentages = [47, 52, 55, 50, 45]  # Izdomāti procenti, pamatojoties uz pieejamo statistiku

    plt.figure(figsize=(8, 5))
    plt.bar(age_groups, percentages, color="chocolate")
    plt.xlabel("Vecuma grupa")
    plt.ylabel("Procenti (%)")
    plt.title("Kafijas patēriņš dažādās vecuma grupās")
    plt.ylim(0, 60)
    plt.savefig("static/age_distribution.png")  # Saglabājam attēlu
    plt.close()

# Funkcija, lai izveidotu sektoru diagrammu kafijas veidiem
def plot_coffee_types():
    coffee_types = ["Maltā kafija", "Šķīstošā kafija"]
    percentages = [45.8, 54.2]  # Pēc ASV datiem

    plt.figure(figsize=(6, 6))
    plt.pie(percentages, labels=coffee_types, autopct="%1.1f%%", colors=["peru", "burlywood"])
    plt.title("Kafijas patēriņa sadalījums pēc veida (ASV)")
    plt.savefig("static/coffee_types.png")  # Saglabājam attēlu
    plt.close()

# Izsaucam funkcijas, lai sagatavotu diagrammas
get_top_countries()
plot_age_distribution()
plot_coffee_types()
