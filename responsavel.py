from crianca import Crianca
import menu


class Responsavel:
    def __init__(self, login: str, senha: str):
        self._login = login
        self._senha = senha
        self._filhos: dict[str, Crianca] = dict()

    def get_senha(self):
        return self._senha

    def menu_conta(self):
        while True:
            menu.print_menu_conta()
            opcoes_conta = {
                1: self.registrar_desenvolvimento_menu,
                2: self.cadastrar_filho_menu,
                3: None
            }

            opcao = int(input("Digite uma opção: "))
            if opcao not in opcoes_conta:
                return False
            elif opcao == 3:
                break
            opcoes_conta[opcao]()

    def listar_filhos(self):
        print("Filhos cadastrados: ")
        for nome in self._filhos.keys():
            print("\t" + nome)

    def cadastrar_filho(self, nome, peso, altura, data_nasc, sexo):
        novo_filho = Crianca(nome, peso, altura, data_nasc, sexo)
        self._filhos[nome] = novo_filho
        print("Filho(a) cadastrado com sucesso\n")
        return True

    def cadastrar_filho_menu(self):
        nome_filho = input("Informe o nome do(a) filho(a) a ser cadastrado: ")
        if nome_filho in self._filhos:
            print("Filho já cadastrado\n")
            return False

        peso = float(input("Informe o peso do(a) filho(a) em KG: "))
        altura = int(input("Informe a altura do(a) filho(a) em CM: "))
        data_nascimento = input("Informe a data de nascimento do(a) filho(a) no formato AAAA-MM-DD: ")
        sexo = input("Informe o sexo do(a) filho(a) (M ou F): ")

        return self.cadastrar_filho(nome_filho, peso, altura, data_nascimento, sexo)

    def registrar_desenvolvimento_menu(self):
        self.listar_filhos()
        nome_filho = input("Informe o nome do(a) filho(a): ")
        if nome_filho not in self._filhos:
            return False

        filho = self._filhos[nome_filho]
        nova_altura = int(input("Informe a nova altura do(a) filho(a) em CM: "))
        novo_peso = float(input("Informe o novo peso do(a) filho(a) em KG: "))

        return filho.registrar_evolucao(novo_peso, nova_altura)
