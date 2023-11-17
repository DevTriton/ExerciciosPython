"""Elaborar um programa que contém uma lista com 5 elementos. O usuário deve preencher essa lista. Exibir no final os valores inseridos pelo usuário, porém os valores negativos (caso existirem) devem ser substituídos por zero (0)."""
lista=[]
for cont in range(5):
    lista.append(float(input(f"digite o {cont+1} número, os negativos seram substituidos por zero")))
print(f"os numeros antes da mudança são: {lista}")
for cont in range(5):
    if lista[cont]<0:
        lista[cont]=0
print(f"os numeros após da mudança são: {lista}")        
