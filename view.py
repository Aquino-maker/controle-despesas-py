# Importa o módulo sqlite3, renomeando como 'lite' para facilitar o uso
import sqlite3 as lite

# Estabelece conexão com o banco de dados 'dados.db'
con = lite.connect('dados.db')

# Função para inserir uma nova categoria na tabela Categoria
def insert_category(item):
    with con:  # Garante que a conexão será usada de forma segura
        cur = con.cursor()  # Cria um cursor para executar comandos SQL
        query = "INSERT INTO Categoria (nome) VALUES (?)"  # Comando SQL com placeholder
        cur.execute(query, (item,))  # Executa a inserção com a tupla (item,)

# Função para inserir uma nova receita na tabela Receitas
# Espera receber uma tupla com (categoria, data, valor)
def insert_income(data):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, (data,))  # Executa a inserção com a tupla data

# Função para inserir um novo gasto na tabela Gastos
# Espera receber uma tupla com (categoria, data, valor)
def insert_expense(data):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos(categoria, retirado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, (data,))  # Executa a inserção com a tupla data

# Função para deletar uma receita da tabela Receitas pelo ID
def delete_income(entry_id):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"  # Deleta o registro com o ID correspondente
        cur.execute(query, (entry_id,))  # Executa o comando com a tupla (entry_id,)

# Função para deletar um gasto da tabela Gastos pelo ID
def delete_expense(entry_id):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, (entry_id,))

# Funções para ver os dados

# Mostrar Categoria
def show_categories():
    item_list = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        rows = cur.fetchall()
        for row in rows:
            item_list.append(row)

    return item_list

# Mostrar Receitas
def show_recipe():
    item_list = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        rows = cur.fetchall()
        for row in rows:
            item_list.append(row)

    return item_list

# Mostrar Gastos
def show_expense():
    item_list = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        rows = cur.fetchall()
        for row in rows:
            item_list.append(row)

    return item_list

