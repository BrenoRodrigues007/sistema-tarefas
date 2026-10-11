
from flask import Flask, request
import sqlite3

app = Flask(__name__)


def conectar_banco():
    conexao = sqlite3.connect("tarefas.db")
    conexao.row_factory = sqlite3.Row
    return conexao


@app.route("/")
def inicio():
    return {"mensagem": "API de tarefas funcionando!"}


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    conexao = conectar_banco()

    tarefas = conexao.execute(
        "SELECT * FROM tarefas"
    ).fetchall()

    conexao.close()

    return [dict(tarefa) for tarefa in tarefas]


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()

    if not isinstance(dados, dict):
        return {"erro": "Envie os dados em formato JSON"}, 400

    titulo = dados.get("titulo")

    if not isinstance(titulo, str) or not titulo.strip():
        return {"erro": "O campo titulo é obrigatório"}, 400

    titulo = titulo.strip()

    conexao = conectar_banco()

    cursor = conexao.execute(
        "INSERT INTO tarefas (titulo) VALUES (?)",
        (titulo,)
    )

    conexao.commit()

    tarefa_id = cursor.lastrowid

    conexao.close()

    return {
        "id": tarefa_id,
        "titulo": titulo,
        "concluida": 0
    }, 201



@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    dados = request.get_json()

    if not isinstance(dados, dict):
        return {"erro": "Envie os dados em formato JSON"}, 400

    conexao = conectar_banco()

    tarefa = conexao.execute(
        "SELECT * FROM tarefas WHERE id = ?",
        (id,)
    ).fetchone()

    if tarefa is None:
        conexao.close()
        return {"erro": "Tarefa não encontrada"}, 404

    titulo = dados.get("titulo", tarefa["titulo"])
    concluida = dados.get("concluida", tarefa["concluida"])

    if not isinstance(titulo, str) or not titulo.strip():
        conexao.close()
        return {"erro": "O campo titulo não pode ser vazio"}, 400

    if type(concluida) is not int or concluida not in (0, 1):
        conexao.close()
        return {"erro": "O campo concluida deve ser 0 ou 1"}, 400

    titulo = titulo.strip()

    conexao.execute(
        """
        UPDATE tarefas
        SET titulo = ?, concluida = ?
        WHERE id = ?
        """,
        (titulo, concluida, id)
    )

    conexao.commit()
    conexao.close()

    return {
        "id": id,
        "titulo": titulo,
        "concluida": concluida
    }, 200



@app.route("/tarefas/<int:id>", methods=["GET"])
def buscar_tarefa(id):
    conexao = conectar_banco()

    tarefa = conexao.execute(
        "SELECT * FROM tarefas WHERE id = ?",
        (id,)
    ).fetchone()

    conexao.close()

    if tarefa is None:
        return {"erro": "Tarefa não encontrada"}, 404

    return dict(tarefa), 200


@app.route("/tarefas/<int:id>", methods=["DELETE"])
def excluir_tarefa(id):
    conexao = conectar_banco()

    tarefa = conexao.execute(
        "SELECT * FROM tarefas WHERE id = ?",
        (id,)
    ).fetchone()

    if tarefa is None:
        conexao.close()
        return {"erro": "Tarefa não encontrada"}, 404

    conexao.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (id,)
    )

    conexao.commit()
    conexao.close()

    return {"mensagem": "Tarefa excluída com sucesso"}, 200


if __name__ == "__main__":
    app.run(debug=True)
