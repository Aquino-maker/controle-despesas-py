import sqlite3 as lite

con = lite.connect('dados.db')

def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, (i,))

inserir_categoria("Alimentação")