"""Faça um programa que leia uma lista que receba o nome, idade e sexo de pessoas até que o usuário digite fim no nome. Após a leitura faça: a) Imprima o Nome, idade e sexo das pessoas cuja idade seja maior que a idade da primeira pessoa. b) Imprima o Nome e idade de todas as mulheres. c) Imprima o Nome dos homens menores de 21 anos. """
import os
dados=[]
pessoa=[]
nome=0
nome=input("digite o nome da pessoa, fim para encerrar ").upper()
while nome!="FIM":
    dados.append(nome)
    idade=int(input("digite a idade da pessoa "))
    dados.append(idade)
    sexo=input("digite o sexo F-feminino M-Masculino ").upper()
    while sexo!="F" and sexo!="M":
        print("erro, porfavor digite F ou M")
        sexo=input("digite o sexo F-feminino M-Masculino ").upper()
    dados.append(sexo)  
    pessoa.append(dados[:])
    dados.clear()  
    nome=input("digite o nome da pessoa, fim para encerrar ").upper()
os.system("cls")    
print("Imprima o Nome, idade e sexo das pessoas cuja idade seja maior que a idade da primeira pessoa.")    
for cont in range(len(pessoa)):
    if pessoa[cont][1]>pessoa[0][1]:
        print(f"nome: {pessoa[cont][0]}, idade: {pessoa[cont][1]}, sexo: {pessoa[cont][2]}")
print("imprima o nome de todas as mulheres")
for cont1 in range(len(pessoa)):
    if pessoa[cont1][2]=="F":
        print(f"nome {pessoa[cont1][0]}")
print("Imprima o Nome dos homens menores de 21 anos.") 
for cont2 in range(len(pessoa)):
    if pessoa[cont2][2]=="M":
        if pessoa[cont2][1]<21:
            print(f"nome: {pessoa[cont2][0]}")