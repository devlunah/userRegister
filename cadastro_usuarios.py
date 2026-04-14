from arquivo_usuarios import salvar_usuarios, buscar_usuarios, reescrever_usuarios
from menu import edit_options

def cadastro_usuario(usuarios):
    nome = input("Insira o nome do usuário: ")
    cpf = input("Insira o cpf do usuário: ")
    idade = input("Insira a idade do usuário: ")

    usuario_cadastro = [nome, cpf, idade]
    salvar_usuarios(usuario_cadastro)

    # atualizar a lista salva na memória
    usuarios.append(usuario_cadastro) 

    print("Usuário cadastrado!")
    return usuarios

def editar_usuario(usuarios):
    cpf_busca = input("Insira o CPF do usuário que deseja buscar: ")
    usuario_encontrado = buscar_usuarios(usuarios, cpf_busca)

    if not usuario_encontrado:
        print("Nenhum registro encontrado.")
        return
    
    if usuario_encontrado:
        opcao_editar = edit_options()

        while opcao_editar != 1 and opcao_editar != 2:
            print("Número inválido. Escolha entre 1 e 2!")
            opcao_editar = edit_options()

        if opcao_editar == 1:
            novo_nome = input("Insira o nome: ")
            usuario_encontrado[0] = novo_nome
            
        elif opcao_editar == 2:
            nova_idade = input("Insira a idade: ")
            usuario_encontrado[2] = nova_idade

    # atualizar a lista salva na memória
    for u, usuario in enumerate(usuarios):
        if usuario[1] == cpf_busca:
            usuarios[u] = usuario_encontrado
            break
    
    reescrever_usuarios(usuarios)
    print("Usuário atualizado!")

def busca_usuario(usuarios):
    cpf_busca = input("Insira o CPF do usuário que deseja buscar: ")
    usuario_encontrado = buscar_usuarios(usuarios, cpf_busca)

    if usuario_encontrado:
        print(f"Nome: {usuario_encontrado[0]} | CPF: {usuario_encontrado[1]} | Idade: {usuario_encontrado[2]}")

    if not usuario_encontrado:
        print("Nenhum registro encontrado.")

def listagem_usuarios(usuarios):
    for usuario in usuarios:
        print(f"Nome: {usuario[0]} | CPF: {usuario[1]} | Idade: {usuario[2]}")