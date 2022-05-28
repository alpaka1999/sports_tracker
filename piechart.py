import plotly.express as px
from plotly.offline import plot
import daten

def data():
    eingabe = daten.laden() #daten von data.json werden aufgerufen
    dauer = []
    sportart = []

    #ergänzt die leeren Listen dauer und sportart mit den Eingabedaten aus data.json
    for key, value in eingabe.items():
        duration = value["Dauer"]
        sport = value["Sportart"]
        dauer.append(duration)
        sportart.append(sport)

    return dauer, sportart

#pie-chart von Plotly https://plotly.com/python/pie-charts mit den Daten aus der Funktion data()
#in den code-snippets von Plotly wird fig.show() verwendet. fig.show() öffnet ein eigenes Browserfenster. Daher div, um Diagramm im Sports Tracker anzeigen zu können
def viz():
    dauer, sportart = data()
    fig = px.pie(values=dauer, names=sportart,
                 labels={"values": "Dauer", "names": "Sportart"},
                 title="Erfasste Sportarten dargestellt nach Sportart und Dauer")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    div = plot(fig, output_type="div")
    return div
