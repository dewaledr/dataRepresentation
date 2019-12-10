"""
This is mySQL DB connection or model code for datarepresentation using mysql-connector
Written by:     Francis ADEPOJU
Date Completed: December 15, 2019
"""
import mysql.connector
import dbCONFIG as cfg

# Create the connector object
mydb = mysql.connector.connect(
    host        = cfg.mySQL['host'], 
    user        = cfg.mySQL['user'], 
    password    = cfg.mySQL['password'],
    database    = cfg.mySQL['database'],
    auth_plugin = cfg.mySQL['auth_plugin']
)

# Create a cursor object
mycursor = mydb.cursor()
sql = """
    CREATE TABLE customers 
    (id INT AUTO_INCREMENT PRIMARY KEY, `firstname` VARCHAR(50), `lastname` VARCHAR(50), 
    `gender` VARCHAR(1), `age` VARCHAR(7), `lastvisit` VARCHAR(10), `product` VARCHAR(100), `amountspent` DOUBLE) 
    ENGINE=InnoDB AUTO_INCREMENT=20000 DEFAULT CHARSET=latin1"""
mycursor.execute(sql)


