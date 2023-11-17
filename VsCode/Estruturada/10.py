"""Elabore  um  programa  que faça  5  perguntas  para  uma  pessoa  sobre  um  crime.  As perguntas são:1."Telefonou para a vítima?"2."Esteve no local do crime?"3."Mora perto da vítima?"4."Devia para a vítima?"5."Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3  e 4  como "Cúmplice"  e 5  como "Assassino". Caso  contrário,  ele  será classificado como "Inocente"."""
lista=[]
resp=0
lista.append(input("Telefonou para a vítima? S ou N ").upper())
while lista[0]!="S" and lista[0]!="N":
    lista.append(input("Não tente evitar a pergunta eu sei tudo, S ou N ").upper())
lista.append(input("Esteve no local do crime? S ou N ").upper())
while lista[1]!="S" and lista[1]!="N":
    lista.append(input("Não tente evitar a pergunta eu sei tudo, S ou N ").upper())
lista.append(input("Mora perto da vítima? S ou N ").upper())
while lista[2]!="S" and lista[2]!="N":
    lista.append(input("Não tente evitar a pergunta eu sei tudo, S ou N ").upper())
lista.append(input("Devia para a vítima? S ou N ").upper())
while lista[3]!="S" and lista[3]!="N":
    lista.append(input("Não tente evitar a pergunta eu sei tudo, S ou N ").upper())
lista.append(input("Já trabalhou com a vítima? S ou N ").upper())
while lista[4]!="S" and lista[4]!="N":
    lista.append(input("Não tente evitar a pergunta eu sei tudo, S ou N ").upper())
for cont2 in range(5):
    if lista[cont2]=="S":
        resp=resp+1
if resp==2:
    print("Voçê é um suspeito")
else:
    if resp>3 and resp<=4:
        print("Voçê é um cúmplice")
    else:
        if resp==5:
            print("Voçê é o assassino")
        else:
            print("Voçê é inocente")    