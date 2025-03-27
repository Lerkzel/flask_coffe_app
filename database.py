import sqlite3

def create_database():
    conn = sqlite3.connect("coffee.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS coffee_consumption (
                    country TEXT, 
                    consumption FLOAT)''')
    
    # Пример данных (страны и их потребление кофе на душу населения)
    data = [
        ("Finland", 12.0), ("Norway", 9.9), ("Iceland", 9.0),
        ("Denmark", 8.7), ("Netherlands", 8.4), ("Sweden", 8.2),
        ("Switzerland", 7.9), ("Belgium", 6.8), ("Luxembourg", 6.5), ("Canada", 6.2)
    ]
    
    c.executemany("INSERT INTO coffee_consumption VALUES (?, ?)", data)
    conn.commit()
    conn.close()

def get_top_10_countries():
    conn = sqlite3.connect("coffee.db")
    c = conn.cursor()
    c.execute("SELECT * FROM coffee_consumption ORDER BY consumption DESC LIMIT 10")
    data = c.fetchall()
    conn.close()
    return data

def get_average_consumption():
    conn = sqlite3.connect("coffee.db")
    c = conn.cursor()
    c.execute("SELECT AVG(consumption) FROM coffee_consumption")
    avg_consumption = c.fetchone()[0]
    conn.close()
    return avg_consumption

def get_filtered_countries(min_consumption):
    conn = sqlite3.connect("coffee.db")
    c = conn.cursor()
    c.execute("SELECT * FROM coffee_consumption WHERE consumption >= ?", (min_consumption,))
    data = c.fetchall()
    conn.close()
    return data
