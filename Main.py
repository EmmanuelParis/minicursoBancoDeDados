import auth
from DAO import listar_usuarios
from auth import cadastrarMenu, atualizarMenu, removerMenu

while True:
    print("\033[31m----------MENU----------\033[m")
    print("\033[33m[1]\033[m - \033[34mCadastrar Usuário\033[m")
    print("\033[33m[2]\033[m - \033[34mListar Usuários\033[m")
    print("\033[33m[3]\033[m - \033[34mAtualizar Usuário\033[m")
    print("\033[33m[4]\033[m - \033[34mRemover Usuário\033[m")
    print("\033[33m[5]\033[m - \033[34mSair\033[m")
    print("\033[31m------------------------\033[m\n")

    opcao = int(input("\033[33mDigite uma opção: \033[m"))

    if opcao == 1:
        auth.cadastrarMenu()
    elif opcao == 2:
        print(f'\033[36m{listar_usuarios()}\033[m')
    elif opcao == 3:
        atualizarUser = input("\033[33mDigite o nome do usuário que deseja cadastrar: \033[m")
        auth.atualizarMenu(atualizarUser)
    elif opcao == 4:
        deletarUser = input("\033[33mDigite o nome do usuário que deseja remover: \033[m")
        removerMenu(deletarUser)
    else:
        break
