import os
class alunos:
    def __init__(self, nome, idade, altura, peso ):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    def imc(self, var1, var2):
        self.peso = var1
        self.altura = var2
        self.imc2 = imc2
        imc2=var1/(var2*2)
lista = []
lista2 = []
mp=0
maisp=0
esc=int(input("quantos alunos voçê deseja consultar? "))
for cont in range(esc):
    lista.append(input("digite o nome do aluno "))     
    lista.append(int(input("digite a idade do aluno ")))  
    lista.append(float(input("digite o altura do aluno em metros ")))
    lista.append(float(input("digite o peso do aluno ")))
    os.system("cls")
    lista2.append(lista[:])
    lista.clear()
print(lista2)
resp=int(input("1-Alunos com mais de 65kg 2-Aluno mais pesado 3-aluno mais leve 4-quantidade de alunos maiores de idade 5-quem são os maiores 6-quem são os menores 7-sair"))
while resp!=7:
    
    if resp==1:
        for cont in range(esc):
            if lista2[cont][3] > 65:
                mp=mp+1
        print(f"Com mais de 65kg são {mp} alunos")
    else:
        if resp==2:
            for cont in range(0, esc):
                if lista2[cont][3] > lista2[cont+1][3]:
                    maisp=lista2[cont][0]
                print(f"o aluno mais pesado é {maisp}")
    resp=int(input("1-Alunos com mais de 65kg 2-Aluno mais pesado 3-aluno mais leve 4-quantidade de alunos maiores de idade 5-quem são os maiores 6-quem são os menores 7-sair"))        