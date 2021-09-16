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
    print(pandas.DataFrame.head(data))

fecth_with_join_one()


