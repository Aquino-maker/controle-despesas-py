# Importa o módulo sqlite3, renomeando como 'lite' para facilitar o uso
import sqlite3 as lite

# Estabelece conexão com o banco de dados 'dados.db'
con = lite.connect('dados.db')

# Função para inserir uma nova categoria na tabela Categoria
def inserir_categoria(i):
    with con:  # Garante que a conexão será usada de forma segura
        cur = con.cursor()  # Cria um cursor para executar comandos SQL
        query = "INSERT INTO Categoria (nome) VALUES (?)"  # Comando SQL com placeholder
        cur.execute(query, (i,))  # Executa a inserção com a tupla (i,)

# Função para inserir uma nova receita na tabela Receitas
# Espera receber uma tupla com (categoria, data, valor)
def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, (i,))  # Executa a inserção com a tupla i

# Função para inserir um novo gasto na tabela Gastos
# Espera receber uma tupla com (categoria, data, valor)
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos(categoria, retirado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, (i,))  # Executa a inserção com a tupla i

# Função para deletar uma receita da tabela Receitas pelo ID
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"  # Deleta o registro com o ID correspondente
        cur.execute(query, (i,))  # Executa o comando com a tupla (i,)