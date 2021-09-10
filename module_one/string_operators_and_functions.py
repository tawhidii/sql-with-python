import psycopg2,pandas
from db import mydb as con

def string_functions():
    # concat with operators
    # query = """
    #     SELECT name || ', ' || country AS details FROM cities;
    # """
    # Implementaions of Functions 
    query = """
        SELECT UPPER(CONCAT(name,', ',country)) AS details FROM cities;
    """
    data = pandas.read_sql_query(query,con)
    con.close()
    print('Successful!!')
    print(pandas.DataFrame.head(data))

string_functions()