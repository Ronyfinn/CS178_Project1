from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
#import creds
from dbCode import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_user')
def add_user():
    return render_template('add_user.html')

@app.route("/")
def index():
    source = get_list_of_source()
    return render_template("index.html", results=source)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
