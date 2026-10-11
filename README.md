# Sistema de Tarefas — API REST

API REST para gerenciamento de tarefas, desenvolvida com Python, Flask e SQLite.

## Funcionalidades

- Listar todas as tarefas
- Criar novas tarefas
- Consultar uma tarefa pelo ID
- Atualizar o título e o status de conclusão
- Excluir tarefas
- Validar os dados recebidos
- Retornar códigos HTTP apropriados

## Tecnologias

- Python
- Flask
- SQLite
- Git e GitHub

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/BrenoRodrigues007/sistema-tarefas.git
cd sistema-tarefas
```

### 2. Criar e ativar o ambiente virtual

No Windows, usando o CMD:

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

### 3. Instalar o Flask

```cmd
pip install Flask
```

### 4. Criar o banco de dados

```cmd
python banco.py
```

### 5. Iniciar a API

```cmd
python app.py
```

A API ficará disponível em `http://127.0.0.1:5000`.

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Verificar se a API está funcionando |
| GET | `/tarefas` | Listar tarefas |
| POST | `/tarefas` | Criar tarefa |
| GET | `/tarefas/<id>` | Consultar tarefa |
| PUT | `/tarefas/<id>` | Atualizar tarefa |
| DELETE | `/tarefas/<id>` | Excluir tarefa |

## Exemplo de criação

Envie uma requisição POST para `/tarefas` com o seguinte JSON:

```json
{
  "titulo": "Estudar Python"
}
```

O campo `concluida` utiliza `0` para tarefas pendentes e `1` para tarefas concluídas.

## Banco de dados

O SQLite armazena as tarefas em uma tabela com os campos `id`, `titulo` e `concluida`. O arquivo do banco de dados é criado pelo script `banco.py`.

## Objetivo

Projeto de portfólio para praticar desenvolvimento de APIs REST, operações CRUD, persistência de dados e validação de requisições.

## Autor

Breno Rodrigues (Estudante de Engenharia de Software).