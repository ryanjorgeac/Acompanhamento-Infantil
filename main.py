import sistema
import menu


def main():
    sys = sistema.Sistema()
    opcoes_iniciais = {
        1: sys.login_menu,
        2: sys.cadastro_menu,
        3: None
    }

    while True:
        menu.print_menu_login()
        opcao = int(input("Digite uma opção: "))
        if opcao not in opcoes_iniciais:
            print("Opção inválida. Digite Novamente.")
        elif opcao == 3:
            break
        opcoes_iniciais[opcao]()


if __name__ == "__main__":
    main()
