"""Elaborar um programa para ler uma lista A de 15 elementos e um valor X. O programa deve copiar para a lista B somente os elementos de A que são maiores que X. Exibir no final a lista B. """
listaA=[]
listaB=[]
for cont in range(15):
    listaA.append(int(input(f"digite o {cont+1} número")))
print(f"numeros digitados: {listaA}")    
n=int(input("digite o numero para ser comparado"))
for cont in range(15):
    if listaA[cont]>n:
        n1=listaA[cont]
        listaB.append(n1)
print(f"numeros digitados após a alteração: {listaB}")         
