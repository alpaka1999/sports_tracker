from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

import plotly.express as px
from plotly.offline import plot

app = Flask("Sports tracker")

def get_data():
    jahr = [2015, 2016, 2017, 2018, 2019, 2021]
    loc = [1500, 3500, 12000, 9000, 10000, 4000]
    return jahr, loc

def viz():
    jahr, loc = get_data()
    fig = px.bar(x=jahr, y=loc)
    div = plot(fig, output_type="div")
    return div

@app.route('/')
def hello_world():
    auswertung_link = url_for("auswertung")
    return render_template("index.html", name="Selina", link=auswertung_link, dinger=["Ablauf", "Sportart", "To Do"])

@app.route("/uebersicht")
def auswertung():
    return "success"

@app.route("/auswertung")
def index():
    div = viz()
    return render_template('uebersicht.html', name="Selina", viz_div=div)

@app.route('//', methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        return "Vielen Dank für die Datenerfassung."

if __name__ == "__main__":
    app.run(debug=True, port=5000)