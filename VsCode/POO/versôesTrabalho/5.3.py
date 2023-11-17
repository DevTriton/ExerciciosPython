import json

class ModuloAcademico:
    def __init__(self):
        self.listaAlunos = []
        self.opcao = 1
        self.ct = 0
        self.index = 0
    
    def menu(self):
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
        print("12) excluir um aluno")
        print("13) Sair")
        self.opcao=int(input("digite a opção que deseja fazer: "))
    
    def cadastrar(self):
        nome = input("digite o nome do aluno: ")
        idade = int(input("digite a idade do aluno: "))
        altura = float(input("digite a altura do aluno (metros): "))
        peso = float(input("digite o peso do aluno: "))
        ID = int(input("digite o numero id desse aluno"))
        return Aluno(nome, idade, altura, peso, ID)

    def imprimir(self):
        print("----------------------------------------")
        for cont in self.listaAlunos:
            print(cont.nome, "/", cont.idade, "/", cont.altura, "/", cont.peso, "/", cont.ID)
        print("----------------------------------------")

    def consultar65(self):
        i=0
        for cont in self.listaAlunos:
            if cont.peso>65:
                i=i+1
        print(f"a quantidade de alunos com mais de 65kg são {i}")

    def maisp(self):
        i=0
        j=""
        for cont in self.listaAlunos:
            if cont.peso>i:
                i=cont.peso
                j=cont.nome
        print(f"o aluno mais pesado é: {j}") 

    def menosp(self):
        j=""
        i=500
        for cont in self.listaAlunos:
            if cont.peso<i:
                i=cont.peso
                j=cont.nome
        print(f"o aluno menos pesado é: {j}")

    def qtdmaior(self):
        i=0
        for cont in self.listaAlunos:
            if cont.idade>=18:
                i=i+1
        print(f"A quantidade de alunos maiores de idade é {i}")        

    def qmaior(self):
        i=[]
        for cont in self.listaAlunos:
            if cont.idade>=18:
                i.append(cont.nome)
        print(f"o alunos maiores de idade são {i}")  

    def qmenor(self):
        i=[]
        for cont in self.listaAlunos:
            if cont.idade<18:
                i.append(cont.nome)
        print(f"o alunos menores de idade são {i}")  

    def imc(self):
            i=""
            resp=input("digite o nome do aluno: ")
            for cont in self.listaAlunos:
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

    def SalvarAlunos(self):
        lista = []
        arquivo = open("alunos.json", 'w')
        for cont in self.listaAlunos :
            lista.append(cont.Serializar())
        json.dump(lista, arquivo) 

    def RecuperarAlunos(self):
        self.listaAlunos.clear()
        arquivo = open("alunos.json", 'r')
        lista_de_jsons_text = json.load(arquivo)
        for text in lista_de_jsons_text:
            a = Aluno()
            a.Deserializar(text)
            self.listaAlunos.append(a)

    def RemoverAluno(self):
        resp = input("digite o nome do aluno: ")
        #self.ct = self.ct - 1
        
        
        for cont in self.listaAlunos:
            if resp == cont.nome:
                index = cont.ID - 1
                self.listaAlunos.pop(index)
        for cont in self.listaAlunos:
            if cont.ID > index:
                cont.ID = cont.ID - 1        
    
    def Executar(self):
        while self.opcao != 13:
            self.menu() 
            
            if self.opcao==1:
                aluno = self.cadastrar()
                self.listaAlunos.append(aluno)
                self.ct = self.ct+1
            elif self.opcao==2:
                self.imprimir()
            elif self.opcao==3:
                self.consultar65()
            elif self.opcao==4:
                self.maisp() 
            elif self.opcao==5:
                self.menosp() 
            elif self.opcao==6:
                self.qtdmaior() 
            elif self.opcao==7:
                self.qmaior() 
            elif self.opcao==8:
                self.qmenor() 
            elif self.opcao==9:
                self.imc()
            elif self.opcao==10:
                self.SalvarAlunos()
            elif self.opcao==11:
                self.RecuperarAlunos()
            elif self.opcao==12:
                self.RemoverAluno()        
            elif self.opcao==13:
                break    

class Aluno:
    def __init__(self, nome = "", idade = 0, altura = 0.0, peso = 0.0,  ID=0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.ID = ID

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

moduloA = ModuloAcademico()
moduloA.Executar()