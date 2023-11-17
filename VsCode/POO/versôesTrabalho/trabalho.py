import json

class ModuloAcademico:
    def __init__(self):
        self.listaAlunos = []
        self.listaProfessor = []
        self.listaDisciplinas = []
        self.opcao = 0
        self.index = 0
        for cont in range (2):
            if cont == 2:
                self.RecuperarAlunos()
        #coloquei com o contador pois se não tiver um arquivo ja pré criado e com dados o script da erro, esqueci de perguntar quando tive a chancer :D        

# GERAL 
    def menu_geral(self):
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Qual lista deseja manipular?")
        print("1) Aluno")
        print("2) Professor")
        print("3) Disciplinas")
        print("4) sair")
        self.opcao=int(input("digite a opção desejada "))

    def Executar_geral(self):
        while self.opcao !=4:
            self.menu_geral() 
                        
            if self.opcao==1:
                self.ExecutarAluno()
            elif self.opcao==2:
                self.ExecutarProfessor()
            elif self.opcao==3:
                self.ExecutarDisciplinas()           
            elif self.opcao==4:
                break    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# ALUNO  
    def menuAluno(self):
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
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
        print("10) excluir um aluno")
        print("11) atualizar um aluno")
        print("12) Sair")
        self.opcao=int(input("digite a opção que deseja fazer: "))

    def ExecutarAluno(self):
        while self.opcao != 12:
            self.menuAluno() 
            
            if self.opcao==1:
                aluno = self.cadastrarAluno()
                self.listaAlunos.append(aluno)
                self.SalvarAluno()
            elif self.opcao==2:
                self.imprimirAluno()
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
                self.RemoverAluno()
                self.SalvarAluno()
            elif self.opcao==11:
                self.atualizarAluno()
                self.SalvarAluno()             
            elif self.opcao==12:
                break

    def cadastrarAluno(self):
        
        nome = input("digite o nome do aluno: ")
        idade = int(input("digite a idade do aluno: "))
        altura = float(input("digite a altura do aluno (metros): "))
        peso = float(input("digite o peso do aluno: "))
        ID = int(input("digite o numero id desse aluno"))
        RGM = input("digite o RGM do aluno: ")
        return Aluno(nome, idade, altura, peso, ID, RGM)

    def imprimirAluno(self):
        print("----------------------------------------")
        for cont in self.listaAlunos:
            print(cont.nome, "/", cont.idade, "/", cont.altura, "/", cont.peso, "/", cont.ID)    
        print("----------------------------------------")

    def SalvarAluno(self):
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
        resp = input("digite o Rgm do aluno: ")
        
        for cont in self.listaAlunos:
            if resp == cont.RGM:
                index = cont.ID - 1
                self.listaAlunos.pop(index)

    def atualizarAluno(self):
        resp=input("digite o rgm do aluno que deseja alterar")
        for cont in self.listaAlunos:
            if resp == cont.RGM:
                index = cont.ID - 1
                self.listaAlunos.pop(index)
                aluno = self.cadastrarAluno()
                self.listaAlunos.append(aluno)
                self.SalvarAluno()

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
      
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------# 
# PROFESSOR
 
    def menuProfessor(self):
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Oque deseja fazer?")
        print("1) Cadastrar Professor")
        print("2) Imprimir Professor")
        print("3) excluir um Professor")
        print("4) atualizar um Professor")
        print("5) Sair")
        self.opcao=int(input("digite a opção que deseja fazer: "))

    def ExecutarProfessor(self):
        while self.opcao != 5:
            self.menuProfessor() 
            
            if self.opcao==1:
                Professor = self.cadastrarProfessor()
                self.listaProfessor.append(Professor)
                self.SalvarProfessor()
            elif self.opcao==2:
                self.imprimirProfessor()
            elif self.opcao==3:
                self.RemoverProfessor()
                self.SalvarProfessor()
            elif self.opcao==4:
                self.atualizarProfessor()
                self.SalvarProfessor()             
            elif self.opcao==5:
                break

    def cadastrarProfessor(self):
        
        nome = input("digite o nome do Professor: ")
        idade = int(input("digite a idade do Professor: "))
        altura = float(input("digite a altura do Professor (metros): "))
        peso = float(input("digite o peso do Professor: "))
        matricula = int(input("digite a matricula desse Professor"))
        ID = int(input("digite o id desse professor"))
        return Professor(nome, idade, altura, peso, matricula, ID)

    def imprimirProfessor(self):
        print("----------------------------------------")
        for cont in self.listaProfessor:
            print(cont.nome, "/", cont.idade, "/", cont.altura, "/", cont.peso, "/", cont.matricula)    
        print("----------------------------------------")

    def SalvarProfessor(self):
        lista = []
        arquivo = open("professores.json", 'w')
        for cont in self.listaProfessor :
            lista.append(cont.Serializar())
        json.dump(lista, arquivo) 

    def RecuperarProfessor(self):
        self.listaProfessor.clear()
        arquivo = open("professores.json", 'r')
        lista_de_jsons_text = json.load(arquivo)
        for text in lista_de_jsons_text:
            a = Professor()
            a.Deserializar(text)
            self.listaProfessor.append(a)

    def RemoverProfessor(self):
        resp = input("digite a matricula do professor que deseja remover: ")
        
        for cont in self.listaProfessor:
            if resp == cont.matricula:
                index = cont.ID - 1
                self.listaProfessor.pop(index)

    def atualizarProfessor(self):
        resp=input("digite a matricula do professor que deseja alterar")
        for cont in self.listaProfessor:
            if resp == cont.matricula:
                index = cont.ID - 1
                self.listaProfessor.pop(index)
                professor = self.cadastrarProfessor()
                self.listaProfessor.append(professor)
                self.SalvarProfessor()          
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#  
    def menuDisciplinas(self):
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Oque deseja fazer?")
        print("1) Cadastrar Disciplina")
        print("2) Imprimir Disciplinas")
        print("3) excluir uma Disciplina")
        print("4) atualizar uma Disciplina")
        print("5) Sair")
        self.opcao=int(input("digite a opção que deseja fazer: "))

    def ExecutarDisciplinas(self):
        while self.opcao != 5:
            self.menuDisciplinas() 
            
            if self.opcao==1:
                aluno = self.cadastrarAluno()
                self.listaAlunos.append(aluno)
                self.SalvarAluno()
            elif self.opcao==2:
                self.imprimirAluno()
            elif self.opcao==3:
                self.RemoverAluno()
                self.SalvarAluno()
            elif self.opcao==4:
                self.atualizarAluno()
                self.SalvarAluno()             
            elif self.opcao==5:
                break                            
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#          

class Aluno:
    def __init__(self, nome = "", idade = 0, altura = 0.0, peso = 0.0,  ID=0, RGM=""):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.ID = ID
        self.RGM = RGM

    def Serializar(self):
        dic = {}
        dic["nome"] = self.nome
        dic["idade"] = self.idade
        dic["altura"] = self.altura
        dic["peso"] = self.peso
        dic["RGM"] = self.RGM
        dic["ID"] = self.ID
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
        self.RGM = dic["RGM"] 
        self.ID = dic["ID"]                                   

class Professor:
    def __init__(self, nome = "", idade = 0, altura = 0.0, peso = 0, matricula = 0, ID = 0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.matricula = matricula
        self.ID = ID

    def Serializar(self):
        dic = {}
        dic["nome"] = self.nome
        dic["idade"] = self.idade
        dic["altura"] = self.altura
        dic["peso"] = self.peso
        dic["matricula"] = self.matricula
        dic["ID"] = self.ID
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
        self.matricula = dic["Matricula"]
        self.ID = dic["ID"]     

moduloA = ModuloAcademico()
moduloA.Executar_geral()