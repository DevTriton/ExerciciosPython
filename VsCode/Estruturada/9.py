"""Elaborar um programa que contém uma lista com 5 elementos. O usuário deve preencher essa lista. Exibir no final os valores inseridos pelo usuário, porém os valores negativos (caso existirem) devem ser substituídos por zero (0)."""
lista=[]
for cont in range(5):
    lista.append(int(input(f"digite o {cont+1} valor")))
    if lista[cont]<0:
        lista[cont]=0
print(lista)
