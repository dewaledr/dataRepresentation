"""
This is mySQL DB connection or model code for datarepresentation using mysql-connector
Written by:     Francis ADEPOJU
Date Completed: December 15, 2019
"""
import mysql.connector
import dbCONFIG as cfg

class CustomerDAO:
    db=""
    db=""
    def connectToDB(self):
        self.db     = mysql.connector.connect(
        host        = cfg.mySQL['host'], 
        user        = cfg.mySQL['user'], 
        password    = cfg.mySQL['password'],
        database    = cfg.mySQL['database'],
        auth_plugin = cfg.mySQL['auth_plugin'])
    
    def __init__(self): 
        self.connectToDB()

    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

    def create(self, values):
        # Create a cursor object and insert the record with it
        cursor = self.getCursor()
        sql = """INSERT INTO customers(firstname,lastname,gender,age,lastvisit,product,amountspent) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.getCursor()
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
        cursor = self.getCursor()
        sql = "SELECT * FROM customers WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.getCursor()
        sql =   """ UPDATE customers     
                    SET firstname=%s, lastname=%s, gender=%s, age=%s, 
                        lastvisit=%s, product=%s, amountspent=%s 
                    WHERE id=%s"""
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.getCursor()
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








