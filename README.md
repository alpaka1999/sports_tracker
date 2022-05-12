#Sports Tracker
##Problembeschreibung / Motivation
 - Warum dieses Projekt
 - Welches Problem löst das Projekt
 - Was macht das Projekt
 - Lückenfüller wie: "Dieses Projekt wurde im Rahmen des Programmieren2 Modules an der FHGR gemacht" oder ähnlich sind unnötig. Auch sollten keine Klarnamen, oder Orte genannt werden.

Im Rahmen des Moduls PROG2 hatten die Studierenden den Auftrag, 
eine Webapp zu erstellen, die Daten speichern, verarbeiten und 
wiedergeben kann.

Meine Idee ist ein Sport Tracker, der wie eine Fitbit 
Sportdaten eines Nutzers über ein Webformular entgegennimmt, 
speichert und in Form von einer Auswertungen ausgibt. Der 
Nutzer hat die Möglichkeit, in der Analyse Filter zu nutzen.

Das Sport-Tool löst teure Sportapps ab und kann als Eigenentwicklung 
genutzt werden, um das Sportverhalten des Nutzers zu analysieren. 

##Benutzung
- Wie wird das Projekt benutzt
- Welche Optionen oder auch Spezialitäten existieren
- worauf bin ich stolz

Der Sports Tracker ist so aufgebaut, dass der Nutzer direkt auf 
der Startseite die gewünschte Aktivität aussuchen kann. 

Von der Startseite aus kann der Nutzer auf die Eingabe-Seite für ein 
neues Sportarten-Tracking wechsel. Dort kann der Nutzer bei der Dateneingabe 
die absolvierte Sportart auswählen. Dabei kann der Nutzer zwischen folgenden 
Sportarten unterscheiden: Laufen, Fahrradfahren, Wandern, Tennis, Schwimmen
und Workout. Anschliessend macht der Nutzer Angaben über die Tageszeit, 
die Länge des Trainings, die zurückgelegten Kilometer, die Intension und die 
verbrannten Kalorien. Abgespeichert werden die Daten in einem Json-File, 
welches in der Übersicht visualisiert betrachtet werden kann.

In der Übersicht sieht der Nutzer alle erfassten Daten, sortiert nach 
Eingabedatum. Der Nutzer kann die Daten zudem nach Sportart filtern. 
Die entsprechenden Daten pro Sportart werden dem Nutzer in einer Liste 
dargestellt.

Auf der Seite Auswertung hat der Nutzer die Möglichkeit, eine Statistik
zu erhalten. Der Nutzer hat so die Möglichkeit, sich die Daten im Total, 
pro Monat, pro Woche oder pro Tag anzeigen zu lassen. Die Daten werden 
in einem xy...diagramm (mittels Plotly) dargestellt.
**ACHTUNG: Datenausgabe in x / y Achse. Pro Sportart möglich oder nur im 
Total pro Mt / Woche???**

##Betrieb
 - Welche zusätzliche Pakete müssen bei Bedarf installiert werden. (Muss im Normalfall nicht beachtet werden. Python muss nicht erwähnt werden, da das bei einem Python Projekt impliziert ist.)
 - Was muss man bei der Ausführung beachten. Was muss eventuell davor noch gemacht werden.
 - Welch Datei muss ausgeführt werden

##Architektur
- Hier bei Bedarf eine kurze Beschreibung des Ablaufs des Programms auf Code Ebene z.B. als Ablaufdiagramm.
- flussdiagramm rein (Grafik, 2 Sätze)

##Ungelöste / unbearbeitete Probleme
 - Selbstreflexion, Grenzen aufzeigen
 - Was wurde nicht gelöst
 - Welche Verbesserungen könnten noch gemacht werden
 
**Grafik einbauen**
