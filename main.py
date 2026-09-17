import hashlib
import getpass
import json

def menu_inicio():
    print("""
SISTEMA DE USUÁRIOS

1 - Cadastrar usuário
2 - Listar usuários
3 - Buscar usuário
4 - Editar usuário
5 - Excluir usuário
6 - Sair""")

    escolha = int(input("Digite um numero: "))
    return escolha

def menu_cadastro():
    nome = input("Nome: ")
    senha = getpass.getpass(prompt = "Senha: ")
    telefone = input("Telefone: ")
    cidade = input("Cidade: ")

    hash_da_senha = hashlib.sha256(senha.encode("utf-8")).hexdigest()
    
    with open("cadastros.json", "r", encoding="utf-8") as cadastro:
        dados = json.load(cadastro)

        encontrado = False

        for usuario in dados:
            if nome == usuario["nome"]:
                encontrado = True
                break

        if encontrado:
            print("Já existe um usuário com esse nome")
        else:
            novo_cadastro = {
                        "nome": nome,
                        "senha": hash_da_senha,
                        "telefone": telefone,
                        "cidade": cidade
                    }
            dados.append(novo_cadastro)

            with open("cadastros.json", "w", encoding="utf-8") as cadastro:
                json.dump(dados, cadastro, ensure_ascii=False, indent=4)

    input("\nPressione ENTER para continuar...")
     
def menu_listar():
    with open("cadastros.json", "r", encoding="utf-8") as cadastro:
        dados = json.load(cadastro)
        for usuario in dados:
            print(f"\nNome: {usuario['nome']}")    
    input("\nPressione ENTER para continuar...")

def menu_buscar():
    busca = input("\nDigite um nome: ")
    with open("cadastros.json", "r", encoding="utf-8") as cadastro:
        dados = json.load(cadastro)

        encontrado = False

        for usuario in dados:

            if busca == usuario["nome"]:
                print(f"\nNome: {usuario['nome']}")
                print(f"Telefone: {usuario['telefone']}")
                print(f"cidade: {usuario['cidade']}")
                encontrado = True
                break

        if not encontrado:
            print("nenhum usuario com esse nome.")

        input("\nPressione ENTER para continuar...")

def menu_editar():
    perfil = input("Digite o nome de um Usuario para editar as informações dele: ")
    with open("cadastros.json", "r", encoding="utf-8") as cadastro:
            dados = json.load(cadastro)
    
            encontrado = False
    
            for usuario in dados:
                if perfil == usuario["nome"]:
                    user = usuario
                    encontrado = True
                    break
                if not encontrado:
                    print("nenhum usuario com esse nome encontrado")
                    return
                input("\nPressione ENTER para continuar...")
            
    while True:
        print(f"""\nEDITAR USUÁRIO {user['nome']}

1 - Editar Nome
2 - Editar Telefone
3 - Editar Cidade
4 - Sair""")
        opcao = int(input("Digite um numero: "))

        if opcao == 1:
            user["nome"] = input("Escolha outro nome: ")
        elif opcao == 2:
            user["telefone"] = input("Escolha outro Telefone: ")
        elif opcao == 3:
            user["cidade"] = input("Escolha outra cidade: ")
        elif opcao == 4:
            break
        with open("cadastros.json", "w", encoding="utf-8") as cadastro:
            json.dump(dados, cadastro, ensure_ascii=False, indent=4)

def menu_excluir():
    user = input("digite o nome de um usuario para o excluir: ")
    with open("cadastros.json", "r", encoding="utf-8") as cadastro:
        dados = json.load(cadastro)

        encontrado = False

        for usuario in dados:
            if user == usuario["nome"]:
                encontrado = True
                dados.remove(usuario)
                break

        if encontrado:
            with open("cadastros.json", "w", encoding="utf-8") as cadastro:
                    json.dump(dados, cadastro, ensure_ascii=False, indent=4)
            print("Usuário removido com sucesso!")
        else:
            print("\nNenhum usuário com esse nome.")

        input("\nPressione ENTER para continuar...")

try: 
    while True:
        escolha = menu_inicio()
        if escolha == 1:
            menu_cadastro()
        elif escolha == 2:
            menu_listar()
        elif escolha == 3:
            menu_buscar()
        elif escolha == 4:
            menu_editar()
        elif escolha == 5:
            menu_excluir()
        elif escolha == 6:
            break
except ValueError:
    print("Digite apenas numeros")

    