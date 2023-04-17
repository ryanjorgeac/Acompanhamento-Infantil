from responsavel import Responsavel
from getpass import getpass


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
        print("\n**Conta cadastrada com sucesso!**\n")

    def autenticar(self, login: str, senha: str):
        if login not in self._contas:
            return False

        conta = self._contas[login]
        if conta.get_senha() != senha:
            return False

        return conta

    def login_menu(self):
        login = input("Informe o seu nome de usuário: ")
        senha = getpass("Informe a sua senha: ")

        conta = self.autenticar(login, senha)
        if not conta:
            print("\nDados inválidos. Tente novamente.\n")
        else:
            print("\n**Logado com sucesso!**\n")
            conta.menu_conta()

    def cadastro_menu(self):
        login = input("Informe o nome de usuário a ser cadastrado: ")
        senha = getpass("Informe a sua senha: ")

        if login in self._contas:
            print("\nConta já existente.\n")
            return

        return self.cadastrar_conta(login, senha)
