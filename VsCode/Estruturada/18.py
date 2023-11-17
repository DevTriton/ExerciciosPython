fun2500=0
fun1300=0
total=0
N=int(input("digite o numero de funcionarios: "))
while N<=0:
    print("erro")
    N=int(input("digite o numero de funcionarios: "))
for cont in range(N):
    sal=float(input(f"digite o {cont+1} salario"))
    while sal<=0:
        print("erro")
        sal=float(input(f"digite o {cont+1} salario"))
    total=total+sal    
    if sal>2500:
        fun2500=fun2500+1
    else:
        if sal<1300:
            fun1300=fun1300+1
perc=(fun1300*N)/100
media=total/N
print(f"o total é {total}, a quantidade de funcionarios que recebem mais de 2500 são {fun2500}, a média é {media} e o percentual de pessoas que recebem menos que 1300 é {perc}")