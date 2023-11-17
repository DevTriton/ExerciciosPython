"""Elabore um programa que gere um vetor(lista em python)A com n números inteiros aleatórios, calcule e mostre a soma dos quadrados dos elementos do vetor."""
import random
lista=[]
lista2=[]
esc=int(input("digite quantos numeros deseja gerar para a lista: "))
for cont in range(esc):
    lista.append(random.randrange(0,100))
for cont2 in range(esc):
    lista2.append(lista[cont2] * lista[cont2])
soma=sum(lista2[:])
print(lista, lista2)
print(f"a soma dos quadrados é: {soma}")    