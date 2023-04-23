from sistema import Sistema
from menu import print_menu_login


def main():
    sys = Sistema()
    opcoes_iniciais = {
        1: sys.login_menu,
        2: sys.cadastro_menu,
        3: None
    }
    print("*** Bem-vindo ao Sistema de Acompanhamento Infantil ***\n")

    while True:
        print_menu_login()
        try:
            opcao = int(input("Digite uma opção: "))
        except ValueError:
            print("\nOpção inválida. Digite novamente.")
            continue

        if opcao not in opcoes_iniciais:
            print("\nOpção inválida. Digite Novamente.")
            continue
        elif opcao == 3:
            print("Saindo...")
            break
        opcoes_iniciais[opcao]()


if __name__ == "__main__":
    main()
