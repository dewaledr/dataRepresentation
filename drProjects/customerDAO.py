"""
This is mySQL DB connection or model code for datarepresentation using mysql-connector using connection pooling
Written by:     Francis ADEPOJU
Date Completed: December 15, 2019
"""
import mysql.connector
import dbCONFIG as cfg

class CustomerDAO:
    
    def initConnectToDB(self):
        db = mysql.connector.connect(
            host        = cfg.mySQL['host'], 
            user        = cfg.mySQL['user'], 
            password    = cfg.mySQL['password'],
            database    = cfg.mySQL['database'],
            # auth_plugin = cfg.mySQL['auth_plugin'],
            pool_name='my_connection_pool',
            pool_size=10
        )
        return db
    
    def getConnection(self):
        db = mysql.connector.connect(
            pool_name='my_connection_pool'
        )
        return db
    
    def __init__(self): 
        db = self.initConnectToDB()
        db.close()

    def create(self, values):
        # Create a cursor object and insert the record with it
        db = self.getConnection()
        cursor = db.cursor()
        sql = """INSERT INTO customers(firstname,lastname,gender,age,lastvisit,product,amountspent) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, values)
        db.commit()
        lastRowId = cursor.lastrowid
        db.close()
        return lastRowId

    def getAll(self):
        db  = self.getConnection()
        cursor = db.cursor()
        sql = "SELECT * FROM customers"
        cursor.execute(sql)
        result = cursor.fetchall()
        returnArray = []
        print(result)
        for res in result:
            print(res)
            returnArray.append(self.convertToDictionary(res))
        db.close()
        return returnArray
        

    def findByID(self, id):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "SELECT * FROM customers WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        customer = self.convertToDictionary(result)
        db.close()
        return customer

    def update(self, values):
        db = self.getConnection()
        cursor = db.cursor()
        sql =   """ UPDATE customers     
                    SET firstname=%s, lastname=%s, gender=%s, age=%s, 
                        lastvisit=%s, product=%s, amountspent=%s 
                    WHERE id=%s"""
        cursor.execute(sql, values)
        db.commit()
        db.close()

    def delete(self, id):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "DELETE FROM customers WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        db.commit()
        print("deleted...")
        db.close()

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








