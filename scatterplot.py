#import aller Funktionen und Dateien, die im scatterplot.py benötigt werden
import plotly.express as px
from plotly.offline import plot
import daten

#scatterplot von Plotly https://plotly.com/python/line-and-scatter mit den Daten aus der Funktion daten.diagramme()
#Daten stammen aus der Funktion diagramme() in daten.py. Hier wird nur der typ scatterplot aufgerufen.
#in den code-snippets von Plotly wird fig.show() verwendet. fig.show() öffnet ein eigenes Browserfenster.
#Daher div, um Diagramm im Sports Tracker anzeigen zu können
#hover_data: Argument für weitere Elemente im Hover. Ausgegeben wird die 1. Eingabe mit 0 (da Liste).
#Daher in labels "hover_data_0"
def viz():
    dauer, distanz, kalorien, datum, sportart = daten.diagramme("scatterplot")
    fig = px.scatter(x=dauer, y=distanz, size=kalorien, color=sportart, hover_data=[datum],
                     labels={"x": "Dauer in Minuten", "y": "Distanz in Schritte", "size": "Kalorien",
                             "color": "Sportart", "hover_data_0": "Datum"},
                     title="Korrelation Dauer(x), Distanz(y), Kalorien(Kreisgrösse) und Sportart(Farbe)")
    div = plot(fig, output_type="div")
    return div