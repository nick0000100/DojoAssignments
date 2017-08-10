from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = "hunter2"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/turtle", methods=["POST"])
def turtle():
    return redirect("/")

app.run(debug=True)