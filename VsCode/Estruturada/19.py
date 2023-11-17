print("exercicios com lista")
lista=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
num=[]
"""intervalo de 1 a 9"""
print(f"{lista[1:10]}")
print("-"*30)
"""intervalo de 8 a 13"""
print(f"{lista[8:14]}")
print("-"*30)
"""numeros pares"""
for cont in range (len(lista)):
    if lista[cont]%2==0:
        num.append(lista[cont])
print(num)
num.clear() 
print("-"*30)  
"""numeros impares"""
for cont1 in range(len(lista)):
    if lista[cont1]%2!=0:
        num.append(lista[cont1])
print(num)
num.clear()
print("-"*30)
"""multiplos de 2, 3 e 4"""  
for cont3 in range(len(lista)):
    if lista[cont3]%2==0:
        num.append(lista[cont3])
print(num)
num.clear()
print("-"*30)    
for cont3 in range(len(lista)):
    if lista[cont3]%3==0:
        num.append(lista[cont3])
print(num)
num.clear() 
print("-"*30) 
for cont3 in range(len(lista)):
    if lista[cont3]%4==0:
        num.append(lista[cont3])
print(num)
num.clear()
print("-"*30) 
"""lista reversa"""  
for cont4 in range(len(lista)-1,0,-1):
    num.append(cont4)
print(num)  
num.clear()
print("-"*30)
"""soma do intervalo de 10 a 15"""
soma=sum(lista[10:16]) 
print(soma)
print("-"*30)
"""uma lista com um novo elemento"""
lista.append(16)
print(lista)
print("-"*30)
"""substituir o elemento com indice 6"""
lista.insert(6,17)
print(lista)