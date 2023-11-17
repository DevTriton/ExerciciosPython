lista=[]
lista2=[]
m65=0
class Aluno:
    def __init__(self, nome, idade, altura, peso):
        self.nome=nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
  
a=Aluno("eddie", 18, 1.86, 100)
lista.append(a.nome)
lista.append(a.idade)
lista.append(a.peso)
lista2.append(lista[:])
lista.clear()
b=Aluno("Igor", 16, 1.86, 120)
lista.append(b.nome)
lista.append(b.idade)
lista.append(b.peso)
lista2.append(lista[:])
lista.clear()
c=Aluno("vinicius", 23, 1.76, 80)
lista.append(c.nome)
lista.append(c.idade)
lista.append(c.peso)
lista2.append(lista[:])
lista.clear()

print(lista2)

for cont in range (3):
    if lista2[cont][2] > 65:
        m65= m65+1
if lista2[0][2]>lista2[1][2]:
      if lista2[0][2]>lista2[2][2]:
        print(f"o aluno com mais peso é {lista2[0][0]}")
if lista2[1][2]>lista2[2][2]:
    print(f"o aluno com mais peso é {lista2[1][0]}")
else: 
    print(f"o aluno com mais peso é {lista2[2][0]}")                      
print(m65)