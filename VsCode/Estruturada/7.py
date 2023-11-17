"""Altere o programa anterior e crie uma segunda pesquisa para encontrar os alunos que tem maior altura e menor altura. Salve o resultado da pesquisa em um arquivo no formato JSON.  (obs.:  faça  o  download  do  arquivo  json  e  abra-o  na  sua  máquina,  utilizando  o browser, para ver se ele está correto.)"""
lista=[]
lista2=[]
resp="S"
n=0
esc=int(input("digite quantos alunos serão cadastrados "))
for cont in range(esc):
    lista.append(int(input(f"digite a idade do {cont+1} aluno: ")))
    lista2.append(float(input(f"digite a altura do {cont+1} aluno: ")))
altm=sum(lista2[:])/esc
resp=input("voçê quer consultar quantos alunos de mais de 13 anos estão abaixo da média de altura? S-Sim N-Não ").upper()
while resp!="S" and resp!="N":
    resp=input("por favor digite S-Sim ou N-Não ").upper()
if resp=="S":
    for cont in range(esc):
        if lista[cont]<=13:    
            if lista2[cont]<altm:
                n=n+1                
resp2=input("voçê quer salvar o resultado em um arquivo .Json? S-Sim N-Não ").upper()
while resp2!="S" and resp2!="N":
    resp2=input("por favor digite S-Sim ou N-Não ").upper()
if resp2=="S":    
    arquivo = open('1.Json','w')
    arquivo.write(f"o numero de alunos abaixo da media é: {n}\n")
    arquivo.close()    
print(f"o número de alunos abaixo da média é {n} ")