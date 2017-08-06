from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "hunter2"

@app.route("/")

def index():
    session["count"] += 1
    return render_template("index.html")

@app.route("/2")

def plus2():
    session["count"] += 2
    return render_template("index.html")

@app.route("/reset")

def reset():
    session["count"] = 1
    return render_template("index.html")

app.run(debug=True)