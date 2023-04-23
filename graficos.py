import matplotlib.pyplot as plt

ALTURAS_ATE_2_M = []
ALTURAS_ATE_2_F = []
ALTURAS_ATE_5_M = []
ALTURAS_ATE_5_F = []
ALTURAS_ATE_10_M = []
ALTURAS_ATE_10_F = []
PESOS_ATE_2_M = []
PESOS_ATE_2_F = []
PESOS_ATE_5_M = []
PESOS_ATE_5_F = []
PESOS_ATE_10_M = []
PESOS_ATE_10_F = []
IDADES_ATE_2 = []
IDADES_ATE_5 = []
IDADES_ATE_10 = []


def grafico_altura_ate_2(crianca):
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(8, 5))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.94)

    idades = []
    alturas = []
    for item in crianca.get_desenvolvimento():
        data = list(item.keys())[0]
        idade = crianca.calcular_idade(data)
        altura = list(item.values())[0][1]

        idades.append(idade)
        alturas.append(altura)

    plt.plot(idades, alturas, label=f"Desenvolvimento de {crianca.get_nome()}")

    if crianca.get_sexo() == "M":
        plt.plot(ALTURAS_ATE_2_M, IDADES_ATE_2, label="Desenvolvimento padrão")
    else:
        plt.plot(ALTURAS_ATE_2_F, IDADES_ATE_2, label="Desenvolvimento padrão")

    plt.title("Altura x Idade até 2 anos")
    plt.legend()
    plt.xlabel('Idade (meses)')
    plt.ylabel('Altura (cm)')
    plt.xlim(40, 100)
    plt.ylim(0, 24)
    plt.yticks(range(40, 105, 5))
    plt.xticks(range(0, 25, 1))

    plt.show()


def grafico_altura_ate_5(crianca):
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(8, 5))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.94)

    idades = []
    alturas = []
    for item in crianca.get_desenvolvimento():
        data = list(item.keys())[0]
        idade = crianca.calcular_idade(data)
        altura = list(item.values())[0][1]
        if idade >= 24 and altura >= 75:
            idades.append(idade)
            alturas.append(altura)

    print(idades)
    print(alturas)
    plt.plot(idades, alturas, label=f"Desenvolvimento de {crianca.get_nome()}")

    if crianca.get_sexo() == "M":
        plt.plot(ALTURAS_ATE_5_M, IDADES_ATE_5, label="Desenvolvimento padrão")
    else:
        plt.plot(ALTURAS_ATE_5_F, IDADES_ATE_5, label="Desenvolvimento padrão")

    plt.title("Altura x Idade de 2 a 5 anos")
    plt.legend()
    plt.xlabel('Idade (meses)')
    plt.ylabel('Altura (cm)')
    plt.yticks(range(75, 130, 5))
    plt.xticks(range(24, 61, 2))

    plt.tight_layout()

    plt.show()


def grafico_altura_ate_10(crianca):
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(8, 5))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.94)

    idades = []
    alturas = []
    for item in crianca.get_desenvolvimento():
        data = list(item.keys())[0]
        idade = crianca.calcular_idade(data)
        altura = list(item.values())[0][1]

        idades.append(idade)
        alturas.append(altura)

    plt.plot(idades, alturas, label=f"Desenvolvimento de {crianca.get_nome()}")

    if crianca.get_sexo() == "M":
        plt.plot(ALTURAS_ATE_10_M, IDADES_ATE_10, label="Desenvolvimento padrão")
    else:
        plt.plot(ALTURAS_ATE_10_F, IDADES_ATE_10, label="Desenvolvimento padrão")

    plt.title("Altura x Idade de 5 a 10 anos")
    plt.legend()
    plt.xlabel('Idade (meses)')
    plt.ylabel('Altura (cm)')
    plt.yticks(range(90, 165, 5))
    plt.xticks(range(60, 121, 1))

    plt.show()

def grafico_peso_ate_2(crianca):
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(8, 5))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.94)

    idades = []
    pesos = []
    for item in crianca.get_desenvolvimento():
        data = list(item.keys())[0]
        idade = crianca.calcular_idade(data)
        peso = list(item.values())[0][0]

        idades.append(idade)
        pesos.append(peso)

    plt.plot(idades, pesos, label=f"Desenvolvimento de {crianca.get_nome()}")

    if crianca.get_sexo() == "M":
        plt.plot(PESOS_ATE_2_M, IDADES_ATE_2, label="Desenvolvimento padrão")
    else:
        plt.plot(PESOS_ATE_2_F, IDADES_ATE_2, label="Desenvolvimento padrão")

    plt.title("Peso x Idade até 2 anos")
    plt.legend()
    plt.xlabel('Idade (meses)')
    plt.ylabel('Peso (kg)')
    plt.yticks(range(1, 19, 1))
    plt.xticks(range(0, 25, 1))

    plt.show()

def grafico_peso_ate_5(crianca):
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(8, 5))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.94)

    idades = []
    pesos = []
    for item in crianca.get_desenvolvimento():
        data = list(item.keys())[0]
        idade = crianca.calcular_idade(data)
        peso = list(item.values())[0][0]

        idades.append(idade)
        pesos.append(peso)

    plt.plot(idades, pesos, label=f"Desenvolvimento de {crianca.get_nome()}")

    if crianca.get_sexo() == "M":
        plt.plot(PESOS_ATE_5_M, IDADES_ATE_5, label="Desenvolvimento padrão")
    else:
        plt.plot(PESOS_ATE_5_F, IDADES_ATE_5, label="Desenvolvimento padrão")

    plt.title("Peso x Idade de 2 a 5 anos")
    plt.legend()
    plt.xlabel('Idade (meses)')
    plt.ylabel('Peso (kg)')
    plt.yticks(range(7, 31, 1))
    plt.xticks(range(24, 61, 1))

    plt.show()

def grafico_peso_ate_10(crianca):
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(8, 5))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.94)

    idades = []
    pesos = []
    for item in crianca.get_desenvolvimento():
        data = list(item.keys())[0]
        idade = crianca.calcular_idade(data)
        peso = list(item.values())[0][0]

        idades.append(idade)
        pesos.append(peso)

    plt.plot(idades, pesos, label=f"Desenvolvimento de {crianca.get_nome()}")

    if crianca.get_sexo() == "M":
        plt.plot(PESOS_ATE_10_M, IDADES_ATE_10, label="Desenvolvimento padrão")
    else:
        plt.plot(PESOS_ATE_10_F, IDADES_ATE_10, label="Desenvolvimento padrão")

    plt.title("Peso x Idade de 5 a 10 anos")
    plt.legend()
    plt.xlabel('Idade (meses)')
    plt.ylabel('Peso (kg)')
    plt.yticks(range(15, 65, 5))
    plt.xticks(range(24, 61, 1))

    plt.show()
