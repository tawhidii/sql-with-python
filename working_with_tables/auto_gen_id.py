from db import mydb as con

cursor = con.cursor()


def create_table_auto_gen_id():
    cursor.execute("""
    CREATE TABLE users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(50)
    );
    """)
    con.commit()
    con.close()


# create_table_auto_gen_id()


def insert_values_users():
    cursor.execute("""
        INSERT INTO users(username)
            VALUES
                ('bari'),
                ('tawhidi'),
                ('khademul'),
                ('billah'),
                ('tony'),
                ('wong');
    """)
    con.commit()
    con.close()

# insert_values_users()


def create_table_with_fk():
    cursor.execute("""
        CREATE TABLE photos(
            id SERIAL PRIMARY KEY,
            url VARCHAR(50),
            user_id INTEGER REFERENCES users(id)
        );
    """)
    con.commit()
    print('Created !!')
    con.close()

# create_table_with_fk()

def insert_values_to_photos():
    cursor.execute("""
        INSERT INTO photos(url,user_id) 
            VALUES
                ('http://one.jpg',1),
                ('http://two.jpg',6),
                ('http://three.jpg',5),
                ('http://four.jpg',3),
                ('http://five.jpg',3),
                ('http://six.jpg',2),
                ('http://seven.jpg',2),
                ('http://eight.jpg',4),
                ('http://nine.jpg',4);
                
    """)
    con.commit()
    con.close()

insert_values_to_photos()




