"""
This is mySQL DB connection or model code for datarepresentation using mysql-connector
Written by:     Francis ADEPOJU
Date Completed: December 15, 2019
"""
import mysql.connector
import dbCONFIG as cfg

class CustomerDAO:
    db=""
    def __init__(self):
        # Create the connector object from configuration file dbCONFIG.py
        self.db     = mysql.connector.connect(
        host        = cfg.mySQL['host'], 
        user        = cfg.mySQL['user'], 
        password    = cfg.mySQL['password'],
        database    = cfg.mySQL['database'],
        auth_plugin = cfg.mySQL['auth_plugin']
    )

    def create(self, values):
        # Create a cursor object and insert the record with it
        cursor = self.db.cursor()
        sql = """INSERT INTO customers(firstname,lastname,gender,age,lastvisit,product,amountspent) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM customers"
        cursor.execute(sql)
        result = cursor.fetchall()
        returnArray = []
        print(result)
        for res in result:
            print(res)
            returnArray.append(self.convertToDictionary(res))
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "SELECT * FROM customers WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        # cursor.execute ("UPDATE tblTableName 
        # SET Year=%s, Month=%s, 
        # Day=%s, Hour=%s, Minute=%s WHERE Server='%s' " 
        # % (Year, Month, Day, Hour, Minute, ServerID))
        # (firstname, lastname, gender, age, lastvisit, product, amountspent)
        sql =   """ UPDATE customers     
                    SET firstname=%s, lastname=%s, gender=%s, age=%s, 
                        lastvisit=%s, product=%s, amountspent=%s 
                    WHERE id=%s"""
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql = "DELETE FROM customers WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("deleted...")

    def convertToDictionary(self, result):
        colnames=['id','firstname','lastname', 'gender', 'age','lastvisit','product','amountspent']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

# Instantiate this class
customerDAO = CustomerDAO()








