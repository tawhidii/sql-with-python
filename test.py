import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='sql_store'

)

db_cursor= db.cursor()
db_cursor

