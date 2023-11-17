"""Faça um programa que leia uma lista que receba o nome, idade e sexo de pessoas até que o usuário digite fim no nome. Após a leitura faça: a) Imprima o Nome, idade e sexo das pessoas cuja idade seja maior que a idade da primeira pessoa. b) Imprima o Nome e idade de todas as mulheres. c) Imprima o Nome dos homens menores de 21 anos. """
import os
dados=[]
pessoa=[]
nome=input("Digite o nome, fim para encerrar")
while nome!="fim":
    dados.append(nome)
    sexo=input("Digite o sexo M-masculino F-Feminino: ").upper()
    while sexo!="F" and sexo!="M":
        print("erro")
        sexo=input("Digite o sexo: ").upper()
    dados.append(sexo)    
    idade=int(input("Digite a idade: "))
    while idade<=0 and idade>=116:
        idade=int(input("Digite a idade: "))
    dados.append(idade)
    pessoa.append(dados[:])
    dados.clear()
    nome=input("Digite o nome, fim para encerrar")   
os.system("cls")
print("Imprima o Nome, idade e sexo das pessoas cuja idade seja maior que a idade da primeira pessoa.")    
print("Nome \t idade \t sexo")
for cont in range (len(pessoa)):
    if pessoa[cont][2] > pessoa[0][2]:
        print(f"{pessoa[cont][0]}\t{pessoa[cont][1]}\t{pessoa[cont][2]}")
print("imprima o nome de todas as mulheres")
print("Nome \t idade")
for cont1 in range(len(pessoa)):
    if pessoa[cont1][1] == "F":
        print(f"{pessoa[cont][0]}\t{pessoa[cont][2]}")
print("Imprima o Nome dos homens menores de 21 anos.") 
print("Nome\tIdade")
for cont2 in range(len(pessoa)):
    if pessoa[cont2][1]=="M":
        if pessoa[cont2][2] < 21:
            print(f"{pessoa[cont2][0]}\t{pessoa[cont2][2]}")