import sqlite3
import pandas as pd

def queries(state, items):

    conn=sqlite3.connect('snowflake.db')
    c=conn.cursor()
    # c.execute(f"SELECT * FROM Personas where LastName='{state}' or LastName='{items}'")
    # data=c.fetchall()
    # conn.close()
    # data_lista_de_listas = [[[elemento] for elemento in list(tupla)] for tupla in data]
    data_lista_de_listas= pd.read_sql_query(f"SELECT * FROM Personas where LastName='{state}' or LastName='{items}'", conn)

    return data_lista_de_listas

def querie_all(state):

    conn=sqlite3.connect('snowflake.db')
    c=conn.cursor()
    # c.execute(f"SELECT City FROM Personas where LastName='{state}'")
    
    # data_state=c.fetchall()
    # conn.close()
    data_state=pd.read_sql_query(f"SELECT City FROM Personas where LastName='{state}'",conn)
    return data_state

def querie_status(status):

    conn=sqlite3.connect('snowflake.db')
    c=conn.cursor()
    # c.execute(f"SELECT City FROM Personas where LastName='{status}'")
    # data_status=c.fetchall()
    # conn.close()
    data_status=pd.read_sql_query(f"SELECT City FROM Personas where LastName='{status}'", conn)
    return data_status

# c.execute("SELECT * FROM Personas where LastName='espsar'")
# c.execute("UPDATE Personas SET Problema = 'new_email@example.com' WHERE LastName = 'juan' OR LastName= 'azra'")

# data=c.fetchall()

# c.execute("INSERT INTO Personas values ('1','2','3','4','5','6','7','8','9','10')")


# conn.commit()
# conn.close()

# c.execute("ALTER TABLE Personas ADD COLUMN another TEXT")