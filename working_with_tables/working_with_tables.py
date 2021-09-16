from db import mydb as con
import pandas
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
                ('http://seven.jpg',2);                
    """)
    con.commit()
    con.close()

insert_values_to_photos()


def get_user_image_url():
    
    # getting all data of specific user 
    # query = """
    #     SELECT * FROM photos WHERE user_id =4;
    # """

    # gettings image url data by join 
    query = """
        SELECT username,url FROM photos 
            JOIN users ON users.id = photos.user_id
    """
    data = pandas.read_sql_query(query,con)
    con.close()
    print(pandas.DataFrame.head(data))

# get_user_image_url()




def create_table_with_fk_cascade():
    cursor.execute("""
        CREATE TABLE photos(
            id SERIAL PRIMARY KEY,
            url VARCHAR(50),
            user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
        );
    """)
    con.commit()
    print('Created !!')
    con.close()

# create_table_with_fk_cascade()


def create_table_with_fk_null():
    cursor.execute("""
        CREATE TABLE photos(
            id SERIAL PRIMARY KEY,
            url VARCHAR(50),
            user_id INTEGER REFERENCES users(id) ON DELETE SET NULL
        );
    """)
    con.commit()
    print('Created !!')
    con.close()

# create_table_with_fk_null()