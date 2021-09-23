from db import mydb as conn
import pandas


def group_by():
    q = """
    SELECT user_id FROM comments GROUP BY user_id;
    """
    data = pandas.read_sql_query(q)

    print(data)



def aggregate():
    """
    Functions Are : 
    SUM()
    AVG()
    MIN()
    MAX()
    """
    q = """
    SELECT SUM(id) FROM comments;
    """
    data = pandas.read_sql_query(q,conn)

    print(data)


# aggregate()


def group_by_with_aggregate():
    q = """
    SELECT user_id , COUNT(id) AS num_comment_created FROM comments GROUP BY user_id;
    """
    data = pandas.read_sql_query(q,conn)
    print(data)


# group_by_with_aggregate()


def group_by_join_aggregate():
    q = """
    SELECT url,COUNT(*) as count_url FROM photos 
    JOIN users ON  users.id = photos.user_id
    JOIN comments ON comments.user_id =photos.user_id
    GROUP BY url;
    """
    data = pandas.read_sql_query(q,conn)
    print(data)
group_by_join_aggregate()

