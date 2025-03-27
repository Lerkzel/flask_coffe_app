from flask import Flask, render_template
from database import get_top_10_countries
from visualization import generate_plots

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/visualization")
def visualization():
    generate_plots()
    return render_template("visualization.html")

if __name__ == "__main__":
    app.run(debug=True)
