import json
listaAlunos = []
opcao=1

class Aluno:
    def __init__(self, nome = "", idade = 0, altura = 0.0, peso = 0.0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

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

    
def menu():
    global opcao
    print("Oque deseja fazer?")
    print("1) Cadastrar Aluno")
    print("2) Imprimir Alunos")
    print("3) Consulta Alunos > 65 Kg:")
    print("4) Aluno mais pesado")
    print("5) Aluno menos pesado")
    print("6) qtd de alunos maiores de idade")
    print("7) quem são os alunos maiores de idade")
    print("8) quem são os alunos menores de idade")
    print("9) calcular imc")
    print("10) salvar em .Json")
    print("11) Recuperar Alunos")
    print("12) Sair")
    opcao=int(input("digite a opção que deseja fazer: "))
   
def cadastrar():
    nome = input("digite o nome do aluno: ")
    idade = int(input("digite a idade do aluno: "))
    altura = float(input("digite a altura do aluno (metros): "))
    peso = float(input("digite o peso do aluno: "))
    return Aluno(nome, idade, altura, peso)

def imprimir():
    print("----------------------------------------")
    for cont in listaAlunos:
        print(cont.nome, "/", cont.idade, "/", cont.altura, "/", cont.peso)
    print("----------------------------------------")

def consultar65():
    i=0
    for cont in listaAlunos:
        if cont.peso>65:
            i=i+1
    print(f"a quantidade de alunos com mais de 65kg são {i}")

def maisp():
    i=0
    j=""
    for cont in listaAlunos:
        if cont.peso>i:
            i=cont.peso
            j=cont.nome
    print(f"o aluno mais pesado é: {j}") 

def menosp():
    j=""
    i=500
    for cont in listaAlunos:
        if cont.peso<i:
            i=cont.peso
            j=cont.nome
    print(f"o aluno menos pesado é: {j}")

def qtdmaior():
    i=0
    for cont in listaAlunos:
        if cont.idade>=18:
            i=i+1
    print(f"A quantidade de alunos maiores de idade é {i}")        

def qmaior():
    i=[]
    for cont in listaAlunos:
        if cont.idade>=18:
            i.append(cont.nome)
    print(f"o alunos maiores de idade são {i}")  

def qmenor():
    i=[]
    for cont in listaAlunos:
        if cont.idade<18:
            i.append(cont.nome)
    print(f"o alunos menores de idade são {i}")  

def imc():
        i=""
        resp=input("digite o nome do aluno: ")
        for cont in listaAlunos:
            if cont.nome == resp:
                resultado = cont.peso / (cont.altura * cont.altura)
            if resultado < 18.5:
                i="abaixo do peso normal"
            elif resultado > 18.5 and resultado < 24.9:
                i = "Peso Normal"
            elif resultado > 25.0 and resultado < 29.9:
                i="Excesso de peso"
            elif resultado > 30.0 and resultado < 34.9:
                i="obesidade grau 1"
            elif resultado > 35.0 and resultado < 39.9:
                i="obesidade grau 2"
            elif resultado >= 40.0:
                i="obesidade grau 3"    
        print(f"o imc desse aluno é {resultado} é a situação dele é {i}") 

def SalvarAlunos():
  lista = []
  arquivo = open("alunos.json", 'w')
  for cont in listaAlunos :
    lista.append(cont.Serializar())
  json.dump(lista, arquivo) 

def RecuperarAlunos():
  listaAlunos.clear()
  arquivo = open("alunos.json", 'r')
  lista_de_jsons_text = json.load(arquivo)
  for text in lista_de_jsons_text:
    a = Aluno()
    a.Deserializar(text)
    listaAlunos.append(a)

def Excluir():
    resp=input("digite o nome do aluno que deseja excluir: ")
    for cont in listaAlunos:
        if cont.nome == resp:
            listaAlunos.pop[0, 1, 2, 3]    
    
while opcao != 14:
    menu() 
    
    if opcao==1:
        aluno = cadastrar()
        listaAlunos.append(aluno)
    elif opcao==2:
        imprimir()
    elif opcao==3:
        consultar65()
    elif opcao==4:
        maisp() 
    elif opcao==5:
        menosp() 
    elif opcao==6:
        qtdmaior() 
    elif opcao==7:
        qmaior() 
    elif opcao==8:
        qmenor() 
    elif opcao==9:
        imc()
    elif opcao==10:
        SalvarAlunos()
    elif opcao==11:
        RecuperarAlunos()
    elif opcao==12:
        Excluir()
    elif opcao==13:
        break                               
