"""Altere o programa anterior, intercalando 3 vetores de n elementos cada em um vetor de tamanho 3*N"""
import random
lista1=[]
lista2=[]
lista3=[]
lista4=[]
esc=int(input("digite quantos números deseja ter nas listas: "))
for cont in range(esc):
    lista1.append(random.randrange(0,100))
for cont in range(esc):    
    lista2.append(random.randrange(0,100))
for cont in range(esc):    
    lista3.append(random.randrange(0,100))    
for cont2 in range(esc):
    lista4.append(lista1[cont2])
    lista4.append(lista2[cont2])
    lista4.append(lista3[cont2])
print(f"O vetor com os elementos intercalados dos vetores 1, 2 e 3 é: {lista4}")