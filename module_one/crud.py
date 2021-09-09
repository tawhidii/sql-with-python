from db import mydb

cursor = mydb.cursor()

# create table 
def create_table():
    cursor.execute('''
        CREATE TABLE cities(
            name VARCHAR(50),
            country VARCHAR(50),
            population INTEGER,
            area INTEGER
        );
    ''')
    print('Table Created !!')
    mydb.commit()
    mydb.close()

# create_table()


# insert value into cities 
def insert_value():
    cursor.execute("""
        INSERT INTO cities(name,country,population,area)
        VALUES 
            ('Dhaka','Bangladesh',2344444,547570),
            ('NewYork','USA',212342442,3443333),
            ('Delhi','India',5454646,74884),
            ('Tokyo','Japan',84874748,547570),
            ('SangHai','China',993883838,33570),
            ('Budapest','Hungery',7838773,47570),
            ('CopenHegen','Denmark',9766466,57570);
         
    """)
    print('Value inserted')
    mydb.commit()
    mydb.close()

# insert_value()

# fetching values 
def fecth_value():
    # fetch all 
    cursor.execute("""
    SELECT * FROM cities;
    """)
    # fetch spefic attrs 
    cursor.execute("""
        SELECT name,country,area FROM cities;
    """)
    rows = cursor.fetchall()
    print(rows)
    mydb.close()

# fecth_value()


# do calculation in rows 
def calculation():
    cursor.execute("""
        SELECT name, population/area AS density FROM cities;
    """)
    rows = cursor.fetchall()
    print(rows)
    mydb.close()

calculation()