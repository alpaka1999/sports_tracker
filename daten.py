from datetime import datetime
import json

#Funktion, um Daten von der Nutzereingabe auf der Eingabeseite (tracker.html) zu speichern.
#Daten werden in der Datei sport_data-json als dict abgespeichert
def speichern(sportart, intensivitaet, datum, dauer, distanz, kalorien):
    datei = "sport_data.json"
    try:
        with open(datei, "r") as open_file: #"r" = read file in "read-only" mode
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    #erstellt im json ein dict mit den Inhalten pro Eingabe unter tracker.html
    #als Key für die json-Datei wird das Erfassungsdatum der Daten erfasst mit datetime.now()
    datei_inhalt[str(datetime.now())] = {"Sportart": sportart,
                                         "Intensivitaet": intensivitaet,
                                         "Datum": datum,
                                         "Dauer": int(dauer),
                                         "Distanz": int(distanz),
                                         "Kalorien": int(kalorien)
                                         }

    with open(datei, "w") as open_file: #"w" = write file (neue Daten werden in json-Datei gespeichert)
        json.dump(datei_inhalt, open_file, indent=4)

#Funktion, um gespeicherte Daten aus dem json laden und wiedergeben zu können
def laden():
    datei_name = "sport_data.json"
    try:
        with open(datei_name, "r") as open_file: #"r" = read file in "read-only" mode
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt