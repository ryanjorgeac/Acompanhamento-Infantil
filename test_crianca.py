import datetime

from crianca import Crianca

def test_calculo_idade_1():
    crianca = Crianca("Ryan", 4, 30, "2023-02-17", "M")
    idade_crianca = crianca.calcular_idade(data=datetime.datetime.now())

    assert idade_crianca == 2
