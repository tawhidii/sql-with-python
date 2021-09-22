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

# fetch_with_full_join()



def fetch_data_with_join_where():
    query = """
        SELECT contents,url FROM comments
        JOIN photos ON photos.id = comments.photo_id
        WHERE comments.user_id = photos.user_id;
    """
    data = pandas.read_sql_query(query,conn)
    print(data)


# fetch_data_with_join_where()


def example_of_three_way_join():

    query = """
        SELECT contents,url,username FROM comments
        JOIN photos ON photos.id = comments.photo_id
        JOIN users ON  users.id = photos.user_id AND users.id = comments.user_id;
    """
    data = pandas.read_sql_query(query,conn)

    print(data)



# example_of_three_way_join()




#a = """
#SELECT title,name,rating FROM reviews
#JOIN books ON books.id = reviews.book_id JOIN authors ON authors.id = books.author_id AND authors.id = reviews.reviewer_id;
#"""