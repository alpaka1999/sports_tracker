import plotly.express as px
from plotly.offline import plot
import daten

def data():
    eingabe = daten.laden() #daten von data.json werden aufgerufen mit der Funktion laden() in daten.py
    dauer = [] #leere Listen, die dann mit Daten aus sport_data.json ergänzt wird
    distanz = []
    kalorien = []
    datum = []
    sportart = []

    #ergänzt die leeren Listen dauer und sportart mit den Eingabedaten aus data.json
    for key, value in eingabe.items():
        duration = int(value["Dauer"])
        distance = int(value["Distanz"])
        calories = int(value["Kalorien"])
        date = value["Datum"]
        sport = value["Sportart"]
        dauer.append(duration)
        distanz.append(distance)
        kalorien.append(calories)
        datum.append(date)
        sportart.append(sport)

    return dauer, distanz, kalorien, datum, sportart

#scatterplot von Plotly https://plotly.com/python/line-and-scatter mit den Daten aus der Funktion data()
#in den code-snippets von Plotly wird fig.show() verwendet. fig.show() öffnet ein eigenes Browserfenster. Daher div, um Diagramm im Sports Tracker anzeigen zu können
#hover_data: Argument für weitere Elemente im Hover. Ausgegeben wird die 1. Eingabe mit 0 (da Liste). Daher in labels "hover_data_0"
def viz():
    dauer, distanz, kalorien, datum, sportart = data()
    fig = px.scatter(x=dauer, y=distanz, size=kalorien, color=sportart, hover_data=[datum],
                     labels={"x": "Dauer in Minuten", "y": "Distanz in Schritte", "size": "Kalorien", "color": "Sportart", "hover_data_0": "Datum"},
                     title="Korrelation Dauer(x), Distanz(y), Kalorien(Kreisgrösse) und Sportart(Farbe)")
    div = plot(fig, output_type="div")
    return div