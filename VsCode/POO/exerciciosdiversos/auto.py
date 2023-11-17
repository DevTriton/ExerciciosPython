class automovel:
    def __init__(self, ano, marca, cor, chasi, modelo):
        self.aro_da_roda = 0
        self.cavalos_do_motor = 0
        self.transparencia_da_janela = 0
        self.ano = ano
        self.marca = marca
        self.cor = cor
        self.fipe = 0
        self.teto_solar = 0
        self.chasi = chasi
        self.modelo = modelo
    def transportar(self):
        print ("O seu carro pode transportar pessoa")
    def andar(self):
        print ("O seu carro anda")
    def parar(self):
        print ("O seu carro pode parar")
    def desligar(self):
        print ("O seu carro pode desligar")            

a=automovel(int(input("digite o ano do carro ")), 
            float(input("digite o chassi do carro ")), 
            input("digite a marca do carro "), 
            input("digite o modelo do carro "),
            input("digite o cor do carro "))
a.desligar()