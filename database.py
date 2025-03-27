import sqlite3

# Datu bāzes un tabulas izveide
def create_database():
    with sqlite3.connect("coffee.db") as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS coffee_consumption (
                        country TEXT,
                        consumption FLOAT)''')
        
        # Dati par kafijas patēriņu (kg uz vienu iedzīvotāju gadā)
        data = [  
            ("Nīderlande", 8.3), ("Somija", 7.8), ("Zviedrija", 7.6),  
            ("Norvēģija", 6.6), ("Kanāda", 5.5), ("Libāna", 5.3),  
            ("Vācija", 5.2), ("Brazīlija", 5.1), ("Katara", 5.0),  
            ("Šveice", 4.8), ("Itālija", 4.7), ("Igaunija", 4.3),  
            ("Portugāle", 4.0), ("ASV", 3.5), ("Francija", 3.4),  
            ("Ukraina", 1.5), ("Krievija", 1.2)  
        ]  
        c.executemany("INSERT INTO coffee_consumption VALUES (?, ?)", data)  
        conn.commit()

# 15 valstis ar lielāko kafijas patēriņu
def get_top_15_countries():
    with sqlite3.connect("coffee.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM coffee_consumption ORDER BY consumption DESC LIMIT 15")
        data = c.fetchall()
    return data

# Aprēķinām vidējo kafijas patēriņu
def get_average_consumption():
    with sqlite3.connect("coffee.db") as conn:
        c = conn.cursor()
        c.execute("SELECT AVG(consumption) FROM coffee_consumption")
        avg_consumption = c.fetchone()[0]
    return avg_consumption

# Filtrē valstis ar patēriņu virs norādītā līmeņa
def get_filtered_countries(min_consumption):
    with sqlite3.connect("coffee.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM coffee_consumption WHERE consumption >= ?", (min_consumption,))
        data = c.fetchall()
    return data

# Datu bāzes izveide un datu pievienošana
create_database()

# Piemēru vaicājumi
print("Tops 15 valstis pēc kafijas patēriņa:", get_top_15_countries())
print("Vidējais kafijas patēriņš:", get_average_consumption())
print("Valstis ar patēriņu virs 4 kg:", get_filtered_countries(4))
