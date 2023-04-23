import matplotlib.pyplot as plt


ALTURAS_ATE_2_M = [50, 58, 63, 67, 70, 73, 76, 78, 80, 82, 84, 86, 88]
ALTURAS_ATE_2_F = [49, 57, 62, 65, 69, 71, 74, 76, 78, 81, 83, 85, 86]
ALTURAS_ATE_5_M = [88, 90, 93, 96, 98, 101, 103, 105, 108, 110]
ALTURAS_ATE_5_F = [86, 89, 92, 95, 97, 100, 103, 105, 107, 109]
ALTURAS_ATE_10_M = [110, 113, 116, 119, 122, 125, 127, 130, 132, 135, 138]
ALTURAS_ATE_10_F = [109, 112, 115, 118, 121, 124, 127, 129, 132, 135, 138]
PESOS_ATE_2_M = [3.3, 5.7, 7, 7.9, 8.6, 9.3, 9.8, 10.3, 10.7, 11.1, 11.5, 11.9, 12.2]
PESOS_ATE_2_F = [3.2, 4.8, 6.2, 7.2, 8, 8.6, 9.1, 9.6, 9.9, 10.2, 10.6, 11, 11.5]
PESOS_ATE_5_M = [12.2, 12.8, 13.5, 14.2, 14.8, 15.6, 16.3, 17, 17.7, 18.2]
PESOS_ATE_5_F = [11.5, 12.2, 13, 13.8, 14.5, 15.2, 16, 16.5, 17.5, 18.2]
PESOS_ATE_10_M = [18.2, 19.5, 20.5, 21.9, 23, 24.5, 25.6, 27, 28.4, 29.8, 31]
PESOS_ATE_10_F = [18.2, 19, 20, 21, 22.2, 23.5, 25, 26.5, 28.2, 30, 32]
IDADES_ATE_2 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
IDADES_ATE_5 = [24, 28, 32, 36, 40, 44, 48, 52, 56, 60]
IDADES_ATE_10 = [60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120]


def grafico_altura_ate_2(crianca):
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(12, 6))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.94)

    idades = []
    alturas = []
    for item in crianca.get_desenvolvimento():
        data = list(item.keys())[0]
        idade = crianca.calcular_idade(data)
        altura = list(item.values())[0][1]  # [0][0] Peso e [0][1] Altura

        idades.append(idade)
        alturas.append(altura)

    plt.plot(idades, alturas, label=f"Desenvolvimento de {crianca.get_nome()}")
    plt.scatter(idades, alturas)

    if crianca.get_sexo() == "M":
        plt.plot(IDADES_ATE_2, ALTURAS_ATE_2_M, label="Desenvolvimento padrão", color="green")
    else:
        plt.plot(IDADES_ATE_2, ALTURAS_ATE_2_F, label="Desenvolvimento padrão", color="green")

    plt.title("Altura x Idade até 2 anos")
    plt.legend()
    plt.xlabel('Idade (meses e anos completos)')
    plt.ylabel('Altura (cm)')
    plt.xlim(0, 24)
    plt.ylim(40, 100)
    plt.yticks(range(40, 105, 5))

    marcadores = list(range(0, 25, 1))
    nomes_marcadores = [f"{x // 12} anos" if x % 12 == 0 else x for x in marcadores]
    nomes_marcadores[0] = "Nascimento"
    plt.xticks(marcadores, nomes_marcadores, fontsize=8)
    xticks = plt.xticks()
    for i in range(len(xticks[0])):
        if xticks[0][i] % 12 == 0:
            label = xticks[1][i]  # Acessing label
            position = label.get_position()

            label.set_position((position[0], position[1] - 0.03))
            label.set_fontsize(10)

    plt.tight_layout()
    plt.show()


