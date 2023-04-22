import datetime
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt


class Crianca:
    def __init__(self, nome, peso_nascimento, altura_nascimento, data_nascimento, sexo):
        self.nome = nome
        self.peso_nascimento = peso_nascimento
        self.altura_nascimento = altura_nascimento
        self.data_nascimento = self.formatar_data(data_nascimento)
        self.sexo = sexo
        self._desenvolvimento = []

    def formatar_data(self, data: str):
        data = data.split("-")
        return date(int(data[0]), int(data[1]), int(data[2]))

    def registrar_evolucao(self, peso, altura):
        data = date.today()
        registro = {"data": str(data), "peso": peso, "altura": altura}
        self._desenvolvimento.append(registro)
        print("*Cadastro de evolução feito com sucesso!*\n")

    def calcular_idade(self, data=None):
        data_atual = data or datetime.now()
        diferenca_datas = relativedelta(data_atual, self.data_nascimento)
        idade_meses = diferenca_datas.years * 12 + diferenca_datas.months + diferenca_datas.days / 31
        return round(idade_meses)

    def plotar_grafico(self):
        plt.style.use('_mpl-gallery')
        fig, ax = plt.subplots(figsize=(8, 5))  # Altura do gráfico
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1)  # Padding do gráfico

        x = [datetime.datetime.strptime(registro['data'], '%Y-%m-%d') for registro in self._desenvolvimento]
        y = [registro['altura'] for registro in self._desenvolvimento]
        plt.scatter(x, y)
        plt.title(f"Desenvolvimento de altura de {self.nome}")
        plt.xlabel('Idade (meses completos e anos)')
        plt.ylabel('Altura (cm)')
        plt.show()
        print(x)
        print(y)


if __name__ == "__main__":
    crianca = Crianca("Ryan", 4, 30, "2003-02-17", "M")
    crianca.registrar_evolucao(8, 35)
    crianca.registrar_evolucao(10, 40)
    crianca.registrar_evolucao(14, 47)
    crianca.registrar_evolucao(18, 52)
    crianca.plotar_grafico()