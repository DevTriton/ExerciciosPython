"""fazer um calculo"""
op=0
while op!=5:
	op=int(input("digite a opção desejada 1-soma 2-subtração 3-multiplicação 4-divisão 5-sair : "))
	while op<1 or op>5:
			op=int(input("digite a opção desejada 1-soma 2-subtração 3-multiplicação 4-divisão 5-sair : "))
	if op>=1 and op<=5:		
		if op==1:
			num=int(input("digite o primeiro número"))
			num2=int(input("digite o segundo número"))
			soma=num+num2
			print(f"a soma dos dois valores é {soma}")	
		if op==2:
			num=int(input("digite o primeiro número"))
			num2=int(input("digite o segundo número"))
			soma=num-num2
			print(f"O resultado da subtração dos dois valores é {soma}")
		if op==3:
			num=int(input("digite o primeiro número"))
			num2=int(input("digite o segundo número"))
			soma=num*num2
			print(f"O resultado da multiplicação dos dois valores é {soma}")
		if op==4:
			num=int(input("digite o primeiro número"))
			num2=int(input("digite o segundo número"))
			soma=num/num2
			print(f"O resultado da divisão dos dois valores é {soma}")		