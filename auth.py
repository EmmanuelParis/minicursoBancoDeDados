import DAO
from DAO import remover_usuario, buscar_usuario, buscar_id, update_usuario, cadastrar_usuario


def cadastrarMenu():
    nome = input("\033[33mDigite seu nome: \033[m")
    email = input("\033[33mDigite seu email: \033[m")
    senha = input("\033[33mDigite sua senha: \033[m")
    cadastrar_usuario(nome, email, senha)

def atualizarMenu(nome):
    usuario = buscar_usuario(nome)
    id = buscar_id(nome)

    print(f'\033[33mO nome atual é: {nome}\033[m')
    nomeNovo = input("\033[33mDigite o novo nome: \033[m"+'\n')

    print(f'\033[33mO email atual é: {usuario[0][1]}\033[m')
    emailNovo = input("\033[33mDigite o novo email: \033[m"+'\n')

    update_usuario(id, nomeNovo, emailNovo)

def removerMenu(nome):
    id = buscar_id(nome)

    remover_usuario(id)
