"""Elaborar um programa que leia uma lista que contenha 20 números inteiros e em seguida o programa deve exibir o maior e o menor número."""
lista=[]
for cont in range(20):
    lista.append(int(input(f"digite o {cont+1} número ")))
minimo=min(lista)    
maximo=max(lista)
print(f"o menor número é {minimo} e o maior é {maximo}")