#copy Odoni 10_presistent_Daten

from datetime import datetime
import json

#Funktion, um Daten von der Nutzereingabe auf der Eingabeseite (tracker.html) zu speichern.
#Daten werden in der datau sport_data-json json abgespeichert
def speichern(datei, key, value): #ab hier ergänzen: eingabedaten
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


def aktivitaet_speichern(aktivitaet):
    datei_name = "aktivitaeten_2.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, aktivitaet)
    return zeitpunkt, aktivitaet


def aktivitaeten_laden():
    datei_name = "aktivitaeten_2.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt