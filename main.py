from menu import menu_options
from arquivo_usuarios import carregar_usuarios
from cadastro_usuarios import cadastro_usuario, editar_usuario,busca_usuario, listagem_usuarios

resp = menu_options()
usuarios = carregar_usuarios() 

while resp != 5:
    if resp == 1:
        cadastro_usuario(usuarios)
        resp = menu_options()

    elif resp == 2:
        editar_usuario(usuarios)
        resp = menu_options()

    elif resp == 3:
        busca_usuario(usuarios)
        resp = menu_options()

    elif resp == 4:
        listagem_usuarios(usuarios)
        resp = menu_options()

    else:
        print("Número inválido. Escolha entre 1 e 5!")
        resp = menu_options()

print("Fim!")