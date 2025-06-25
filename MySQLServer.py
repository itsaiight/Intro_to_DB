import mysql.connector

try:
   
    mydb = mysql.connector.connect(host= 'localhost', user = 'root', password = 'Gwen2580Sql')

    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print("Error while connecting to MySQL or creating the database:", e)


finally:
    if mydb.is_connected:
        mycursor.close()
        mydb.close()