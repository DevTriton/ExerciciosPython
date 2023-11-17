import os, time
import json

opcao = 1
listaAlunos = []

class Aluno:

  def __init__(self, idade = 0, altura = 0.0, peso = 0.0, nome = ""):
    self.idade = idade
    self.altura = altura
    self.peso = peso
    self.nome = nome

  def imc(self):
    resultado = self.peso / (self.altura * self.altura)
    if resultado >= 40.0 :
      return "Obesidade classe III"
    elif resultado >= 35.0:
      return "Obesidade classe II"
    elif resultado >= 30.0 :
      return "Obesidade classe I"
    elif resultado >= 25.0:
      return "Excesso de Peso"
    elif resultado >= 18.5:
      return "Peso Normal"
    if resultado < 18.5:
      return "Abaixo do peso normal"

  def Serializar(self):
    dic = {}
    dic["nome"] = self.nome
    dic["idade"] = self.idade
    dic["altura"] = self.altura
    dic["peso"] = self.peso
    texto_json = json.dumps(dic, indent = 3)
    return texto_json

  def Deserializar(self, texto_json):
    dic = json.loads(texto_json)
    #print(dic)
    self.nome = dic["nome"]
    #print(dic["nome"])
    self.idade = dic["idade"]
    #print(dic["idade"])
    self.altura = dic["altura"]
    #print(dic["altura"])
    self.peso = dic["peso"]
    #print(dic["peso"])


def SalvarAlunos():
  lista = []
  arquivo = open("alunos.json", 'w')
  for a in listaAlunos :
    lista.append(a.Serializar())
  json.dump(lista, arquivo)

def RecuperarAlunos():
  listaAlunos.clear()
  arquivo = open("alunos.json", 'r')
  lista_de_jsons_text = json.load(arquivo)
  for text in lista_de_jsons_text:
    dic2 = json.loads(text)
    idade = int(dic2["idade"])
    altura = float(dic2["altura"])
    peso = float(dic2["peso"])
    nome = dic2["nome"]
    listaAlunos.append(Aluno(idade, altura, peso, nome))

def RecuperarAlunos2():
  listaAlunos.clear()
  arquivo = open("alunos.json", 'r')
  lista_de_jsons_text = json.load(arquivo)
  for text in lista_de_jsons_text:
    a = Aluno()
    a.Deserializar(text)
    listaAlunos.append(a)

def cadastrarAluno():
  idade = int(input("Digite a idade:"))
  altura = float(input("Digite a altura:"))
  peso = float(input("Digite a peso:"))
  nome = input("Digite o nome:")
  return Aluno(idade, altura, peso, nome)

def imprimirAlunos():
  print("|Alunos:")
  print("|Nome|Altura|Idade|Peso|")
  print("-------------------------------")
  for a in listaAlunos :
    print(a.nome, "|", a.idade, "|", a.altura, "|", a.peso)
  print("-------------------------------")

def Consulta_Peso():
  contador = 0
  for a in listaAlunos :
    if a.peso > 65:
      contador += 1
  print("Quantidade de alunos > 65 kg eh: ", contador)
  for a in listaAlunos :
    if a.peso > 65:
      print("O aluno ", a.nome, " tem imc: ", a.imc())

def deletar(resp):
  i=0
  while i<len(listaAlunos):
    if resp == listaAlunos[i].nome:
      #index = listaAlunos[i].index(resp)
      #listaAlunos 
      i=i+1

def show_menu():
  global opcao
  print("|############################################################|")
  print("|                        OOP PYTHON                          | ")
  print("|############################################################|")
  print("")
  print("")
  print("1) Cadastrar Alunos")
  print("2) Imprimir Alunos")
  print("3) Consulta Alunos > 65 Kg:")
  print("4) Salvar Alunos:")
  print("5) Recuperar Alunos (v1):")
  print("6) Recuperar Alunos (v2):")
  print("7) deletar um aluno:")
  print("9) Sair")
  opcao = int(input("Qual eh a sua opcao? : "))




while opcao != 9:
  show_menu()

  if opcao==1:
    aluno = cadastrarAluno()
    listaAlunos.append(aluno)
    time.sleep(1)
  elif opcao==2:
    imprimirAlunos()
    time.sleep(1)
  elif opcao == 3:
    Consulta_Peso()
    time.sleep(1)
  elif opcao == 4:
    SalvarAlunos()
    time.sleep(1)
  elif opcao == 5:
    RecuperarAlunos()
    time.sleep(1)
  elif opcao == 6:
    RecuperarAlunos2()
    time.sleep(1)
  elif opcao == 7:
    deletar(input("digite o nome do aluno que deseja remover"))
    time.sleep(1)
  elif opcao == 9:
    print("... SAINDO ... ")
    exit(0)