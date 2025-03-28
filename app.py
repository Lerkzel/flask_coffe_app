from flask import Flask, render_template
from database import get_top_15_countries, get_average_consumption, get_filtered_countries

app = Flask(__name__)

@app.route('/')
def index():
    top_countries = get_top_15_countries()
    avg_consumption = get_average_consumption()
    filtered_countries = get_filtered_countries(4)
    
    return render_template("index.html",
                           top_countries=top_countries,
                           avg_consumption=avg_consumption,
                           filtered_countries=filtered_countries)

if __name__ == '__main__':
    app.run(debug=True)
