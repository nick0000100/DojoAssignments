from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "hunter2"

@app.route('/')
def index():
    return render_template('survey.html')

@app.route("/survey_results", methods=["POST"])
def results():
    name = request.form["name"]
    email = request.form["email"]
    color = request.form["color"]
    if len(name) <= 0 or len(email) <= 0 or len(color) <= 0:
        flash("Missing one or more fields")
        return redirect('/')
    elif len(name) > 120 or len(email) > 120 or len(color) > 120:
        flash("One or more fields is too long")
        return redirect('/')
    else:
        flash("You completed the form correctly")
    return render_template("survey_results.html", name=name, email=email, color=color)
app.run(debug=True)