# Importa o módulo sqlite3 e o renomeia como 'lite' para facilitar o uso
import sqlite3 as lite

# Estabelece uma conexão com o banco de dados 'dados.db'.
# Se o arquivo não existir, ele será criado automaticamente.
con = lite.connect('dados.db')

# Criação da tabela 'Categoria'
with con:
    cur = con.cursor()  # Cria um cursor para executar comandos SQL
    cur.execute(
        "CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)"
    )  # Cria a tabela 'Categoria' com dois campos:
       # 'id' como chave primária e 'nome' como texto

# Criação da tabela 'Receitas'
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, "
        "valor DECIMAL)"
    )  # Cria a tabela 'Receitas' com quatro campos:
       # 'id' (chave primária), 'categoria' (texto),
       # 'adicionado_em' (data) e 'valor' (número decimal)

# Criação da tabela 'Gastos'
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, "
        "valor DECIMAL)"
    )  # Cria a tabela 'Gastos' com estrutura semelhante à tabela 'Receitas',
       # mas com a data chamada 'retirado_em' em vez de 'adicionado_em'