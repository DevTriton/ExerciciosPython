"""elabore um programa que recebe um texto, fornecido pelo user e verifica se o texto é um anagrama"""
texto=input("digite o texto ")
j=len(texto)-1
x = 0
print(range(0, len(texto)-1))
for cont in range(0, len(texto)-1):
    if texto[cont]!=texto[j]:
        print("cont: ", cont, " j: ", j)
        print("não é")
        x =1
        break
    j=j-1

if x ==0:
    print("sua palavra é um anagrama")    
