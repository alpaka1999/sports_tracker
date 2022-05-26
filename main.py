from flask import Flask
from flask import render_template
from flask import request

import piechart
import daten

app = Flask("Sports tracker")

"""
Dieses Projekt wurde in Einzelarbeit erarbeitet. Für das Projekt wurden vorwiegend die Vorlesungsunterlagen aus 
PROG1 und PROG2 sowie die Tutoring-Sessions genutzt. Weitere Quellen wie Youtube-Videos (wie Codemy.com), 
stackoverflow, die Bootstrap Dokumentation oder w3schools wurden für die Ausarbeitung des Projekts beigezogen.
"""

#Custom Error Pages: 404 & 500
#Invalid URL: 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error: 500
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

#Startseite / Home: Uebersichtsseite mit allen Aktivitäten, die in der Applikation vorgenommen werden können
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
        #Speicherung der Daten als in sport_data.json (siehe daten.py)
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
    #1. eingabe bezieht sich auf eingabe in uebersicht.html. 2. eingabe auf daten.laden() hier im main
    return render_template("uebersicht.html", eingabe=eingabe)

#Auswertungsseite: Auswertungen mit Kreisdiagramm und xy...
#NOTE: noch nicht fertig
#Ideen: Rangliste mit Top-Sportarten
#Idee: oben eingeben: ich möchte Sportart laufen und dann zeigts alle Daten laufen oder ich will nur Daten von Mai
#Welche Art von Daten möchte ich analysieren (ob Text oder Diagramm ist egal kann 1-2 Diagramme sein)
@app.route("/auswertung")
def auswertung():
    div = piechart.viz() #Kreisdiagramm (siehe piechart.py)
    return render_template("auswertung.html", viz_div=div)

#Zum Öffnen der Startseite des Projekts kann im Browser http://127.0.0.1:5000 aufgerufen werden
if __name__ == "__main__":
    app.run(debug=True, port=5000)