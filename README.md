# Caffiene Tracker Web App

## What The Project Does
The premise of this web application is for users to be able to track their daily caffeine intake, primarily targeted towards gym goers. But is available, easy to access, and useful for everyone. Users can create an account, delete an account, update their username, display their caffeine log, and login. Focusing on the general CRUD format.e hashed This web application utilizes a backend supported by **AWS**, **DynamoDB**, and an **RDS in AWS**. But is supported throught the use of **Flask**. It should be noted that passwords stored in **DynamoDB** are hashed, giving more security.

## Why This Project is Useful
This project allows users to track not only their caffeine consumption in an organized fasion, but also allows users to view key insights in their habits. Such as the source of where the caffeine is coming from, taste rating, effect rating
amount of dollars per serving, etc. This allows user to analyze trends such as which caffeine source effects them the most, if their taste is consistent, thus which source/brand/flavor tastes the best, how much money they spend, and more.

## How to Get Started
*_ clone the repository _*
git clone https://github.com/Ronyfinn/CS178_Project1
and then proceed to cd into where the file is stored
For this, I recommend using a git terminal, as that is what worked best for me, but whichever works best for you should be used.

*_ install dependencies_*
there might be a few dependencies that you need to install which you should install

*_ Condifigure AWS_*
Set up AWS credentials using the AWS CLI or an IAM user.
Create a **DynamoDB** table called `users` with `user_id` as the primary key.
Create a **MySQL RDS instance** and configure the caffeine logs table.

*_ Edit your database connection in `dbCode.py` _*:
    Code should look like this to hard code:
    ```python
    connection = pymysql.connect(
        host='your-rds-endpoint',
        user='your-db-username',
        password='your-db-password',
        db='your-db-name'
    )
    ```

  *_ Run Flaskapp _*:
    ```bash
    python3 flaskapp.py
    ```

    *_ Visit webpage _*

##👨‍💻 Who Maintains and Contributes to the Project

This project was created by **Rony Finney**, student at Drake University for the CS178: Big Data course. Contributions are welcome.
