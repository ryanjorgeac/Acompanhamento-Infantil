import sistema


def print_menu_login():
    print('1 - Fazer Login')
    print('2 - Criar conta')
    print('3 - Sair')

def print_menu_conta():
    print('1 - Registrar novo tamanho e peso')
    print('2 - Cadastrar novo filho(a)')
    print('3 - Sair')

def login_menu(system: sistema.Sistema):
    login = input("Informe o seu nome de usuário: ")
    senha = input("Informe a sua senha: ")

    conta = system.autenticar(login, senha)
    if not conta:
        print("Dados inválidos. Tente novamente.")
    else:
        print_menu_conta()


def main():
    sys = sistema.Sistema()
    opcoes_iniciais = {
        1: login_menu,
        2: sys.cadastrar_conta,
        3: exit
    }

    print_menu_login()
    while True:
        opcao = int(input("Digite uma opção: "))
        if opcao in opcoes_iniciais:
            opcoes_iniciais[opcao]()
        else:
            print("Opção inválida. Digite Novamente.")


if __name__ == "__main__":
    main()