"""Elabore um programa que gere dois vetores(lista em python) com n números inteiros aleatórios cada, Gere  um  terceiro  vetor  de  2*N elementos,  cujos  valores  deverão  ser compostos pelos elementos intercalados dos dois outros vetores. """
import random
lista1=[]
lista2=[]
lista3=[]
esc=int(input("digite quantos números deseja ter nas listas: "))
for cont in range(esc):
    lista1.append(random.randrange(0,100))
for cont in range(esc):    
    lista2.append(random.randrange(0,100))
for cont2 in range(esc):
    lista3.append(lista1[cont2])
    lista3.append(lista2[cont2])
print(f"O vetor com os elementos intercalados dos vetores 1 e 2 é: {lista3}")