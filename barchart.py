#import aller Funktionen und Dateien, die im barchart.py benötigt werden
import plotly.express as px
from plotly.offline import plot
import daten

#barchart von Plotly https://plotly.com/python/bar-charts/ mit den Daten aus der Funktion daten.diagramme()
#Daten stammen aus der Funktion diagramme() in daten.py. Hier wird nur der typ barchart aufgerufen.
#in den code-snippets von Plotly wird fig.show() verwendet. fig.show() öffnet ein eigenes Browserfenster.
#Daher div, um Diagramm im Sports Tracker anzeigen zu können
def viz():
    monat, distanz, sportart = daten.diagramme("barchart")
    fig = px.histogram(x=monat, y=distanz, color=sportart, barmode='group',
                     labels={"x": "Monat", "y": "Distanz in Schritte", "color": "Sportart"},
                     title="Erfasste Sportarten dargestellt nach Monat und Distanz in Schritte")
    #sortiert die x-Achse aufsteigend
    fig.update_layout(xaxis={'categoryorder':'category ascending'})
    div = plot(fig, output_type="div")
    return div

#zusammen hast du xy stunden sport gemacht