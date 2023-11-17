"""Elaborar um programa para ler uma lista A de 15 elementos e um valor X. O programa deve copiar para a lista B somente os elementos de A que são maiores que X. Exibir no final a lista B. """
lista=[]
num=[]
for cont in range(15):
    lista.append(int(input(f"digite o {cont+1} valor: ")))
escolha=int(input("digite o numero que deseja comparar. "))    
for cont in range(15):
    if lista[cont]>escolha:
        num.append(lista[cont])
print(num)        