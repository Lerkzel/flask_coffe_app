import sqlite3  

# Izveido datubāzi un tabulu  
def create_database():  
    conn = sqlite3.connect("coffee.db")  
    c = conn.cursor()  
    c.execute('''CREATE TABLE IF NOT EXISTS coffee_consumption (  
                    country TEXT,  
                    consumption FLOAT)''')  

    # Kafijas patēriņa dati (kg uz vienu iedzīvotāju gadā)  
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
    conn.close()  

# Iegūst top 10 valstis pēc kafijas patēriņa  
def get_top_10_countries():  
    conn = sqlite3.connect("coffee.db")  
    c = conn.cursor()  
    c.execute("SELECT * FROM coffee_consumption ORDER BY consumption DESC LIMIT 10")  
    data = c.fetchall()  
    conn.close()  
    return data  

# Aprēķina vidējo kafijas patēriņu  
def get_average_consumption():  
    conn = sqlite3.connect("coffee.db")  
    c = conn.cursor()  
    c.execute("SELECT AVG(consumption) FROM coffee_consumption")  
    avg_consumption = c.fetchone()[0]  
    conn.close()  
    return avg_consumption  

# Filtrē valstis ar kafijas patēriņu virs noteikta līmeņa  
def get_filtered_countries(min_consumption):  
    conn = sqlite3.connect("coffee.db")  
    c = conn.cursor()  
    c.execute("SELECT * FROM coffee_consumption WHERE consumption >= ?", (min_consumption,))  
    data = c.fetchall()  
    conn.close()  
    return data  

# Izveido datubāzi un ievada datus  
create_database()  

# Testē vaicājumus  
print("Top 10 kafijas patēriņa valstis:", get_top_10_countries())  
print("Vidējais kafijas patēriņš:", get_average_consumption())  
print("Valstis ar patēriņu virs 4 kg:", get_filtered_countries(4))
