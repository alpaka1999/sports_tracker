from datetime import datetime
import json

#Funktion, um Daten von der Nutzereingabe auf der Eingabeseite (tracker.html) zu speichern.
#Daten werden in der Datei sport_data-json als dict abgespeichert
def speichern(sportart, intensivitaet, datum, dauer, distanz, kalorien):
    datei = "sport_data.json"
    try:
        #"r" = read file in "read-only" mode
        with open(datei, "r") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    #erstellt im json ein dict mit den Inhalten pro Eingabe in tracker.html
    #als Key für die json-Datei wird das Erfassungsdatum der Daten erfasst mit datetime.now()
    datei_inhalt[str(datetime.now())] = {"Sportart": sportart,
                                         "Intensivitaet": intensivitaet,
                                         "Datum": datum,
                                         "Dauer": dauer,
                                         "Distanz": distanz,
                                         "Kalorien": kalorien
                                         }
    #"w" = write file (neue Daten werden in json-Datei gespeichert)
    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

#Funktion, um gespeicherte Daten aus dem json laden und wiedergeben zu können
def laden():
    datei_name = "sport_data.json"
    try:
        #"r" = read file in "read-only" mode
        with open(datei_name, "r") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt