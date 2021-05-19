import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='sql_store'

)

db_cursor= db.cursor()
db_cursor.execute('SHOW DATABASES') # will get all databases

for d in db_cursor:
    print(d) # list all databases

