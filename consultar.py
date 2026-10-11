
import sqlite3

conexao = sqlite3.connect("tarefas.db")

tarefas = conexao.execute(
    "SELECT * FROM tarefas"
).fetchall()

for tarefa in tarefas:
    print(tarefa)

conexao.close()
