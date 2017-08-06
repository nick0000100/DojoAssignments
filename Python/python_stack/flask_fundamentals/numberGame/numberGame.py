import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "hunter2"

@app.route("/")

def index():
    session["number"] = random.randrange(0, 101)
    print session["number"]
    return render_template("index.html")

@app.route("/results", methods=["POST"])

def check():
    guess = int(request.form["guess"])
    number = session["number"]
    print "guess", guess
    print "number", session["number"]
    if guess == number:
        return render_template("results.html", result="Winner")
    elif guess > number:
        return render_template("results.html", result="Too High")
    else:
        return render_template("results.html", result="Too low")

# @app.route("/"):


app.run(debug=True)