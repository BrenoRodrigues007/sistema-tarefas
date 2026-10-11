import sqlite3

conexao = sqlite3.connect("tarefas.db")

conexao.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        concluida INTEGER NOT NULL DEFAULT 0
    )
""")

conexao.commit()
conexao.close()

print("Banco de dados e tabela criados com sucesso!")
