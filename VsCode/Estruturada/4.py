"""Elabore um programa que leia as idades e alturas de n alunos, na fase de cadastro. Depois o programa deve fornecer a opção de consulta, que deve avaliar a quantidade de alunos com mais de 13 anos que possuem altura inferior à média de altura dos demais alunos."""
lista=[]
lista2=[]
resp="S"
n=0
esc=int(input("digite quantos alunos serão cadastrados "))
for cont in range(esc):
    lista.append(int(input(f"digite a idade do {cont+1} aluno: ")))
    lista2.append(float(input(f"digite a altura do {cont+1} aluno: ")))
altm=sum(lista2[:])/esc
while resp!="N":
    resp=input("voçê quer consultar quantos alunos de mais de 13 anos estão abaixo da média de altura? S-Sim N-Não ").upper()
    while resp!="S" and resp!="N":
        resp=input("por favor digite S-Sim ou N-Não ").upper()
    for cont in range(esc):
        if lista[cont]<=13:    
            if lista2[cont]<altm:
                n=n+1    
    print(f"o número de alunos abaixo da média é {n} ")