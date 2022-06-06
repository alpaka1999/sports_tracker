import plotly.express as px
from plotly.offline import plot
import daten


#pie-chart von Plotly https://plotly.com/python/pie-charts mit den Daten aus der Funktion data.wiedergabe()
#Daten stammen aus der Funktion wiedergabe() in daten.py. Hier wird nur der typ piechart aufgerufen.
#in den code-snippets von Plotly wird fig.show() verwendet. fig.show() öffnet ein eigenes Browserfenster. Daher div, um Diagramm im Sports Tracker anzeigen zu können
def viz():
    dauer, sportart = daten.wiedergabe("piechart")
    fig = px.pie(values=dauer, names=sportart,
                 labels={"values": "Dauer", "names": "Sportart"},
                 title="Erfasste Sportarten dargestellt nach Sportart und Dauer in Minuten")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    div = plot(fig, output_type="div")
    return div
