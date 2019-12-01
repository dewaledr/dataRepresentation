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
    database="datarepresentation",
    auth_plugin='mysql_native_password'
)

# Create a cursor object and insert the record with it
mycursor = mydb.cursor()
# sql = """
# INSERT INTO customers(firstname, lastname, gender, age, lastvisit, product, amountspent ) 
# VALUES (%s, %s, %s, %s, %s, %s, %s)"""
# values = ("Francis", "Adepoju", "M", "67-99", "2019-11-05", "iPhone", 2200.99)
# sql = """
# INSERT INTO customers(firstname, lastname, gender, age, lastvisit, product, amountspent ) 
# VALUES (%s, %s, %s, %s, %s, %s, %s)"""
# values = ("Ann", "Schmitz", "F", "19-25", "2018-02-11", "Blender", 250.55)

# sql = """
# INSERT INTO customers(firstname, lastname, gender, age, lastvisit, product, amountspent ) 
# VALUES (%s, %s, %s, %s, %s, %s, %s)"""
# values = ("Philip", "McGinley", "M", "36-45", "2019-07-28", "Addidas Trainers", 2199.59)

# sql = """
# INSERT INTO customers(firstname, lastname, gender, age, lastvisit, product, amountspent ) 
# VALUES (%s, %s, %s, %s, %s, %s, %s)"""
# values = ("Andrew", "Beatty", "M", "19-25", "2019-08-17", "MacBook Pro 2019", 3599.23)

mycursor.execute(sql, values)
mydb.commit()
print("1 record inserted, ID: ", mycursor.lastrowid)
