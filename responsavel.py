from crianca import Crianca
import menu


class Responsavel:
    def __init__(self, login: str, senha: str):
        self._login = login
        self._senha = senha
        self._filhos: dict[str, Crianca] = dict()

    def __str__(self):
        return f"{self._login}&{self._senha}"

    def get_senha(self):
        return self._senha

    def get_filhos(self):
        return self._filhos

    def menu_conta(self):
        while True:
            menu.print_menu_conta()
            opcoes_conta = {
                1: self.registrar_desenvolvimento_menu,
                2: self.cadastrar_filho_menu,
                3: self.exibir_desenvolvimento_menu,
                4: None
            }

            try:
                opcao = int(input("Digite uma opção: "))
            except ValueError:
                print("\nOpção inválida. Digite novamente.")
                continue
            if opcao not in opcoes_conta:
                return False
            elif opcao == 4:
                break
            opcoes_conta[opcao]()

    def listar_filhos(self):
        print("\nFilhos cadastrados: ")
        for nome in self._filhos.keys():
            print("\t" + nome)
        print('\n')

    def cadastrar_filho(self, nome, peso, altura, data_nasc, sexo):
        novo_filho = Crianca(nome, peso, altura, data_nasc, sexo)
        self._filhos[nome] = novo_filho
        print("\nFilho(a) cadastrado com sucesso\n")
        return True

    def cadastrar_filho_menu(self):
        nome_filho = input("Informe o nome do(a) filho(a) a ser cadastrado: ")
        if nome_filho in self._filhos:
            print("\nFilho já cadastrado\n")
            return False

        peso = float(input("Informe o peso do(a) filho(a) em KG: "))
        altura = int(input("Informe a altura do(a) filho(a) em CM: "))
        data_nascimento = input("Informe a data de nascimento do(a) filho(a) no formato AAAA-MM-DD: ")
        sexo = input("Informe o sexo do(a) filho(a) (M ou F): ").upper()

        return self.cadastrar_filho(nome_filho, peso, altura, data_nascimento, sexo)

    def registrar_desenvolvimento_menu(self):
        if len(self._filhos) == 0:
            print("\nNão há filhos cadastrados\n")
            return False

        self.listar_filhos()
        nome_filho = input("Informe o nome do(a) filho(a): ")
        if nome_filho not in self._filhos:
            print("\nFilho(a) não cadastrado.\n")
            return False

        filho = self._filhos[nome_filho]
        novo_peso = float(input("Informe o novo peso do(a) filho(a) em KG: "))
        nova_altura = int(input("Informe a nova altura do(a) filho(a) em CM: "))
        data_registro = input("Quando foi medido? (AAAA-MM-DD): ")

        return filho.registrar_desenvolvimento(novo_peso, nova_altura, data_registro)

    def exibir_desenvolvimento_menu(self):
        if len(self._filhos) == 0:
            print("\nNão há filhos cadastrados\n")
            return False

        self.listar_filhos()
        nome_filho = input("Informe o nome do(a) filho(a): ")
        if nome_filho not in self._filhos:
            print("\nFilho(a) não cadastrado.\n")
            return False

        filho = self._filhos[nome_filho]
        opcao = input("Deseja acompanhar o desenvolvimento pela altura ou pelo peso? ")
        if opcao.lower() == "altura":
            return filho.acompanhar_desenvolvimento_altura()
        else:
            return filho.acompanhar_desenvolvimento_peso()
