import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')
# make data
x = np.linspace(0, 24, 24)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots(figsize=(8, 5))  # Altura do gráfico
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1)  # Padding do gráfico

ax.plot([1, 3, 6, 7, 9, 12, 14, 15, 17, 18, 21, 23],
        [45, 53, 55, 66, 68, 70, 75, 83, 85, 92, 95, 100])  # Marcação 1

ax.plot([2, 4, 5, 8, 10, 12, 14, 16, 17, 18, 21, 23],
        [45, 53, 55, 66, 68, 70, 75, 83, 85, 92, 95, 100])  # Marcação 2

ax.set(xlim=(0, 25), xticks=np.arange(0, 25),
       ylim=(40, 105), yticks=np.arange(40, 105, 5))

plt.ylabel('Altura')
plt.xlabel('Idade (Em meses)')

plt.show()


# 1 - Gerenciar Filhos
# 2 - Gerenciar Perfil
#
#
# 1 =
#
# 1 - Cadastrar Filho
# 2 - Alterar Dados
# 3 - Acompanhar Desen. Filho
#
# 3 =
#     Qual filho deseja acompanhar?
#
# 1 - Filho 1
# 2 - Filho 2
#
# 1  = chamar função mostrar_grafico do filho 1
