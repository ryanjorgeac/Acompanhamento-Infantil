from responsavel import Responsavel
import menu


class Sistema:
    def __init__(self):
        self._contas: dict[str, Responsavel] = dict()

    def cadastrar_conta(self, login: str, senha: str) -> bool:
        if login is None:
            return False
        elif senha is None:
            return False
        elif login in self._contas:
            return False
        nova_conta = Responsavel(login, senha)
        self._contas[login] = nova_conta
        print("Conta cadastrada com sucesso!")

    def autenticar(self, login: str, senha: str):
        if login not in self._contas:
            return False

        conta = self._contas[login]
        if conta.get_senha() != senha:
            return False

        return conta

    def login_menu(self):
        login = input("Informe o seu nome de usuário: ")
        senha = input("Informe a sua senha: ")

        conta = self.autenticar(login, senha)
        if not conta:
            print("Dados inválidos. Tente novamente.\n")
        else:
            conta.menu_conta()

    def cadastro_menu(self):
        login = input("Informe o nome de usuário a ser cadastrado: ")
        senha = input("Informe a sua senha: ")

        if login in self._contas:
            print("Conta já existente.\n")
            return

        return self.cadastrar_conta(login, senha)
