#import aller Funktionen und Dateien, die im piechart.py benötigt werden
import plotly.express as px
from plotly.offline import plot
import daten

#pie-chart von Plotly https://plotly.com/python/pie-charts mit den Daten aus der Funktion daten.diagramme()
#Daten stammen aus der Funktion diagramme() in daten.py. Hier wird nur der typ piechart aufgerufen.
#in den code-snippets von Plotly wird fig.show() verwendet. fig.show() öffnet ein eigenes Browserfenster.
#Daher div, um Diagramm im Sports Tracker anzeigen zu können
def viz():
    dauer, sportart = daten.diagramme("piechart")
    fig = px.pie(values=dauer, names=sportart,
                 labels={"values": "Dauer", "names": "Sportart"},
                 title="Erfasste Sportarten dargestellt nach Sportart und Dauer in Minuten")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    div = plot(fig, output_type="div")
    return div
