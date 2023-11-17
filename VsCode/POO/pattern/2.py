import json
import os

class Pessoa:
    def __init__(self, nome="", idade=0, altura=0.0, peso=0.0, rgm=""):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, altura=0.0, peso=0.0, rgm=""): 
        super().__init__(nome, idade, altura, peso)
        self.rgm = rgm

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

    def serializar(self):
      dic = {}
      dic["nome"] = self.nome
      dic["idade"] = self.idade
      dic["altura"] = self.altura
      dic["peso"] = self.peso
      dic["rgm"] = self.rgm
      texto_json = json.dumps(dic, indent = 3)
      return texto_json

    def deserializar(self, texto_json):
      dic = json.loads(texto_json)
      self.nome = dic["nome"]
      self.idade = dic["idade"]
      self.altura = dic["altura"]
      self.peso = dic["peso"]
      self.rgm = dic["rgm"]

class Professor(Pessoa):
    def __init__(self, nome="", idade=0, altura=0.0, peso=0.0, matricula=""):
        super().__init__(nome, idade, altura, peso)
        self.matricula = matricula

    def serializar(self):
      dic = {}
      dic["nome"] = self.nome
      dic["idade"] = self.idade
      dic["altura"] = self.altura
      dic["peso"] = self.peso
      dic["matricula"] = self.matricula
      texto_json = json.dumps(dic, indent = 3)
      return texto_json

    def deserializar(self, texto_json):
      dic = json.loads(texto_json)
      self.nome = dic["nome"]
      self.idade = dic["idade"]
      self.altura = dic["altura"]
      self.peso = dic["peso"]
      self.matricula = dic["matricula"]

class Disciplina:
  def __init__(self, codigo="", nome="", cargaHoraria=160, turma="", notaMinima=7):
      self.codigo = codigo
      self.nome = nome
      self.cargaHoraria = cargaHoraria
      self.turma = turma
      self.notaMinima = notaMinima

  def serializar(self):
    dic = {}
    dic["codigo"] = self.codigo
    dic["cargaHoraria"] = self.cargaHoraria
    dic["turma"] = self.turma
    dic["notaMinima"] = self.notaMinima
    texto_json = json.dumps(dic, indent = 3)
    return texto_json

  def deserializar(self, texto_json):
    dic = json.loads(texto_json)
    self.codigo = dic["codigo"]
    self.cargaHoraria = dic["cargaHoraria"]
    self.turma = dic["turma"]
    self.notaMinima = dic["notaMinima"]


