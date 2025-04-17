import boto3
import pymysql
from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from boto3.dynamodb.conditions import Key, Attr
import pymysql
#import creds
from dbCode import *

dynamodb = boto3.resource('dynamodb', region_name = "us-east-1")
users_table = dynamodb.Table('users')
caffeine_logs_table = dynamodb.Table('caffeine_logs')

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)

        users_table.put_item(
            Item={
                "user_id": email,
                "username": username,
                "email": email,
                "password": hashed_password
            }
        )

        flash('User added successfully!', 'success')
        return redirect(url_for('home'))
    else:
        return render_template('add_user.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        response = users_table.get_item(
            Key={
                'user_id': email
            }
        )
        
        user = response.get('Item')

        if user and check_password_hash(user['password'], password):
            session['email'] = email
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'danger')
            return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/delete-user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        email = request.form["email"]

        users_table.delete_item(
            Key={
                'user_id': email
            }
        )

        flash('User deleted successfully', 'danger')

        return redirect(url_for('home'))
    else:
        return render_template('delete_user.html')


'''@app.route("/index.html")
def index():
    source = get_list_of_source()
    return render_template("index.html", results=source)'''

@app.route('/add-log', methods=['GET', 'POST'])
def add_log():
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        caffeine_mg = request.form['caffeine']
        serving_size = request.form['serving_size']
        effect = request.form['effect']
        taste = request.form['taste']
        context = request.form['context']
        brand = request.form['brand']
        flavor = request.form['flavor']
        cost_per_serving = request.form['cost_per_serving']
        cost_per_100mg = request.form['cost_per_100mg']
        email = session['email']

        email = session.get('email')
        if not email:
            flash('You must be logged in to add a log.', 'danger')
            return redirect(url_for('login'))

        query = """
            INSERT INTO caffeine_source (brand, flavor, cost_per_serving, cost_per_100mg)
            VALUES (%s, %s, %s, %s)
        """
        execute_query(query, (brand, flavor, cost_per_serving, cost_per_100mg))

        query = """
            INSERT INTO caffeine_log (user_email, source_id, date, time, caffeine_mg, serving_size, effect, taste, context)
            VALUES (%s, LAST_INSERT_ID(), %s, %s, %s, %s, %s, %s, %s)
        """
        execute_query(query, (
            email, date, time, caffeine_mg, serving_size, effect, taste, context
        ))

        flash('Caffeine log added successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('add_log.html')



@app.route('/display-logs')
def display_user_logs():
    email = session.get('email')
    logs = get_user_table(email)
    return render_template("user_logs.html", results=logs)




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
