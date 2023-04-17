from datetime import date


class Crianca:
    def __init__(self, nome, peso_nascimento, altura_nascimento, data_nascimento, sexo):
        self.nome = nome
        self.peso_nascimento = peso_nascimento
        self.altura_nascimento = altura_nascimento
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.registros: dict[date, tuple] = {}

    def registrar_desenvolvimento(self, peso, altura):
        data = date.today()
        self.registros[data] = (peso, altura)
        print("\n**Cadastro de evolução feito com sucesso!**\n")

    def exibir_desenvolvimento(self):
        raise NotImplementedError
