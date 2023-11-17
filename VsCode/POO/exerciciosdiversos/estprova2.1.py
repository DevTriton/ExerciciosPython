class funcionario:
    def __init__(self, carteira_TB, nome, cargo, setor,  cracha):
        self.carteira_TB = carteira_TB
        self.nome = nome
        self.cracha = cracha
        self.cargo = cargo
        self.setor = setor
        self.idade = 0
        self.rg = 0
        self.salario = 0
        self.escolaridade = 0
        self.score = 0
    def trabalhar(self):
        print(f"O fúncionario {self.nome} está apto a trabalhar")
    def bater_ponto(self):
        print(f"O fúncionario {self.nome} bateu o ponto")
    
a=funcionario(int(input("digite o número da carteira de trabalho")), 
              input("digite o nome do funcionario"), 
              input("digite o cargo do funcionario"), 
              input("digite o setor do funcionario"), 
              int(input("digite o cracha do funcionario")))
