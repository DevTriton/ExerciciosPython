import os
import time
import json
opcao = 1
listaAlunos = []

class Aluno:
    def __init__(self, nome = "", idade = 0, altura = 0.0, peso = 0.0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso


def cadastrarAluno():
    nome = input("digite o nome do aluno: ")
    idade = int(input("Digite a idade: "))
    altura = int(input("Digite a altura: "))
    peso = int(input("Digite a peso: "))
    return Aluno(nome, idade, altura, peso)


def imprimirAlunos():
    print("|Alunos:")
    print("|Nome|Altura|Idade|Peso|")
    print("-------------------------------")
    for a in listaAlunos:
        print(a.nome, "|",a.idade, "|", a.altura, "|", a.peso)
    print("-------------------------------")


def maior65():
    i = 0
    for a in listaAlunos:
        if a.peso > 65:
            i = i+1
    print(f"A quantidade de alunos com mais de 65 kilos é: {i}")

def maispesado():
    i=0
    for a in listaAlunos:
        if a.peso > i:
            i=a.peso
            n=a.nome
    print(f"O aluno mais pesado é {n} com o peso de {i} kilos")    

def menospesado():
    for a in listaAlunos:
        i=a.peso
        if a.peso < i:
            i=a.peso
            n=a.nome
    print(f"O aluno menos pesado é {n} com o peso de {i} kilos")  

def maioridd():
    i = 0
    for a in listaAlunos:
        if a.idade >= 18:
            i = i+1
    print(f"A quantidade de alunos maiores de idade é: {i}")

def qmaioridd():
    i = []
    for a in listaAlunos:
        if a.idade >= 18:
            i.append(a.nome)
    print(f"A quantidade de alunos maiores de idade é: {i}")

def qmenoridd():
    i = []
    for a in listaAlunos:
        if a.idade < 18:
            i.append(a.nome)
    print(f"A quantidade de alunos maiores de idade é: {i}")

def imc(var1, var2) :
  result=var1/(var2*var2)
  if result < 18.5:
      print("abaixo do peso normal")
  elif result > 18.5 and result < 24.9:
      print("Peso Normal")
  elif result > 25.0 and result < 29.9:
      print("Excesso de peso")
  elif result > 30.0 and result < 34.9:
      print("obesidade grau 1")
  elif result > 35.0 and result < 39.9:
      print("obesidade grau 2")
  elif result >= 40.0:
      print("obesidade grau 3")    

def salvar(self):
  dic = {}
  dic["nome"] = self.nome
  dic["idade"] = self.idade
  dic["altura"] = self.altura
  dic["peso"] = self.peso
  texto_json = json.dumps(dic, indent = 3)
  return texto_json
  

def show_menu():
    global opcao
    print("|------------------------------------------------------------|")
    print("|                       OOP PYTHON                           |")
    print("|------------------------------------------------------------|")
    print("")
    print("")
    print("1) Cadastrar Alunos")
    print("2) Imprimir Alunos")
    print("3) Consulta Alunos > 65 Kg:")
    print("4) Aluno mais pesado")
    print("5) Aluno menos pesado")
    print("6) qtd de alunos maiores de idade")
    print("7) quem são os alunos maiores de idade")
    print("8) quem são os alunos menores de idade")
    print("9) calcular imc")
    print("10) salvar em .Json")
    print("11) Sair")
    opcao = int(input("Qual é a sua opção? : "))


while opcao !=11:
    show_menu()

    if opcao == 1:
        os.system("cls")
        time.sleep(1)
        aluno = cadastrarAluno()
        listaAlunos.append(aluno)
        time.sleep(1)
        os.system("cls")

        
    elif opcao == 2:
        os.system("cls")
        time.sleep(1)
        imprimirAlunos()
        time.sleep(1)
        os.system("cls")

        
    elif opcao == 3:
        os.system("cls")
        time.sleep(1)
        maior65()
        time.sleep(1)
        os.system("cls")


    elif opcao == 4:
        os.system("cls")
        time.sleep(1)
        maispesado()
        time.sleep(1)
        os.system("cls")


    elif opcao == 5:
        os.system("cls")
        time.sleep(1)
        menospesado()
        time.sleep(1)
        os.system("cls")


    elif opcao == 6:
        os.system("cls")
        time.sleep(1)
        maioridd()
        time.sleep(1)
        os.system("cls")


    elif opcao == 7:
        os.system("cls")
        time.sleep(1)
        qmaioridd() 
        time.sleep(1)
        os.system("cls")
 

    elif opcao == 8:
        os.system("cls")
        time.sleep(1)
        qmenoridd() 
        time.sleep(1)
        os.system("cls")
  

    elif opcao == 9:
        os.system("cls")
        time.sleep(1)
        imc(int(input("digite o peso do aluno")), float(input("digite a altura do aluno (em metros)")))
        time.sleep(1)
        os.system("cls")


    elif opcao == 10:
        os.system("cls")
        time.sleep(1)
        salvar()
        time.sleep(1)
        os.system("cls")
                       

    elif opcao == 11:
        print("... SAINDO ... ")
        
        exit(0)
