while True:
  try:
    #if y == 0:
    #  raise Exception("Voce nao pode dividir por zero")  
    idade = int(input("Digite a idade:"))
    if idade <=  0 or idade >= 955:
      raise Exception("Nao eh possivel uma idade [", idade, "]") 
 
    print("dados inseridos com Sucesse!")
    break
  except NameError:
    print("Variavel nao definida")
  except ZeroDivisionError:
    print("dividiu por zero, coleguinhe..")
  except Exception as e:
      print(e)  
      print("Erro identificado. Tente novamente... ")
  finally:
    print(" ")