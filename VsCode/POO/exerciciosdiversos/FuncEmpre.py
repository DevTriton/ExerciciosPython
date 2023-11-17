lista=[]
class funcionario:
    def __init__(self, nome, data_nasc, CT, setor, salario, HT):
        self.nome = nome
        self.data_nasc = data_nasc
        self.CT = CT
        self.setor = setor
        self.salario = salario
        self.HT = HT
    def trabalhar(self):
        print(f"o funcionario {self.nome} esta apto á trabalhar ")
    def entrar(self):
        print(f"O funcionario {self.nome} bateu o ponto de entrada ")
    def sair(self):
        print(f"O funcionario {self.nome} bateu o ponto de saida")

class empresa:
    def __init__(self, CNPJ, CEP, proprietario, razaosocial, Lm, DT):
        self.CNPJ = CNPJ
        self.CEP = CEP
        self.proprietario = proprietario
        self.razaosocial = razaosocial
        self.Lm = Lm
        self.DT = DT
    def contratar(self):
        lista.append(funcionario.nome)
        print(f"A empresa contratou os funcionarios: {lista}")
    def demitir(self):
        print(f"A empresa demitiu um total de {self.DT} funcionarios esse mês")

a=funcionario("eddie", "26/10/2004", 123123, 1, 1.200, 8)
a.trabalhar()
a.entrar()
a.sair()
