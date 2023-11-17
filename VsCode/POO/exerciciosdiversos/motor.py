class motor:
    def __init__(self, ano, marca, HP, modelo):
        self.ano = ano
        self.marca = marca
        self.modelo = modelo
        self.HP = HP
        self.cilindradas = 0
        self.injeção_eletrica = 0
        self.injeção_de_gasolina = 0
        self.taxa_de_compressão = 0
        self.Temperatura = 0
        self.temperatura_do_liquido_de_resfriamento = 0
    def ligar(self):
        print ("O seu motor pode ligar")
    def esquentar(self):
        print ("O seu motor esquenta")
    def esfriar(self):
        print ("O seu motor esfria")
    def desligar(self):
        print ("O seu motor pode desligar")            

a=motor(int(input("digite o ano do motor ")),
            input("digite a marca do motor "),  
            int(input("digite o HP do motor ")), 
            input("digite o modelo do motor "))
a.ligar()
a.esquentar()
a.esfriar()
a.desligar()