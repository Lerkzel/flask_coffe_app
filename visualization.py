import matplotlib.pyplot as plt
import pandas as pd
from database import get_top_10_countries

def generate_plots():
    data = get_top_10_countries()
    df = pd.DataFrame(data, columns=["Country", "Consumption"])

    plt.figure(figsize=(10, 5))
    plt.bar(df["Country"], df["Consumption"], color="brown")
    plt.xlabel("Country")
    plt.ylabel("Coffee Consumption (kg per capita)")
    plt.title("Top 10 Coffee Consuming Countries")
    plt.xticks(rotation=45)
    
    plt.savefig("static/coffee_plot.png")
    plt.close()
