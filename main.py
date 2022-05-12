from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

app = Flask("Sports tracker")

@app.route('/')
def hello_world():
    auswertung_link = url_for("auswertung")
    return render_template("index.html", name="Selina", link=auswertung_link, dinger=["Ablauf", "Sportart", "To Do"])

@app.route("/auswertung")
def auswertung():
    return "success"

@app.route('//', methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        return "Vielen Dank für die Datenerfassung."

if __name__ == "__main__":
    app.run(debug=True, port=5000)