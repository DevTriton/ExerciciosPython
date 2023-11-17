print("Elabore um fluxograma que receba o salário de N funcionários. Calcule e mostre:")
N=int(input("digite a quantidade de vezes que deseja receber o salario"))
while N<=0:
    print("erro")
    N=int(input("digite a quantidade de vezes que deseja receber o salario"))
total=0
cont2500=0
cont1300=0
for cont in range (0,N):
    sal=float(input("digite o salário"))
    while sal<=0:
        print("Erro")
        sal=float(input("digite o salário"))
    if sal>2500:
        cont2500=cont2500+1
    else:
        if sal<1300:
            cont1300=cont1300+1
    total=total+sal
media=total/N
perc=cont1300*N/100
print(f"O total é {total}, a quantidade de pessoa que recebem mais que 2500 é {cont2500}, a média é {media} e o percentual é de {perc}")    
                
            