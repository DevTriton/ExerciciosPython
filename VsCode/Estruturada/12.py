import random
lista=[]
lista2=[]
resp=0
sus=0
cump=0
ass=0
ino=0
resp0=0
resp1=0
resp2=0
resp3=0
resp4=0
zero=0
um=0
dois=0
tres=0
quatro=0
zerow=0
umw=0
doisw=0
tresw=0
quatrow=0
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
        resp0=resp0+1
    if lista2[cont2][1]==0:
        resp=resp+1
        resp1=resp1+1
    if lista2[cont2][2]==0:
        resp=resp+1
        resp2=resp2+1
    if lista2[cont2][3]==0:
        resp=resp+1
        resp3=resp3+1
    if lista2[cont2][4]==0:
        resp=resp+1 
        resp4=resp4+1
    x0=(100*resp0)/resp   
    x1=(100*resp1)/resp 
    x2=(100*resp2)/resp 
    x3=(100*resp3)/resp 
    x4=(100*resp4)/resp  
    if resp==2:
        sus=sus+1
        if lista2[cont2][0]==0:
            zero=zero+1
        if lista2[cont2][1]==0:
            um=um+1
        if lista2[cont2][2]==0:
            dois=dois+1
        if lista2[cont2][3]==0:
            tres=tres+1
        if lista2[cont2][4]==0:
            quatro=quatro+1  
    else:
        if resp>3 and resp<=4:
            cump=cump+1
            if lista2[cont2][0]==0:
                zero=zero+1
            if lista2[cont2][1]==0:
                um=um+1
            if lista2[cont2][2]==0:
                dois=dois+1
            if lista2[cont2][3]==0:
                tres=tres+1
            if lista2[cont2][4]==0:
                quatro=quatro+1                  
        else:
            if resp==5:
                ass=ass+1
            else:
                ino=ino+1    
    resp=0
print(f"A porcentagem de respostas sim de cada pergunta é respectivamente {x0}%, {x1}%, {x2}%, {x3}%, {x4}%")
if x0>x1:
    if x0>x2:
        if x0>x3:
            if x0>x4:
                print("a primeira pergunta foi a mais respondida com Sim")
    else:
        if x1>x2:
            if x1>x3:
                if x1>x4:
                    print("a segunda pergunta foi a mais respondida com Sim")
        else:
            if x2>x3:
                if x2>x4:
                    print("a terceira pergunta foi a mais respondida com Sim")
            else:
                if x3>x4:
                    print("a quarta pergunta foi a mais respondida com Sim")  
                else:
                    print("a quinta pergunta foi a mais respondida com Sim")                                  
                    
if x0<x1:
    if x0<x2:
        if x0<x3:
            if x0<x4:
                print("a primeira pergunta foi a menos respondida com Sim")
    else:
        if x1<x2:
            if x1<x3:
                if x1<x4:
                    print("a segunda pergunta foi a menos respondida com Sim")
        else:
            if x2<x3:
                if x2<x4:
                    print("a terceira pergunta foi a menos respondida com Sim")
            else:
                if x3<x4:
                    print("a quarta pergunta foi a menos respondida com Sim")  
                else:
                    print("a quinta pergunta foi a menos respondida com Sim")
if zero>um:
    if zero>dois:
        if zero>tres:
            if zero>quatro:
                print("a primeira pergunta foi a mais respondida com Sim pelos cumplices")       
else:
    if um>dois:
        if um>tres:
            if um>quatro:
                print("a segunda pergunta foi a mais respondida com Sim pelos cumplices")                       
    else:
        if dois>tres:
            if dois>quatro:
                print("a terceira pergunta foi a mais respondida com Sim pelos cumplices")                       
        else:
            if tres>quatro:
                print("a quarta pergunta foi a mais respondida com Sim pelos cumplices")       
            else:
                print("a quinta pergunta foi a mais respondida com Sim pelos cumplices")

if zero<um:
    if zero<dois:
        if zero<tres:
            if zero<quatro:
                print("a primeira pergunta foi a menos respondida com Sim pelos cumplices")       
else:
    if um<dois:
        if um<tres:
            if um<quatro:
                print("a segunda pergunta foi a menos respondida com Sim pelos cumplices")                       
    else:
        if dois<tres:
            if dois<quatro:
                print("a terceira pergunta foi a menos respondida com Sim pelos cumplices")                       
        else:
            if tres<quatro:
                print("a quarta pergunta foi a menos respondida com Sim pelos cumplices")       
            else:
                print("a quinta pergunta foi a menos respondida com Sim pelos cumplices")                                                                                    
print(f"o total de Cumplices é: {cump} de Suspeitos é {sus} e de Assasinos são {ass} e de inocentes é {ino}")    