#import aller Funktionen und Dateien, die im main.py benötigt werden
from flask import Flask
from flask import render_template
from flask import request

import piechart
import scatterplot
import barchart
import daten

#Installation Flask mit der App-Bennenung "Sports tracker"
app = Flask("Sports tracker")

"""
Dieses Projekt wurde in Einzelarbeit erarbeitet. Für das Projekt wurden vorwiegend die Vorlesungsunterlagen aus 
PROG1 und PROG2 sowie die Tutoring-Sessions genutzt. Weitere Quellen wie Youtube-Videos (wie Codemy.com), 
stackoverflow, die Bootstrap Dokumentation oder w3schools wurden für die Ausarbeitung des Projekts beigezogen.
"""

#Custom Error Page: Invalid URL: 404 nach https://www.youtube.com/watch?v=3O4ZmH5aolg
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Custom Error Page: Internal Server Error: 500 nach https://www.youtube.com/watch?v=3O4ZmH5aolg
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

#Startseite / Home: Übersichtsseite mit allen Aktivitäten, die in der Applikation vorgenommen werden können
@app.route('/')
def home():
    return render_template("index.html", user="Selina")

#Formularseite "Neuer Eintrag": hier kann der User neue Sportdaten erfassen.
#Wenn POST: Übermittlung der zu verarbeitenden Daten an den Server, sobald der Button "Daten speichern" gedrückt wird
#Ansonsten: tracker.html Seite wird angezeigt
@app.route('/tracker', methods=["GET", "POST"])
def tracker():
    if request.method == 'POST':
        #Bezieht sich auf das jeweilige Attribute "name=" in tracker.html
        sportart = request.form['sportart']
        intensivitaet = request.form['intensivitaet']
        datum = request.form['datum']
        dauer = request.form['dauer']
        distanz = request.form['distanz']
        kalorien = request.form['kalorien']
        #Speicherung der Daten in sport_data.json (siehe daten.py)
        daten.speichern(sportart, intensivitaet, datum, dauer, distanz, kalorien)
        #Rückgabe-Message nachdem der Button "Daten speichern" gedrückt wird
        rueckgabe_string = "Deine Daten zu deinem Training vom " + datum + " wurden gespeichert."
        return render_template("tracker.html", success_message=rueckgabe_string)
    else:
        return render_template("tracker.html")

#Überesichtsseite: Übersicht der Erfassten Daten aus sport_data.json
#Daten werden aus aus sport_data.json geladen und in uebersicht.html wiedergegeben (siehe daten.py)
@app.route("/uebersicht")
def uebersicht():
    eingabe = daten.laden()
    return render_template("uebersicht.html", eingabe=eingabe)

#Auswertungsseite: Auswertungen mit Berechnung Gesamtdauer in Stunde & Kreisdiagramm, Scatter Plot und Balkendiagramm
#Diagramme sind jeweils in einem separaten Python File
@app.route("/auswertung")
def auswertung():
    gesamtdauer = daten.gesamtdauer() #gesamtdauer in Stunden
    div1 = piechart.viz() #Kreisdiagramm (siehe piechart.py)
    div2 = scatterplot.viz() #Scatter Plot (siehe scatterplot.py)
    div3 = barchart.viz() #Balkendieagramm (siehe barchart.py)
    return render_template("auswertung.html", gesamtdauer=gesamtdauer, viz_piechart=div1, viz_scatterplot=div2, viz_barchart=div3)

#Zum Öffnen der Startseite des Sport Trackers kann im Browser http://127.0.0.1:5000 aufgerufen werden
if __name__ == "__main__":
    app.run(debug=True, port=5000)