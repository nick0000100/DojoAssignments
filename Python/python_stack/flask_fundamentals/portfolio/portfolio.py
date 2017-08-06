from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('project.html')

@app.route('/about')
def about():
    print 'herr'
    return render_template('aboutMe.html')

app.run(debug=True)