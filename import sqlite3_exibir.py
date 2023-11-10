import sqlite3

def exibir_dados_do_banco():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    dados = cursor.fetchall()
    conn.close()

    for linha in dados:
        print(linha)

exibir_dados_do_banco()