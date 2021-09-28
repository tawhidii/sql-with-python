from db import mydb as conn
import pandas


def example_of_having():
    query = """
    SELECT photo_id,COUNT(*) FROM comments
    WHERE photo_id<3
    GROUP BY photo_id HAVING COUNT(*)>2;
    """
    data = pandas.read_sql_query(query,conn)
    print(data)


example_of_having()


def more_having_example():
    query = """
    SELECT user_id,COUNT(*) FROM comments
    WHERE photo_id < 50
    GROUP BY user_id
    HAVING COUNT(*) > 20;
    """ 

    data = pandas.read_sql_query(query,conn)
    print(data)

more_having_example()


"""
SELECT manufacturer,SUM(price*units_sold)
FROM phones 
GROUP BY manufacturer HAVING SUM(price*units_sold)>2000000;

"""