import sqlite3


def queries(state):

    conn=sqlite3.connect('snowflake.db')

    c=conn.cursor()

    c.execute(f"SELECT * FROM Personas where LastName='{state}'")
    data=c.fetchall()
    conn.close()
    # data = [list(row) for row in data]
    data_to_list=list(data[0])
    data_str = [str(r) for r in data_to_list]
    lista=22
    return data_str