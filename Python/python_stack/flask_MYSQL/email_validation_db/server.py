from flask import Flask, render_template, request, redirect, session, flash, url_for
from datetime import datetime
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app,'emails')
app.secret_key = 'hunter2'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

def register():
    query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    data = {
        'email': request.form['email']
    }
    mysql.query_db(query, data)

def getData():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails=emails)

@app.route('/register', methods=["POST"])
def validate():
    email = request.form['email']
    if len(email) <= 0:
        flash("Enter an email")
        return redirect('/')
    elif not EMAIL_REGEX.match(email):
        flash("Not valid email")
        return redirect('/')
    flash("You entered a correct email and it has been added to the database!")
    print "hello"
    register()
    return getData()

app.run(debug=True)