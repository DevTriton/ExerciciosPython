class Pessoa:
  def __init__(self, nome, idade, altura, peso):
    self.nome = nome
    self.idade = idade
    self.altura = altura
    self.peso = peso

  def ImprimirNome(self):
    print(self.nome)  

class Estudante(Pessoa):
  def __init__(self, nome, idade, altura, peso, rgm):
    super(Pessoa).__init__(nome, nome, idade, altura, peso)
    self.rgm = rgm

class Professor(Pessoa):
  def __init__(self, nome, idade, altura, peso, matricula):
    super().__init__(nome, nome, idade, altura, peso)
    self.matricula = matricula

s = Estudante("jose", "16", "1.86", "100", "40028922")
s.ImprimirNome()