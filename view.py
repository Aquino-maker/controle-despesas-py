import sqlite3 as lite

con = lite.connect('dados.db')

def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, (i,))

def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, (i,))

def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos(categoria, retirado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, (i,))