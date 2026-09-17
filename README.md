# Sistema de Usuários em Python
![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/Data-JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![SHA-256](https://img.shields.io/badge/Security-SHA--256-4CAF50?style=for-the-badge)
Sistema de gerenciamento de usuários desenvolvido em **Python**, utilizando **JSON** para armazenamento dos dados e **SHA-256** para criptografia das senhas.

O projeto permite cadastrar, listar, buscar, editar e excluir usuários através de um menu executado no terminal.

---

## Funcionalidades
os sistema possui as seguintes funcionalidades:

- **Cadastrar usuário**
    - Nome
    - Senha
    - Telefone
    - Cidade
- **Listar usuários cadastrados**
- **Buscar usuário pelo nome**
- **Editar informações do usuário**
    - Nome
    - Telefone
    - Cidade
- **Excluir usuário**
- **Armazenamento da senha utilizando SHA-256**
- **Persistencia de dados usando arquivo JSON**
- **interface através do Terminal**

---

## Tecnologias utilizadas
- **Python 3**
- `json` — armazenamento e leitura dos usuários
- `hashlib` — geração do hash das senhas
- `getpass` — entrada de senha sem exibição no terminal

---

## Estrutura do projeto

```text
sistema-usuarios/
│
├── main.py
├── cadastros.json
└── README.md
```
### `main.py`

Arquivo principal contendo toda a lógica do sistema.

### `cadastros.json`

Arquivo utilizado para armazenar os usuários cadastrados.

Exemplo:

```json
[
    {
        "nome": "Erik",
        "senha": "hash_da_senha",
        "telefone": "99999-9999",
        "cidade": "Pelotas"
    }
]
```

### `README.md`

Documentação do projeto.

---
## Como executar

### 1. Instale o Python

Certifique-se de que o **Python 3** está instalado no computador.

Para verificar:

```bash
python --version
```

ou:

```bash
python3 --version
```

---

### 2. Clone o projeto

```bash
git clone https://github.com/ErikGarciaV/sistema-usuarios.git
```

Entre na pasta:

```bash
cd sistema-usuarios
```

---

### 3. Crie o arquivo `cadastros.json`
Caso o arquivo ainda não exista, crie um arquivo chamado:

```text
cadastros.json
```

E coloque:

```json
[]
```

---

### 4. Execute o programa

```bash
python main.py
```

---

## Menu principal

Ao executar o programa, será exibido:

```text
SISTEMA DE USUÁRIOS

1 - Cadastrar usuário
2 - Listar usuários
3 - Buscar usuário
4 - Editar usuário
5 - Excluir usuário
6 - Sair
```

---

## Cadastro

Ao escolher a opção `1`, o sistema solicita:

```text
Nome:
Senha:
Telefone:
Cidade:
```

A senha não é armazenada diretamente.

Antes de ser salva no arquivo JSON, ela é transformada em um hash SHA-256:

```python
hash = hashlib.sha256(senha.encode("utf-8")).hexdigest()
```

Isso faz com que o arquivo não armazene a senha original.

---

## Busca

A opção `3` permite procurar um usuário pelo nome.

Exemplo:

```text
Digite um nome: Erik

Nome: Erik
Telefone: 99999-9999
cidade: Pelotas
```

---

## Edição

A opção `4` permite selecionar um usuário e alterar suas informações.

```text
EDITAR USUÁRIO Erik

1 - Editar Nome
2 - Editar Telefone
4 - Editar Cidade
5 - Sair
```

A senha não pode ser alterada através desse menu.

---

## Exclusão

A opção `5` permite excluir um usuário pelo nome.

Exemplo:

```text
digite o nome de um usuario para o excluir: Erik

Usuário removido com sucesso!
```

---

## Segurança

O projeto utiliza:

```python
hashlib.sha256()
```

para transformar as senhas em hashes.

Por exemplo:

```text
Senha original:
minhasenha123

Armazenado:
<hash SHA-256>
```

### Observação

Este projeto tem finalidade **educacional**.

---

## Conceitos praticados

Este projeto é útil para praticar conceitos fundamentais de Python:

- Funções
- `while`
- `for`
- Condicionais
- Listas
- Dicionários
- Entrada de dados com `input()`
- Tratamento de erros com `try/except`
- Manipulação de arquivos
- JSON
- Hash de senhas
- Organização de código
- CRUD

### CRUD

O projeto implementa as quatro operações básicas de gerenciamento de dados:

| Operação   | Funcionalidade          |
| ---------- | ----------------------- |
| **Create** | Cadastrar usuário       |
| **Read**   | Listar e buscar usuário |
| **Update** | Editar usuário          |
| **Delete** | Excluir usuário         |

---

## Objetivo do projeto

O objetivo deste projeto é praticar **Python e desenvolvimento de sistemas CRUD**, utilizando persistência de dados em arquivos JSON e conceitos básicos de segurança para armazenamento de senhas.

O projeto também serve como base para evoluir posteriormente para aplicações mais completas utilizando **bancos de dados, APIs, autenticação e interfaces gráficas**.

---

## Autor
**Erik Garcia Vieira**

Desenvolvido como projeto de estudo em Python.

**Tecnologia principal:** Python


