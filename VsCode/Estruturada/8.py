"""Elabore  um  programa  que receba  a  temperatura  média  de  cada  mês  do  ano  e armazene-as  em  uma  lista.  Após  isto,  calcule  a  média  anual  das  temperaturas  e  mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 Janeiro, 2 Fevereiro, etc.)."""
lista=[]
lista2=["Janeiro", "fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
lista3=[]
for cont in range (12):
    lista.append(float(input(f"digite a temperatura média do mês {cont+1} ")))
media=(sum(lista[:]))/12
for cont2 in range (12):
    if lista[cont2]>media:
        lista3.append(lista2[cont2])
print(lista3)
