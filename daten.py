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

#Funktion, um einzelne Daten aus sport_data.json zu laden und für die Ausgabe wiederzugeben
def wiedergabe(typ):
    if typ == "barchart":
        eingabe = laden() #daten von sport_data.jso werden aufgerufen mit der Funktion laden()
        monat = [] #leere Listen, die dann mit Daten aus sport_data.json ergänzt wird
        distanz = []
        sportart = []

        #ergänzt die leeren Listen monat, distanz und sportart mit den Eingabedaten aus sport_data.json
        for key, value in eingabe.items():
            distance = int(value["Distanz"])
            date = value["Datum"]
            date = date.split("-") #splitet Daten vom Datum nach - und gibt Daten dann gesplittet in einer Liste aus
            sport = value["Sportart"]
            distanz.append(distance)
            monat.append(date[1]) #nimmt in der gespliteten data liste nur das mittlere Element (Monat)
            sportart.append(sport)

        return monat, distanz, sportart
    elif typ == "piechart":
        eingabe = laden()  #daten von sport_data.jso werden aufgerufen mit der Funktion laden()
        dauer = []  #leere Listen, die dann mit Daten aus sport_data.json ergänzt wird
        sportart = []

        #ergänzt die leeren Listen dauer und sportart mit den Eingabedaten aus sport_data.json
        for key, value in eingabe.items():
            duration = int(value["Dauer"])
            sport = value["Sportart"]
            dauer.append(duration)
            sportart.append(sport)

        return dauer, sportart
    elif typ == "scatterplot":
        eingabe = laden()  #daten von sport_data.jso werden aufgerufen mit der Funktion laden()
        dauer = []  #leere Listen, die dann mit Daten aus sport_data.json ergänzt wird
        distanz = []
        kalorien = []
        datum = []
        sportart = []

        #ergänzt die leeren Listen dauer, distanz, kalorien, datum und sportart mit den Eingabedaten aus data.json
        for key, value in eingabe.items():
            duration = int(value["Dauer"])
            distance = int(value["Distanz"])
            calories = int(value["Kalorien"])
            date = value["Datum"]
            sport = value["Sportart"]
            dauer.append(duration)
            distanz.append(distance)
            kalorien.append(calories)
            datum.append(date)
            sportart.append(sport)

        return dauer, distanz, kalorien, datum, sportart