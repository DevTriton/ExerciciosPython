import json

class SistemaMeteorologico:
    def __init__(self, temperatura_media = 0, humidade_relativa = 0, precipitacao_media = 0):
        self.temperatura_media = temperatura_media
        self.humidade_relativa = humidade_relativa
        self.precipitacao_media = precipitacao_media
        self.op = 0
        self.listaMes=[]
        self.listaMes2=[]
        self.listaMes3=[]

    def cadastrar_tempmedia(self):
        temperaturas = []
        for cont in range(12):
            temperaturas.append(float(input(f"digite a temperatura média do {cont+1} mes")))
            self.temperatura_media = sum(temperaturas)/12
        print(self.temperatura_media)
        return SistemaMeteorologico(self.temperatura_media)
    
    def cadastrar_humrelat(self):
        humidade = []
        for cont in range(12):
            humidade.append(float(input(f"digite a humidade relativa do ar média do {cont+1} mes")))
            self.humidade_relativa = sum(humidade)/12
        print(self.humidade_relativa)
        return SistemaMeteorologico(self.humidade_relativa)
    
    def cadastrar_precipmed(self):
        precipitacao = []
        for cont in range(12):
            precipitacao.append(float(input(f"digite a precipitação média do {cont+1} mes")))
            self.precipitacao_media = sum(precipitacao)/12
        print(self.precipitacao_media)
        return SistemaMeteorologico(self.precipitacao_media)
    
    def menu(self):
        print("O que deseja fazer?")
        print("1) Cadastrar a temperatura média")
        print("2) Cadastrar a humidade relativa do ar média")
        print("3) Cadastrar a precipitação média")
        print("4) salvar em .json")
        print("5) Sair")
        self.op=int(input("digite a opção escolhida: "))

    def Executar(self):
        while self.op != 5:
            self.menu()
            
            if self.op == 1:
                self.cadastrar_tempmedia()
                self.listaMes.append(SistemaMeteorologico)
            if self.op == 2:
                self.cadastrar_humrelat()
                self.listaMes2.append(SistemaMeteorologico)
            if self.op == 3:
                self.cadastrar_precipmed()
                self.listaMes3.append(SistemaMeteorologico)
            if self.op == 4:
                self.SalvarAlunos()
            if self.op == 5:
                break 

    def Serializar(self):
        dic = {}
        dic["temperatura média"] = self.temperatura_media
        dic["humidade relativa do ar"] = self.humidade_relativa
        dic["precipitação média"] = self.precipitacao_media
        texto_json = json.dumps(dic, indent = 3)
        return texto_json

    def Deserializar(self, texto_json):
        dic = json.loads(texto_json)
        self.temperatura_media = dic["temperatura média"]
        self.humidade_relativa = dic["humidade relativa do ar"]
        self.precipitacao_media = dic["precipitação média"]

    def SalvarAlunos(self):
        lista = []
        arquivo = open("meses.json", 'w')
        for cont in self.listaMes :
            lista.append(cont.Serializar())
        json.dump(lista, arquivo) 

    def RecuperarAlunos(self):
        self.listaMes.clear()
        arquivo = open("meses.json", 'r')
        lista_de_jsons_text = json.load(arquivo)
        for text in lista_de_jsons_text:
            a = SistemaMeteorologico()
            a.Deserializar(text)
            self.listaMes.append(a)                    

moduloA = SistemaMeteorologico()
moduloA.Executar()            