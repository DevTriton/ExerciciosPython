print("Elaborar um programa em Python que receba uma lista com 9 valores numéricos, calcule e mostre quantos números pares foram digitados e a somatória desses números.")
lista=[]
contpar=0
for cont in range (0,9):
    lista.append(int(input(f"digite o {cont} numero"))) 
    if lista[cont]%2==0:
        contpar=contpar+1
soma=sum(lista[:])
print(f"a quantidade de números pares é {contpar}, e a soma total é {soma}.")        