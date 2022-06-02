import plotly.express as px
from plotly.offline import plot
import daten

"""
Notizen Absprache Dozent:
DONE Woche: Datum in date.time(), dann extrahieren date.time get week -> dann kann man Woche kriegen.
DONE Neu: Monat & sportart x -> Monat wie jede aussieht, y distanz in Schritte. Barplot.
Neu: wieviele Minuten bin ich ihn leicht, mittel, hart gewesen. json filtern, nur hart / mittel wenig, rechne Minuten
in % oder so aus. -> barplot.
-> Struktur von Daten holen als Funktion definieren -> data z.B.
"""

def data():
    eingabe = daten.laden() #daten von data.json werden aufgerufen mit der Funktion laden() in daten.py
    monat = [] #leere Listen, die dann mit Daten aus sport_data.json ergänzt wird
    distanz = []
    sportart = []

    #ergänzt die leeren Listen dauer und sportart mit den Eingabedaten aus data.json
    for key, value in eingabe.items():
        distance = int(value["Distanz"])
        date = value["Datum"]
        date = date.split("-")
        sport = value["Sportart"]
        distanz.append(distance)
        monat.append(date[1])
        sportart.append(sport)

    return monat, distanz, sportart

#scatterplot von Plotly https://plotly.com/python/bar-charts/ mit den Daten aus der Funktion data()
#in den code-snippets von Plotly wird fig.show() verwendet. fig.show() öffnet ein eigenes Browserfenster. Daher div, um Diagramm im Sports Tracker anzeigen zu können
def viz():
    monat, distanz, sportart = data()
    fig = px.histogram(x=monat, y=distanz, color=sportart, barmode='group',
                     labels={"x": "Monat", "y": "Distanz in Schritte", "color": "Sportart"},
                     title="Erfasste Sportarten dargestellt nach Monat und Distanz in Schritte")
    div = plot(fig, output_type="div")
    return div