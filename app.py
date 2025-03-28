from flask import Flask, render_template
from database import get_top_15_countries, get_average_consumption, get_filtered_countries
import visualization  

app = Flask(__name__)

@app.route('/')
def index():
    visualization.get_top_countries()
    visualization.plot_age_distribution()
    visualization.plot_coffee_types()
    
    top_countries = get_top_15_countries()
    avg_consumption = get_average_consumption()
    filtered_countries = get_filtered_countries(4)
    return render_template('index.html',
                         top_countries=top_countries,
                         avg_consumption=avg_consumption,
                         filtered_countries=filtered_countries)

@app.route('/visualization')
def show_visualization():
    visualization.get_top_countries()
    visualization.plot_age_distribution()
    visualization.plot_coffee_types()
    return render_template('visualization.html')

if __name__ == '__main__':
    app.run(debug=True)