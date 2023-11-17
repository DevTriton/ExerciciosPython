import random
lista=[]
lista2=[]
resp=0
sus=0
cump=0
ass=0
ino=0
resp=int(input("quantas pessoas devem participar desta simulação? "))
for cont in range(resp):
    lista.append(random.randrange(0,2))
    lista.append(random.randrange(0,2))
    lista.append(random.randrange(0,2))
    lista.append(random.randrange(0,2))
    lista.append(random.randrange(0,2))
    lista2.append(lista[:])
    lista.clear()
for cont2 in range(resp):
    if lista2[cont2][0]==0:
        resp=resp+1
    if lista2[cont2][1]==0:
        resp=resp+1
    if lista2[cont2][2]==0:
        resp=resp+1
    if lista2[cont2][3]==0:
        resp=resp+1
    if lista2[cont2][4]==0:
        resp=resp+1 
    if resp==2:
        sus=sus+1
    else:
        if resp>3 and resp<=4:
            cump=cump+1
        else:
            if resp==5:
                ass=ass+1
            else:
                ino=ino+1    
    resp=0                                
print(f"as simulações são: {lista2} e o total de Cumplices é: {cump} de Suspeitos é {sus} e de Assasinos são {ass} e de inocentes é {ino}")    