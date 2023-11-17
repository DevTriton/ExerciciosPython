"""Elaborar um programa que leia uma lista de 6 números inteiros e mostre cada número juntamente com a sua posição na lista."""
lista=[]
for cont in range(6):
    lista.append(int(input("digite um numero ")))
for cont1 in range(6):
    index=lista.index(lista[cont1])
    print(f"o numero é {lista[cont1]} e seu indice é {index}")