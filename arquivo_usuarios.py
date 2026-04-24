import os

arquivo = "./usuarios.txt"

def carregar_usuarios():
    if os.path.exists(arquivo):
        with open(arquivo, "r") as txt:
            return [linha.strip().split(' - ') for linha in txt.readlines() if linha.strip() != ""]
    return []

def salvar_usuarios(usuario):
    with open(arquivo, "a") as txt:
        txt.writelines("\n" + " - ".join(usuario))

def buscar_usuarios(usuarios, cpf):
    for usuario in usuarios:
        if usuario[1] == cpf:
            return usuario
    return None
            
def reescrever_usuarios(usuarios):
    with open(arquivo, "w") as txt:
        txt.writelines("\n" + " - ".join(usuario) for usuario in usuarios)

