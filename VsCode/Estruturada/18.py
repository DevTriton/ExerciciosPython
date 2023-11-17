"""Elaborar um programa que leia uma lista com 4 números reais, em seguida o programa deve exibir os números e a média."""
lista=[]
media=0
for cont in range(4):
    lista.append(float(input("digite um número")))
    media=sum(lista[:])/4
print(f"o números são {lista} e a media é {media}")    