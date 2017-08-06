import random
import datetime
from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = "hunter2"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process_money", methods=["POST"])
def process_money():
    try:
        session["gold"]
    except:
        session["gold"] = 0
    try:
        session["activities"]
    except:
        session["activities"] = []
    dateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.form["building"] == "farm":
        gold = random.randrange(5,21)
        activity = "Earned {} gold from the farm {}".format(str(gold), dateTime)
        session["gold"] += gold
    elif request.form["building"] == "cave":
        gold = random.randrange(5,11)
        activity = "Earned {} gold from the cave {}".format(str(gold), dateTime)
        session["gold"] += gold
    elif request.form["building"] == "house":
        gold = random.randrange(2,6)
        activity = "Earned {} gold from the house {}".format(str(gold), dateTime)
        session["gold"] += gold
    elif request.form["building"] == "casino":
        gold = random.randrange(0,51)
        gomble = random.randint(0,1)
        if gomble == 0:
            session["gold"] += gold
            activity = "Earned {} gold from the casino {}".format(str(gold), dateTime)
        else:
            session["gold"] -= gold
            activity = "Lost {} gold from the casino {}".format(str(gold), dateTime)
    session["activities"].insert(0, activity)
    print session["activities"]
    return redirect(url_for("index"))

@app.route("/reset", methods=["POST"])
def reset():
    try:
        session["gold"]
    except:
        session["gold"] = 0
    try:
        session["activities"]
    except:
        session["activities"] = []
    session.pop("gold")
    session.pop("activities")
    return redirect(url_for("index"))

app.run(debug=True)