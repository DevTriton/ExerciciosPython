lista=[]
lista2=[]
lista3=[]
p=int(input("quantas pessoas deseja consultar? "))
anoa=int(input("digite o ano atual: "))
for cont in range(p):
    lista.append(int(input(f"digite o ano de nascimento da {cont+1} pessoa")))
    lista2.append(anoa-lista[cont])
    lista3.append(2050-lista[cont])
print(f" a idade das pessoas é: {lista2}")
print(f" e e 2050 elas terão: {lista3}")    