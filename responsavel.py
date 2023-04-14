from crianca import Crianca

class Responsavel:
    def __init__(self, login: str, senha: str):
        self._login = login
        self._senha = senha
        self._filhos: dict[str, Crianca] = dict()

    def get_senha(self):
        return self._senha