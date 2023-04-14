from responsavel import Responsavel

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

    def autenticar(self, login: str, senha: str):
        if login not in self._contas:
            return False

        conta = self._contas[login]
        if conta.get_senha() != senha:
            return False
        
        return conta
