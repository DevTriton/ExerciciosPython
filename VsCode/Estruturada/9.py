"""Altere o programa anterior e coloque o resultado dentro de um dictionary, exiba-o na tela, e salve-o em um arquivo no formato texto. (obs.: faça o download do arquivo e abra-o na sua máquina, utilizando o browser, para ver se ele está correto.)"""
lista=[]
lista2=["Janeiro", "fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
lista3=[]
lista4={}
ct=0
for cont in range (12):
    lista.append(float(input(f"digite a temperatura média do mês {cont+1} ")))
media=(sum(lista[:]))/12
for cont2 in range (12):
    if lista[cont2]>media:
        lista3.append(lista2[cont2])
        ct=ct+1
        lista4.update({ct:lista2[cont2]})
print(lista4)
arquivo = open('1.txt','w')
arquivo.write(f"os meses acima da média são {lista4}\n")
arquivo.close()
