from flask import Flask, render_template, request, redirect, flash, session
import re
app = Flask(__name__)
app.secret_key = "sdfijsdo"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
LETTERS_ONLY = re.compile(r"^[a-zA-Z]$")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    # Takes all of the inputs from the form
    fname = request.form["fname"]
    lname = request.form["lname"]
    email = request.form["email"]
    password = request.form["password"]
    cpassword = request.form["cpassword"]

    # Checks to see if inputs are valid

    if len(fname) <= 0 or len(lname) <= 0 or len(email) <= 0 or len(email) <= 0 or len(password) <=0 or len(cpassword) <= 0:
        flash("Missing one or more fields")
    if len(password) < 8:
        flash("Password is not long enough")
    elif password != cpassword:
        flash("Password confirmation did not match")
    if not EMAIL_REGEX.match(email):
        flash("Not valid email")
    if not LETTERS_ONLY.match(fname) or not LETTERS_ONLY.match(lname):
        flash("Not valid name")

    return redirect("/")

app.run(debug=True)