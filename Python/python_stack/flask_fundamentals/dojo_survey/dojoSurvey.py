from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('survey.html')

@app.route("/survey_results", methods=["POST"])
def results():
    name = request.form["name"]
    email = request.form["email"]
    color = request.form["color"]
    return render_template("survey_results.html", name=name, email=email, color=color)
app.run(debug=True)