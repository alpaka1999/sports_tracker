from datetime import datetime
import json

#Funktion, um Daten von der Nutzereingabe auf der Eingabeseite (tracker.html) zu speichern.
#Daten werden in der datei sport_data-json json abgespeichert
def speichern(sportart, intensivitaet, datum, dauer, distanz, kalorien):
    datei = "sport_data.json"
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

#als Key wird das Erfassungsdatum der Daten eingegeben
    datei_inhalt[str(datetime.now())] = {"Sportart": sportart,
                                         "Intensivität": intensivitaet,
                                         "Datum": datum,
                                         "Dauer": dauer,
                                         "Distanz": distanz,
                                         "Kalorien": kalorien
                                         }

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

#Funktion, um gespeicherte Daten laden zu können
def laden():
    datei_name = "sport_data.json"
    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt