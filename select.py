from db import mydb
import pprint
db_cursor = mydb.cursor(dictionary=True)
# Just feching data (order by)
db_cursor.execute('SELECT * FROM customers WHERE customer_id=2 ORDER BY first_name')

# fetch data from specific column with some mathmatical operations and give discriptive name
db_cursor.execute('''SELECT first_name,last_name,
    points,(points+1)*100 AS
    'discount factor' FROM customers''')

# avoid dulplicates values 
db_cursor.execute("""SELECT DISTINCT state FROM customers""")

# Exercise 
db_cursor.execute("""SELECT name,unit_price,(unit_price * 1.1) AS 'new price' FROM products""")

# Where Claues with comparison operator 
db_cursor.execute("""SELECT * FROM customers WHERE birth_date > '1990-01-01' """)
# Where Exercise 
db_cursor.execute(''' SELECT * FROM orders WHERE order_date >= '2018-01-01' ''')

result = db_cursor.fetchall()
for data in result:
    pprint.pprint(data)



