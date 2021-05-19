from db import mydb

db_cursor = mydb.cursor(dictionary=True)
# Just feching data 
# db_cursor.execute('SELECT * FROM customers WHERE customer_id=2 ORDER BY first_name')

# fetch data from specific column with some mathmatical operations and give discriptive name
# db_cursor.execute('''SELECT first_name,last_name,
#     points,(points+1)*100 AS
#     'discount factor' FROM customers''')

# avoid dulplicates values 
# db_cursor.execute("""SELECT DISTINCT state FROM customers""")

# Exercise 
db_cursor.execute("""SELECT name,unit_price,(unit_price * 1.1) AS 'new price' FROM products""")

result = db_cursor.fetchall()
for data in result:
    print(data)



