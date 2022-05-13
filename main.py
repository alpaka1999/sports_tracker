from flask import Flask
from flask import render_template
from flask import request

#ACHTUNG: Plotly noch nur aus Schulbeispiel, noch nicht zu benztzen
import plotly.express as px
from plotly.offline import plot

app = Flask("Sports tracker")

"""
Dieses Projekt wurde in Einzelarbeit erarbeitet. Für das Projekt wurden vorwiegend die Vorlesungsunterlagen aus 
PROG1 und PROG2 sowie die Tutoring-Sessions genutzt. Weitere Quellen wie Youtube-Videos (wie Codemy.com), 
stackoverflow, die Bootstrap Dokumentation oder w3schools wurden für die Ausarbeitung des Projekts beigezogen.
"""

#ACHTGUNG: Plotly testing stuff von Schule
def get_data():
    jahr = [2015, 2016, 2017, 2018, 2019, 2021]
    loc = [1500, 3500, 12000, 9000, 10000, 4000]
    return jahr, loc

def viz():
    jahr, loc = get_data()
    fig = px.bar(x=jahr, y=loc)
    div = plot(fig, output_type="div")
    return div

#Custom Error Pages
#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

#Startseite / Home
@app.route('/')
def home():
    return render_template("index.html", user="Selina")

#Formularseite "Neuer Eintrag"
#NOTE: Datenspeicherung ergänzen!!!!
@app.route('/tracker', methods=["GET", "POST"])
def tracker():
    if request.method == 'POST':
        tracking_datum = request.form['datum']
        rueckgabe_string = "Deine Daten zu deinem Training vom " + tracking_datum + " wurden gespeichert."
        return render_template("tracker.html", success_message=rueckgabe_string)
    else:
        return render_template("tracker.html")

#Überesichts Seite mit Übersicht der Erfassten Daten
#NOTE: noch nicht fertig
@app.route("/uebersicht")
def uebersicht():
    return render_template("uebersicht.html")

#ERGAENZEN: Titel
#NOTE: noch nicht fertig
@app.route("/auswertung")
def auswertung():
    div = viz()
    return render_template("auswertung.html", viz_div=div)

if __name__ == "__main__":
    app.run(debug=True, port=5000)