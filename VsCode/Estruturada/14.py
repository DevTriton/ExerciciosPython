palavra=input("digite a palavra que deseja checar ")
f=len(palavra)-1
s=len(palavra)
x=0
for cont in range(len(palavra)):
    if palavra[f] == palavra[cont]:
        x=x+1
        f=f-1  
    else:
        print("Não é um anagrama") 
        break
if x == s:
    print("sua palavra é um anagrama")
