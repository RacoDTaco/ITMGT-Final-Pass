from flask import Flask
from flask import render_template
from flask import request
#import database as db
#import os


app = Flask(__name__)

#picFolder=os.path.join('static','pics')


#app.config['UPLOAD_FOLDER']=picFolder


@app.route('/')
def index():
    return render_template('webpages.html', page="Index")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/2auth')
def auth():
    return render_template('2auth.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/event')
def event():
    return render_template('eventpage.html')

@app.route('/mylistings')
def mylistings():
    return render_template('mylistings.html')

@app.route('/mypurchases')
def mypurchases():
    return render_template('mypurchases.html')

@app.route('/selling')
def selling():
    return render_template('selling.html')

