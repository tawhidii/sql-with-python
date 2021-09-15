import psycopg2

mydb = psycopg2.connect(database='python_sql',
                        user='barii',
                        password='123456',
                        host='localhost',
                        port='5432')

print('Database connected !!')


