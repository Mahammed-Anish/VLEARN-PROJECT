import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='anish@123ANISH')
cur = mydb.cursor()

# CREATING DATABASE
cur.execute('create database INVENTORY_MANAGEMENT')
