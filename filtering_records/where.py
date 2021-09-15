import psycopg2,pandas
from db import mydb as con

def filter_by_where():
    # query = """
    #     SELECT name,area FROM cities WHERE area <> 3443333;
    # """

    # Between 
    query = """
        SELECT name,area FROM cities WHERE area <> 3443333;
    """
    data = pandas.read_sql_query(query,con)
    con.close()
    print('Successful!!')
    print(pandas.DataFrame.head(data))

# filter_by_where()


def compound_where():
    query = """
        SELECT name,area FROM cities WHERE area BETWEEN 347888 AND 900000 AND name NOT IN('Dhaka','Delhi');
    """
    data = pandas.read_sql_query(query,con)
    con.close()
    print('Successful!!')
    print(pandas.DataFrame.head(data))

compound_where()



