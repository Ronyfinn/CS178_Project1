import boto3
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
        email = request.form['email']

        users_table.delete_item(
            Key={
                'user_id': email
            }
        )

        flash('User deleted successfully', 'danger')

        return redirect(url_for('home'))
    else:
        return render_template('delete_user.html')

@app.route('/display-logs')
def display_logs():
    all_logs = get_user_table()
    return render_template("display_logs.html", results=all_logs)

@app.route('/update-username', methods=['GET', 'POST'])
def update_username():
    if request.method == 'POST':
        try:
            email = request.form['email']
            new_username = request.form['new_username']

            if not email or not new_username: #Need to actually raise error instead of saying "Error" like in MoviesInterface.py
                raise ValueError

            users_table.update_item(
                Key={
                    'user_id': email
                },
                UpdateExpression='SET username = :newname',
                ExpressionAttributeValues={
                    ':newname': new_username
                }
            )

            flash('Username updated successfully!', 'success')
            return redirect(url_for('home'))

        except ValueError:
            flash('Please fill in all fields.', 'warning')
            return redirect(url_for('update_username'))

    return render_template('update_username.html')




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
