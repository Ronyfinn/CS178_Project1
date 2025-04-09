from flask import Flask, render_template, request, redirect, url_for
import pymysql
import creds
from dbCode import *

app = Flask(__name__)

@app.route("/")
def index():
    source = get_list_of_source()
    return render_template("index.html", results=source)

def get_list_of_source():
    query = "SELECT brand, flavor FROM caffeine_source"
    return execute_query(query)