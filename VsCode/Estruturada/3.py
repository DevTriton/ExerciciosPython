"""receba o nome e a nota de cada aluno(a) até receber uma informação de finalização pelo usuário; - guarde 
estes valores em uma lista, calcule e mostre: a média, aluno(a) com maior nota e aluno
(a) com menor nota."""
esc="S"
rep=0
notas=[]
alunos=[]
while esc!="N":
    notas.append(input("digite o nome do aluno"))
    notas.append(float(input("digite a nota")))
    alunos.append(notas[:])
    notas.clear()
    rep=rep+1 
    esc=input("Quer continuar? S-Sim ou N-Não ").upper()
    while esc!="S" and esc!="N":
        esc=input("Quer continuar? S-Sim ou N-Não ").upper()
todos=sum(alunos)
for cont in range(rep):
    media=todos/rep
    print(media)        