def grafico_altura_ate_5(crianca):
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(12, 6))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.94)

    idades = []
    alturas = []
    for item in crianca.get_desenvolvimento():
        data = list(item.keys())[0]
        idade = crianca.calcular_idade(data)
        altura = list(item.values())[0][1]  # [0][0] Peso e [0][1] Altura
        if idade >= 24 and altura >= 75:
            idades.append(idade)
            alturas.append(altura)

    plt.plot(idades, alturas, label=f"Desenvolvimento de {crianca.get_nome()}")
    plt.scatter(idades, alturas)

    if crianca.get_sexo() == "M":
        plt.plot(IDADES_ATE_5, ALTURAS_ATE_5_M, label="Desenvolvimento padrão", color="green")
    elif crianca.get_sexo() == "F":
        plt.plot(IDADES_ATE_5, ALTURAS_ATE_5_F, label="Desenvolvimento padrão", color="green")

    plt.title("Altura x Idade de 2 a 5 anos")
    plt.legend()
    plt.xlabel('Idade (meses e anos completos)')
    plt.ylabel('Altura (cm)')
    plt.xlim(24, 60)
    plt.ylim(75, 125)
    plt.yticks(range(75, 130, 5))

    marcadores = list(range(24, 61, 2))
    nomes_marcadores = [f"{x // 12} anos" if x % 12 == 0 else x for x in marcadores]
    plt.xticks(marcadores, nomes_marcadores, fontsize=8)
    xticks = plt.xticks()
    for i in range(len(xticks[0])):
        if xticks[0][i] % 12 == 0:
            label = xticks[1][i]  # Acessing label
            position = label.get_position()

            label.set_position((position[0], position[1] - 0.03))
            label.set_fontsize(10)

    plt.tight_layout()
    plt.show(block=True)


def grafico_altura_ate_10(crianca):
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(12, 6))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.94)

    idades = []
    alturas = []
    for item in crianca.get_desenvolvimento():
        data = list(item.keys())[0]
        idade = crianca.calcular_idade(data)
        altura = list(item.values())[0][1]  # [0][0] Peso e [0][1] Altura
        if idade >= 60 and altura >= 90:
            idades.append(idade)
            alturas.append(altura)

    plt.plot(idades, alturas, label=f"Desenvolvimento de {crianca.get_nome()}")
    plt.scatter(idades, alturas)

    if crianca.get_sexo() == "M":
        plt.plot(IDADES_ATE_10, ALTURAS_ATE_10_M, label="Desenvolvimento padrão", color="green")
    else:
        plt.plot(IDADES_ATE_10, ALTURAS_ATE_10_F, label="Desenvolvimento padrão", color="green")

    plt.title("Altura x Idade de 5 a 10 anos")
    plt.legend()
    plt.xlabel('Idade (meses e anos completos)')
    plt.ylabel('Altura (cm)')
    plt.xlim(60, 120)
    plt.ylim(90, 160)
    plt.yticks(range(90, 165, 5))

    marcadores = list(range(60, 121, 2))
    nomes_marcadores = [f"{x // 12} anos" if x % 12 == 0 else x for x in marcadores]
    plt.xticks(marcadores, nomes_marcadores, fontsize=8)
    xticks = plt.xticks()
    for i in range(len(xticks[0])):
        if xticks[0][i] % 12 == 0:
            label = xticks[1][i]
            position = label.get_position()  # accessing label

            label.set_position((position[0], position[1] - 0.03))
            label.set_fontsize(10)

    plt.tight_layout()
    plt.show()


def grafico_peso_ate_2(crianca):
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(12, 6))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.94)

    idades = []
    pesos = []
    for item in crianca.get_desenvolvimento():
        data = list(item.keys())[0]
        idade = crianca.calcular_idade(data)
        peso = list(item.values())[0][0]  # [0][0] Peso e [0][1] Altura
        if idade <= 24 and peso <= 18:
            idades.append(idade)
            pesos.append(peso)

    plt.plot(idades, pesos, label=f"Desenvolvimento de {crianca.get_nome()}")
    plt.scatter(idades, pesos)

    if crianca.get_sexo() == "M":
        plt.plot(IDADES_ATE_2, PESOS_ATE_2_M, label="Desenvolvimento padrão", color="green")
    else:
        plt.plot(IDADES_ATE_2, PESOS_ATE_2_F, label="Desenvolvimento padrão", color="green")

    plt.title("Peso x Idade até 2 anos")
    plt.legend()
    plt.xlabel('Idade (meses e anos completos)')
    plt.ylabel('Peso (kg)')
    plt.xlim(0, 24)
    plt.ylim(1, 18)
    plt.yticks(range(1, 19, 1))

    marcadores = list(range(0, 25, 1))
    nomes_marcadores = [f"{x // 12} anos" if x % 12 == 0 else x for x in marcadores]
    nomes_marcadores[0] = "Nascimento"
    plt.xticks(marcadores, nomes_marcadores, fontsize=8)
    xticks = plt.xticks()
    for i in range(len(xticks[0])):
        if xticks[0][i] % 12 == 0:
            label = xticks[1][i]  # Acessing label
            position = label.get_position()

            label.set_position((position[0], position[1] - 0.03))
            label.set_fontsize(10)

    plt.tight_layout()
    plt.show()