class ModuloAcademico:
    def __init__(self):
        self.opcao = 0
        self.listaAlunos = []
        self.listaProfessores = []
        self.listaDisciplinas = []
        self.RecuperarAlunos()
        self.recuperarProfessores()
        self.recuperarDisciplinas()

    def cadastrarAluno(self):
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        altura = float(input("Digite a altura do aluno: "))
        peso = float(input("Digite o peso do aluno: "))
        RGM = input("Digite o RGM do aluno: ")
        aluno = Aluno(nome, idade, altura, peso, RGM)
        self.listaAlunos.append(aluno)
        self.salvarAlunos()

    def cadastrarProfessor(self):
        nome = input("Digite o nome do professor: ")
        idade = int(input("Digite a idade do professor: "))
        altura = float(input("Digite a altura do professor: "))
        peso = float(input("Digite o peso do professor: "))
        matricula = input("Digite a matricula do aluno: ")
        professor = Professor(nome, idade, altura, peso, matricula)
        self.listaProfessores.append(professor)
        self.salvarProfessores()

    def cadastrarDisciplina(self):
        codigo = input("Digite o codigo da disciplina: ")
        nome = input("Digite o nome da disciplina: ")
        cargaHoraria = int(input("Digite a carga horaria da disciplina: "))
        turma = input("Digite a turma da disciplina: ")
        notaMinima = float(input("Digite a nota minima da disciplina: "))
        disciplina = Disciplina(codigo, nome, cargaHoraria, turma, notaMinima)
        self.listaDisciplinas.append(disciplina)
        self.salvarDisciplinas()

    def imprimirAluno(self):
      print("|Alunos:")
      print("|Nome|Idade|Altura|Peso|RGM")
      print("-------------------------------")
      for a in self.listaAlunos :
        print(a.nome, "|", a.idade, "|", a.altura, "|", a.peso, "|", a.rgm)
      print("-------------------------------")

    def imprimirProfessor(self):
      print("|Professores:")
      print("|Nome|Idade|Altura|Peso|Matricula")
      print("-------------------------------")
      for a in self.listaProfessores :
        print(a.nome, "|", a.idade, "|", a.altura, "|", a.peso, "|", a.matricula)
      print("-------------------------------")

    def imprimirDisciplina(self):
      print("|Disciplinas:")
      print("|Codigo|Nome|CargaHoraria|Turma|NotaMinima")
      print("-------------------------------")
      for a in self.listaDisciplinas :
        print(a.codigo, "|", a.nome, "|", a.cargaHoraria, "|", a.turma, "|", a.notaMinima)
      print("-------------------------------")

    def removerAluno(self):
        RGM = input("Digite o RGM do aluno a ser removido: ")
        i = 0
        while i < len(self.listaAlunos):
          if self.listaAlunos[i].rgm == RGM:
            del self.listaAlunos[i]
            self.salvarAlunos()
            print("Aluno, RGM [", RGM, "], removido!")
            return
          i = i + 1
        print("Aluno, RGM [", RGM, "], nao encontrado!")

    def removerProfessor(self):
        matricula = input("Digite a marticula do professor a ser removido: ")
        i = 0
        while i < len(self.listaProfessores):
          if self.listaProfessores[i].matricula == matricula:
            del self.listaProfessores[i]
            self.salvarProfessores()
            print("Professor, matricula [", matricula, "], removido!")
            return
          i = i + 1
        print("Professor, matricula [", matricula, "], nao encontrado!")

    def removerDisciplina(self):
        codigo = input("Digite oo codigo da disciplina a ser removida: ")
        i = 0
        while i < len(self.listaDisciplinas):
          if self.listaDisciplinas[i].codigo == codigo:
            del self.listaDisciplinas[i]
            self.salvarDisciplinas()
            print("Disciplina, codigo [", codigo, "], removida!")
            return
          i = i + 1
        print("Disciplina, codigo [", codigo, "], nao encontrado!")

    def RecuperarAlunos(self):
      self.listaAlunos.clear()
      if os.path.exists('alunos.json'):
        arquivo = open("alunos.json", 'r')
        lista_de_jsons_text = json.load(arquivo)
        for text in lista_de_jsons_text:
          a = Aluno()
          a.deserializar(text)
          self.listaAlunos.append(a)

    def recuperarProfessores(self):
      self.listaProfessores.clear()
      if os.path.exists('professores.json'):
        arquivo = open("professores.json", 'r')
        lista_de_jsons_text = json.load(arquivo)
        for text in lista_de_jsons_text:
          p = Professor()
          p.deserializar(text)
          self.listaProfessores.append(p)

    def recuperarDisciplinas(self):
      self.listaDisciplinas.clear()
      if os.path.exists('disciplinas.json'):
        arquivo = open("disciplinas.json", 'r')
        lista_de_jsons_text = json.load(arquivo)
        for text in lista_de_jsons_text:
          d = Disciplina()
          d.deserializar(text)
          self.listaDisciplinas.append(d)

    def atualizarAluno(self):
        RGM= input("Digite o RGM do aluno a ser atualizado: ")
        for aluno in self.listaAlunos:
            if aluno.RGM == RGM:
                aluno.nome = input("Digite o novo nome do aluno: ")
                aluno.idade = int(input("Digite a nova idade do aluno: "))
                aluno.altura = float(input("Digite a nova altura do aluno: "))
                aluno.peso = float(input("Digite o novo peso do aluno: "))
            break
        self.salvarAlunos()

    def atualizarProfessor(self):
        matricula = input("Digite a matricula do professor a ser atualizado: ")
        for professor in self.listaProfessores:
            if professor.matricula == matricula:
                professor.nome = input("Digite o novo nome do professor: ")
                professor.idade = int(input("Digite a nova idade do professor: "))
                professor.altura = float(input("Digite a nova altura do professor: "))
                professor.peso = float(input("Digite o novo peso do professor: "))
                break
        self.salvarProfessores()

    def atualizarDisciplina(self):
        codigo = input("Digite o codigo da disciplina a ser atualizado: ")
        for disciplina in self.listaDisciplinas:
            if disciplina.codigo == codigo:
                disciplina.nome = input("Digite o novo nome da disciplina: ")
                disciplina.cargaHoraria = int(input("Digite a nova carga horaria da disciplina: "))
                disciplina.turma = input("Digite a nova turma da disciplina: ")
                disciplina.notaMinima = float(input("Digite a nova nota minima da disciplina: "))
                break
        self.salvarDisciplinas()

    def salvarAlunos(self):
      lista = []
      arquivo = open("alunos.json", 'w')
      for a in self.listaAlunos :
        lista.append(a.serializar())
      json.dump(lista, arquivo)
      print("Salvo!")

    def salvarProfessores(self):
      lista = []
      arquivo = open("professores.json", 'w')
      for a in self.listaProfessores :
        lista.append(a.serializar())
      json.dump(lista, arquivo)
      print("Salvo!")

    def salvarDisciplinas(self):
      lista = []
      arquivo = open("disciplinas.json", 'w')
      for a in self.listaDisciplinas :
        lista.append(a.serializar())
      json.dump(lista, arquivo)
      print("Salvo!")

    def consultarAlunos65plus(self):
        contador = 0
        for a in self.listaAlunos :
            if a.peso > 65:
                contador += 1
        print("Quantidade de alunos > 65 kg eh: ", contador)
        for a in self.listaAlunos :
            if a.peso > 65:
                print("O aluno ", a.nome, " tem imc: ", a.imc())

    def executar(self):
        while True:
            print("|############################################################|")
            print("|    ----------     OOP PYTHON        ------- | ")
            print("|############################################################|")
            print("   -- ALUNOS --  ")
            print(" 1) Cadastrar Alunos")
            print(" 2) Imprimir Alunos")
            print(" 3) Remover Alunos")
            print(" 4) Atualizar Alunos")
            print(" 5) Consulta Alunos > 65 Kg:")
            print(" ")
            print("   -- PROFESSOR --  ")
            print(" 11) Cadastrar Professor")
            print(" 12) Imprimir Professor")
            print(" 13) Remover Professor")
            print(" 14) Atualizar Professor")
            print("")
            print("   -- DISCIPLINA --  ")
            print(" 21) Cadastrar Disciplina")
            print(" 22) Imprimir Disciplina")
            print(" 23) Remover Disciplina")
            print(" 24) Atualizar Disciplina")
            print("")
            print("0 - Sair")

            self.opcao = input("Escolha uma opcao: ")

            if self.opcao == "1":
                self.cadastrarAluno()
            elif self.opcao == "2":
                self.imprimirAluno()
            elif self.opcao == "3":
                self.removerAluno()
            elif self.opcao == "4":
                self.atualizarAluno()
            elif self.opcao == "5":
                self.consultarAlunos65plus()

            elif self.opcao == "11":
                self.cadastrarProfessor()
            elif self.opcao == "12":
                self.imprimirProfessor()
            elif self.opcao == "13":
                self.removerProfessor()
            elif self.opcao == "14":
                self.atualizarProfessor()

            elif self.opcao == "21":
                self.cadastrarDisciplina()
            elif self.opcao == "22":
                self.imprimirDisciplina()
            elif self.opcao == "23":
                self.removerDisciplina()
            elif self.opcao == "24":
                self.atualizarDisciplina()
            elif self.opcao == "0":
                break
            else:
                print("Opcao invûÀlida. Tente novamente.")

if __name__ == "__main__":
    modulo_academico = ModuloAcademico()
    modulo_academico.executar()