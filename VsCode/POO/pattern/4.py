class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        print("Movendo!")

    def acerelar(self):
       print("acerelando")

    def ligar(self):
       print("ligando")

    def desligar(self):
       print("desligando")

    def frear(self):
       print("freando")

class Carro(Veiculo):
    def __str__(self):
            return f'Carro({self.marca},{self.modelo})'
    pass

class Bote(Veiculo):
    def __str__(self):
            return f'Bote({self.marca},{self.modelo})'
    pass

    def mover(self):
        print("Velejando!")

    def acerelar(self):
       print("acerelando")

    def ligar(self):
       print("dando corda")

    def desligar(self):
       print("desligando")

    def frear(self):
       print("freando")

class Aviao(Veiculo):
    def __str__(self):
        return f'Avião({self.marca},{self.modelo})'
    pass

    def mover(self):
        print("Voando!")

    def acerelar(self):
       print("acerelando")

    def ligar(self):
       print("dando partida")

    def desligar(self):
       print("desligando motores, ativando rodas")

    def frear(self):
       print("Caiu")    

carro1 = Carro("Ford", "Mustang") #Create a Car object
bote1 = Bote("Ibiza", "Touring 20") #Create a Boat object
aviao1 = Aviao("Boeing", "747") #Create a Plane object

for x in (carro1, bote1, aviao1):
  print(x.marca)
  print(x.modelo)
  x.mover()
  print("--------------------------")

print(carro1)
print(bote1)  