def grafico_peso_ate_5(crianca):
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(12, 6))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.94)

    idades = []
    pesos = []
    for item in crianca.get_desenvolvimento():
        data = list(item.keys())[0]
        idade = crianca.calcular_idade(data)
        peso = list(item.values())[0][0]  # [0][0] Peso e [0][1] Altura
        if idade >= 24 and peso >= 7:
            idades.append(idade)
            pesos.append(peso)

    plt.plot(idades, pesos, label=f"Desenvolvimento de {crianca.get_nome()}")
    plt.scatter(idades, pesos)

    if crianca.get_sexo() == "M":
        plt.plot(IDADES_ATE_5, PESOS_ATE_5_M, label="Desenvolvimento padrão", color="green")
    else:
        plt.plot(IDADES_ATE_5, PESOS_ATE_5_F, label="Desenvolvimento padrão", color="green")

    plt.title("Peso x Idade de 2 a 5 anos")
    plt.legend()
    plt.xlabel('Idade (meses e anos completos)')
    plt.ylabel('Peso (kg)')
    plt.xlim(24, 60)
    plt.ylim(7, 30)
    plt.yticks(range(7, 31, 1))

    marcadores = list(range(24, 61, 2))
    nomes_marcadores = [f"{x // 12} anos" if x % 12 == 0 else x for x in marcadores]
    plt.xticks(marcadores, nomes_marcadores, fontsize=8)
    xticks = plt.xticks()
    for i in range(len(xticks[0])):
        if xticks[0][i] % 12 == 0:
            label = xticks[1][i]  # Acessing label
            position = label.get_position()

            label.set_position((position[0], position[1] - 0.03))
            label.set_fontsize(10)

    plt.tight_layout()
    plt.show()


def grafico_peso_ate_10(crianca):
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(12, 6))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.94)

    idades = []
    pesos = []
    for item in crianca.get_desenvolvimento():
        data = list(item.keys())[0]
        idade = crianca.calcular_idade(data)
        peso = list(item.values())[0][0]  # [0][0] Peso e [0][1] Altura
        if idade >= 60 and peso >= 10:
            idades.append(idade)
            pesos.append(peso)

    plt.plot(idades, pesos, label=f"Desenvolvimento de {crianca.get_nome()}")
    plt.scatter(idades, pesos)

    if crianca.get_sexo() == "M":
        plt.plot(IDADES_ATE_10, PESOS_ATE_10_M, label="Desenvolvimento padrão", color="green")
    else:
        plt.plot(IDADES_ATE_10, PESOS_ATE_10_F, label="Desenvolvimento padrão", color="green")

    plt.title("Peso x Idade de 5 a 10 anos")
    plt.legend()
    plt.xlabel('Idade (meses e anos completos)')
    plt.ylabel('Peso (kg)')
    plt.xlim(60, 120)
    plt.ylim(10, 60)
    plt.yticks(range(10, 65, 5))

    marcadores = list(range(60, 121, 2))
    nomes_marcadores = [f"{x // 12} anos" if x % 12 == 0 else x for x in marcadores]
    plt.xticks(marcadores, nomes_marcadores, fontsize=8)
    xticks = plt.xticks()
    for i in range(len(xticks[0])):
        if xticks[0][i] % 12 == 0:
            label = xticks[1][i]
            position = label.get_position()  # accessing label

            label.set_position((position[0], position[1] - 0.03))
            label.set_fontsize(10)

    plt.tight_layout()
    plt.show()
