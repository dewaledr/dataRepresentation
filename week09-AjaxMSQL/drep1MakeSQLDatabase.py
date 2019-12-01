"""
This is mySQL DB connection or model code for datarepresentation using mysql-connector
Written by:     Francis ADEPOJU
Date Completed: December 15, 2019
"""
import mysql.connector

# Create the connector object
mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="root",
    auth_plugin='mysql_native_password')

# Create a cursor object
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE datarepresentation ")

