"""Elaborar um programa que leia uma lista com 4 números reais, em seguida o programa deve exibir os números e a média."""
lista=[]
for cont in range(4):
    lista.append(float(input(f"digite o {cont+1} numero")))
    print(lista)
    media=sum(lista[:])/4
    print(media)