class Animal():
    def __init__(self, nome, cor):
        self.__nome = nome
        self.__cor = cor

    def comer(self):
        print(f"O {self.__nome} está comendo")

    def getNome(self):
        return self.__nome    

    def andar(self):
        print(f"O {self.__nome} está andar")

    def dormir(self):
        print(f"O {self.__nome} está dormir")

    def fugir(self):            
        print(f"O {self.__nome} está fugindo")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Galinha(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def botarOvos(self):
        print(F"O {self._getNome()} botou um ovo")    


gato = Gato("Bichano", "Branco")
cachorro = Cachorro("Totó", "Preto")
coelho = Coelho("Pernalonga", "Cinza")
galinha = Galinha("Pintadinha", "Amarela")

gato.comer()
cachorro.comer()
coelho.comer()
galinha.botarOvos()        