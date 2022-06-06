import plotly.express as px
from plotly.offline import plot
import daten

"""
Notizen Absprache Dozent:
Neu: wieviele Minuten bin ich ihn leicht, mittel, hart gewesen. json filtern, nur hart / mittel wenig, rechne Minuten
in % oder so aus. -> barplot.
Notizen: Filter einbauen bei Eingaben übersicht???
"""

#barchart von Plotly https://plotly.com/python/bar-charts/ mit den Daten aus der Funktion data.wiedergabe()
#Daten stammen aus der Funktion wiedergabe() in daten.py. Hier wird nur der typ barchart aufgerufen.
#in den code-snippets von Plotly wird fig.show() verwendet. fig.show() öffnet ein eigenes Browserfenster. Daher div, um Diagramm im Sports Tracker anzeigen zu können
def viz():
    monat, distanz, sportart = daten.wiedergabe("barchart")
    fig = px.histogram(x=monat, y=distanz, color=sportart, barmode='group',
                     labels={"x": "Monat", "y": "Distanz in Schritte", "color": "Sportart"},
                     title="Erfasste Sportarten dargestellt nach Monat und Distanz in Schritte")
    div = plot(fig, output_type="div")
    return div