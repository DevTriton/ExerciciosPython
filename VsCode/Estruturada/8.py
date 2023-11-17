"""Elaborar um programa que leia uma lista que contenha 20 números inteiros e em seguida o programa deve exibir o maior e o menor número."""
lista=[]
for cont in range(20):
    lista.append(int(input(f"digite o {cont+1} numero")))
maior=max(lista)
menor=min(lista)    
print(f"o maior numero é {maior} e o menor é {menor}")