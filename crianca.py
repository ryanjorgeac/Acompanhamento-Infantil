import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta
from graficos import grafico_altura_ate_10, grafico_altura_ate_5, grafico_altura_ate_2,\
    grafico_peso_ate_10, grafico_peso_ate_2, grafico_peso_ate_5


class Crianca:
    def __init__(self, nome: str, peso_nascimento: float, altura_nascimento: int, data_nascimento: str, sexo: str):
        self._nome = nome
        self._peso_nascimento = peso_nascimento
        self._altura_nascimento = altura_nascimento
        self._data_nascimento = self.formatar_data(data_nascimento)
        self._sexo = sexo
        self._desenvolvimento = list()
        self._desenvolvimento.append({self._data_nascimento: (peso_nascimento, altura_nascimento)})

    def get_desenvolvimento(self):
        return self._desenvolvimento

    def get_nome(self):
        return self._nome

    def get_sexo(self):
        return self._sexo

    def formatar_data(self, data: str):
        data = data.split("-")
        return datetime(int(data[0]), int(data[1]), int(data[2]))

    def registrar_desenvolvimento(self, peso: float, altura: int, data: str = None):
        data = self.formatar_data(data) if data else datetime.today()
        registro = {data: (peso, altura)}
        self._desenvolvimento.append(registro)
        print("*Cadastro de evolução feito com sucesso!*\n")

    def calcular_idade(self, data: datetime = None):
        data_atual = data or datetime.now()
        print(data_atual)
        diferenca_datas = relativedelta(data_atual, self._data_nascimento)
        print(diferenca_datas)
        idade_meses = diferenca_datas.years * 12 + diferenca_datas.months + diferenca_datas.days / 31
        return round(idade_meses)

    def acompanhar_desenvolvimento_peso(self):
        idade_crianca = self.calcular_idade()
        if idade_crianca <= 24:
            grafico_peso_ate_2(self)
        elif idade_crianca <= 60:
            grafico_peso_ate_5(self)
        else:
            grafico_peso_ate_10(self)

    def acompanhar_desenvolvimento_altura(self):
        idade_crianca = self.calcular_idade()
        print(idade_crianca)
        if idade_crianca <= 24:
            grafico_altura_ate_2(self)
        elif idade_crianca <= 60:
            grafico_altura_ate_5(self)
        else:
            grafico_altura_ate_10(self)


if __name__ == "__main__":
    crianca = Crianca("Ryan", 3, 45, "2020-02-17", 'M')
    crianca.registrar_desenvolvimento(10, 87, "2022-03-17")
    crianca.registrar_desenvolvimento(14, 90, "2022-05-17")
    crianca.registrar_desenvolvimento(18, 92, "2022-08-17")
    crianca.acompanhar_desenvolvimento_altura()