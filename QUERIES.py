import sqlite3

def queries(state, items):

    conn=sqlite3.connect('snowflake.db')

    c=conn.cursor()
    c.execute(f"SELECT * FROM Personas where LastName='{state}' or LastName='{items}'")
    # c.execute("SELECT * FROM Personas")
    data=c.fetchall()
    conn.close()

    data_lista_de_listas = [[[elemento] for elemento in list(tupla)] for tupla in data]

    return data_lista_de_listas

def querie_all(state):

    conn=sqlite3.connect('snowflake.db')

    c=conn.cursor()
    c.execute(f"SELECT City FROM Personas where LastName='{state}'")

    data_state=c.fetchall()
    conn.close()

    return data_state

# c.execute("SELECT * FROM Personas where LastName='espsar'")
# c.execute("UPDATE Personas SET Problema = 'new_email@example.com' WHERE LastName = 'juan' OR LastName= 'azra'")

# data=c.fetchall()

# c.execute("INSERT INTO Personas values ('1','2','3','4','5','6','7','8','9','10')")


# conn.commit()
# conn.close()

# c.execute("ALTER TABLE Personas ADD COLUMN another TEXT")