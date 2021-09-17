from db import mydb as conn
import pandas


def fecth_with_join_one():
    query = """
    SELECT username,comments FROM comments 
        JOIN users ON users.id = comments.user_id;
    """
    data = pandas.read_sql_query(query,conn)
    conn.close()
    print('executed!!')
    print(data)

# fecth_with_join_one()


def fecth_with_join_inner():
    query = """
    SELECT url,username FROM photos
        INNER JOIN users ON users.id = photos.user_id;
    """
    data = pandas.read_sql_query(query,conn)
    conn.close()
    print('executed!!')
    print(data)


# fecth_with_join_inner()

def fetch_with_join_left_outer():
    query = """
    SELECT url,username FROM photos
        LEFT JOIN users ON users.id = photos.user_id;
    """
    data = pandas.read_sql_query(query,conn)
    conn.close()
    print('executed !')
    print(data)

# fetch_with_join_left_outer()


def fetch_with_join_right_outer():
    query = """
    SELECT url,username FROM photos
        RIGHT JOIN users ON users.id = photos.user_id;
    """
    data = pandas.read_sql_query(query,conn)
    print(data)

 
# fetch_with_join_right_outer()


def fetch_with_full_join():
    query = """
    SELECT url,username FROM photos
        FULL  JOIN users ON users.id = photos.user_id;
    """
    data = pandas.read_sql_query(query,conn)
    print(data)

fetch_with_full_join()
