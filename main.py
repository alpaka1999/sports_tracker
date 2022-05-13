from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

import plotly.express as px
from plotly.offline import plot

app = Flask("Sports tracker")

#testing stuff
def get_data():
    jahr = [2015, 2016, 2017, 2018, 2019, 2021]
    loc = [1500, 3500, 12000, 9000, 10000, 4000]
    return jahr, loc

def viz():
    jahr, loc = get_data()
    fig = px.bar(x=jahr, y=loc)
    div = plot(fig, output_type="div")
    return div

#Startseite / Home
@app.route('/')
def home():
    return render_template("index.html", user="Selina")

#Überesichts Seite mit Übersicht der Erfassten Daten
@app.route("/uebersicht")
def uebersicht():
    return render_template("uebersicht.html")

@app.route("/auswertung")
def auswertung():
    div = viz()
    return render_template("auswertung.html", viz_div=div)

@app.route('/tracker', methods=["GET", "POST"])
def tracker():
    if request.method == "GET":
        return render_template('tracker.html')
    if request.method == "POST":
        return "Vielen Dank für die Datenerfassung."

    return render_template('formular.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)