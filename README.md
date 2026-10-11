\# Sistema de Tarefas — API REST



API REST desenvolvida em Python com Flask e SQLite para gerenciamento de tarefas.



\## Funcionalidades



\- Listar todas as tarefas

\- Criar uma nova tarefa

\- Consultar uma tarefa pelo ID

\- Atualizar o título e o status de conclusão de uma tarefa

\- Excluir uma tarefa

\- Validar dados enviados nas requisições

\- Retornar códigos HTTP apropriados para sucesso e erros



\## Tecnologias utilizadas



\- Python

\- Flask

\- SQLite

\- Git e GitHub



\## Como executar o projeto



\### 1. Clonar o repositório



```bash

git clone URL\_DO\_REPOSITORIO

cd Sistema-tarefas

```



Substitua `URL\_DO\_REPOSITORIO` pelo endereço do seu repositório no GitHub.



\### 2. Criar e ativar o ambiente virtual



No Windows, usando o CMD:



```cmd

python -m venv venv

venv\\Scripts\\activate.bat

```



\### 3. Instalar o Flask



```cmd

pip install Flask

```



\### 4. Criar o banco de dados



```cmd

python banco.py

```



\### 5. Iniciar a API



```cmd

python app.py

```



A API estará disponível em:



`http://127.0.0.1:5000`



\## Endpoints



| Método | Rota | Descrição |

|---|---|---|

| GET | `/` | Verificar se a API está funcionando |

| GET | `/tarefas` | Listar todas as tarefas |

| POST | `/tarefas` | Criar uma tarefa |

| GET | `/tarefas/<id>` | Consultar uma tarefa pelo ID |

| PUT | `/tarefas/<id>` | Atualizar uma tarefa |

| DELETE | `/tarefas/<id>` | Excluir uma tarefa |



\## Exemplo de requisição



Criar uma tarefa:



```json

{

"titulo": "Estudar Python"

}

```



A tarefa é criada com um identificador automático e com o status de conclusão inicialmente definido como `0`.



No campo `concluida`:

\- `0` significa que a tarefa não foi concluída.

\- `1` significa que a tarefa foi concluída.



\## Banco de dados



O projeto utiliza SQLite para armazenar as tarefas. A tabela contém os campos `id`, `titulo` e `concluida`.



\## Objetivo



Projeto desenvolvido para praticar desenvolvimento de APIs REST, operações CRUD, persistência de dados, validação de requisições e tratamento de códigos HTTP.



\## Autor



Breno Rodrigues (Estudante de Engenharia de Software).

