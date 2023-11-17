"""Elaborar um programa que leia uma lista de 6 números inteiros e mostre cada número juntamente com a sua posição na lista."""
lista=[]
for cont in range(6):
    lista.append(int(input("digite o numero desejado")))
for cont in range(6):  
    index=lista.index(lista[cont])  
    print(f"o numero {lista[cont]} tem o indice{index}")