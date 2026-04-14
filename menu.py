def menu_options():
    print("----------------------------")
    print("1 - Cadastrar usuário")
    print("2 - Editar usuário")
    print("3 - Buscar usuário")
    print("4 - Listar todos os usuários")
    print("5 - Sair")

    resposta = int(input("Escolha uma opção de 1 - 5: "))

    return resposta

def edit_options():
    print("Opções de Escolha: ")
    print("1 - Editar Nome")
    print("2 - Editar Idade")

    resposta_edit = int(input("Escolha uma opção de 1 - 2: "))
    return resposta_edit