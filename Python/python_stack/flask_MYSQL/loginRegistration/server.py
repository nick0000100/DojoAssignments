from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "hunter2"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():






app.run(debug=True)