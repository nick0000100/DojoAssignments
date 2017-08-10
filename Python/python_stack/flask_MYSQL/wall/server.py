from flask import Flask, render_template, request, redirect, session, flash, url_for
from datetime import datetime
from mysqlconnection import MySQLConnector
import re
import md5
import os, binascii

app = Flask(__name__)
mysql = MySQLConnector(app,'walldb2')
app.secret_key = 'hunter2'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
LETTERS_ONLY = re.compile(r"^[a-zA-Z]+$")

# Navigates to the homepage.
@app.route('/')
def index():
    if session['loggedIn']:
        return redirect('/wall')
    else:
        return render_template('index.html')

# Validates if the given information in the registration form is correct.
def validateNewUser():
    passed = True
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    cPassword = request.form['cPassword']
    if len(first_name) <= 0 or len(last_name) <= 0 or len(email) <= 0 or len(password) <= 0 or len(cPassword) <= 0:
        flash("Missing one or more inputs", "registrationError")
        passed = False
    if cPassword != password:
        flash("Passwords do not match", "registrationError")
        passed = False
    if not EMAIL_REGEX.match(email):
        flash("Not valid email", "registrationError")
        passed = False
    if not LETTERS_ONLY.match(first_name) or not LETTERS_ONLY.match(last_name):
        flash("First or last name contains non-letter character or is empty", "registrationError")
        passed = False
    return passed

# Registers a new user if all of the given data is correct.
# If register fails redirects to homepage with shown errors.
@app.route('/register', methods=['POST'])
def registerNewUser():
    # Returns to login/registration page.
    if not validateNewUser():
        return redirect('/')
    # Add new user to db.
    else:
        # Hash the given password before adding to db.
        salt = binascii.b2a_hex(os.urandom(15))
        password = request.form['password']
        hashed_pw = md5.new(password + salt).hexdigest()
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at, salt) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW(), :salt)"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_pw,
            'salt': salt
        }
        mysql.query_db(query, data) 

        # Create a session for the user
        session['loggedIn'] = True
        session['email'] = request.form['email']
        return redirect('/wall')

# Logs the user in if given correct email and password then redirects to the wall page.
# If log in fails redirects back to home page displaying erros.
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if len(email) <= 0 or len(password) <= 0:
        flash("Email or password not entered", "logInError")
        return redirect('/')
    else:
        query = "SELECT * FROM users WHERE email = :email"
        data = {
            'email': email
        }
        user = mysql.query_db(query, data)
        # Check if the db query returns any information / if person is in the database.
        if user:
            # Check if the password is correct.
            encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
            if user[0]['password'] == encrypted_password:
                session['loggedIn'] = True
                session['email'] = email
                return redirect('/wall')
            else:
                flash("Incorrect password", "logInError")
        flash("Username does not currently exist", "logInError")
    return redirect('/')


@app.route('/wall')
def displayWall():
    if session['loggedIn']:
        messageQuery = "SELECT CONCAT(first_name, ' ', last_name) AS name, message, DATE_FORMAT(messages.created_at, '%M %D %Y') AS created_at, messages.id, messages.users_id FROM messages JOIN users ON messages.users_id = users.id ORDER BY messages.created_at DESC"
        all_messages = mysql.query_db(messageQuery)

        commentQuery = "SELECT CONCAT(first_name, ' ', last_name) AS name, comment, DATE_FORMAT(comments.created_at, '%M %D %Y') AS created_at, messages_id FROM comments JOIN users ON comments.users_id = users.id ORDER BY comments.created_at"
        all_comments = mysql.query_db(commentQuery)

        return render_template("wall.html", all_messages = all_messages, all_comments = all_comments)
    else:
        flash("Log in to see the wall")
        return redirect('/')

# Adds a new message to the database
# Displays message on the wall page.
@app.route('/message', methods=['POST'])
def addMessage():
    message = request.form['message']

    # Gets user id from database.
    idQuery = "SELECT id FROM users WHERE email = '{}'".format(session['email'])
    userId = mysql.query_db(idQuery)[0]['id']

    # Adds message to database
    query = "INSERT INTO messages (users_id, message, created_at, updated_at) VALUES ('{}', '{}', NOW(), NOW())".format(userId, message)
    # data = {
    #     'user_id': userId,
    #     'message': message
    # } find out why it doesnt work "expecting string got an object why does it want a string"
    mysql.query_db(query)
    return redirect('/wall')

# Adds a new message to the database
# Displays message on the wall page.
@app.route('/comment/<message_id>', methods=['POST'])
def addComment(message_id):
    comment = request.form['comment']

    # Gets user id from database.
    idQuery = "SELECT id FROM users WHERE email = '{}'".format(session['email'])
    userId = mysql.query_db(idQuery)[0]['id']

    # Adds message to database
    query = "INSERT INTO comments (messages_id, users_id, comment, created_at, updated_at) VALUES (:message_id, :users_id, :comment, NOW(), NOW())"
    data = {
        'message_id': message_id,
        'users_id': userId,
        'comment': comment
    }

    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)