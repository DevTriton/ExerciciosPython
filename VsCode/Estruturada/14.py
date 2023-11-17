"""Criar uma agenda eletrônica, em Python que armazene em uma lista nome, telefone, empresa em que trabalha. Criar um Menu com as seguintes opções:
1- Adicionar Contato
2- Excluir Contato
3- Listar todos os Contatos
4- Alterar Contato
5- Listar dados de um determinado contato
6- Sair"""
lista=[]
dados=[]
esc=0
while esc!=6:
    esc=int(input("o que deseja fazer 1-adicionar contato 2-excluir contato 3-listar todos os contatos 4-alterar contato 5-listar dados de um determinado contato 6-sair"))
    while esc<1 or esc>6:
        esc=int(input("o que deseja fazer 1-adicionar contato 2-excluir contato 3-listar todos os contatos 4-alterar contato 5-listar dados de um determinado contato 6-sair"))
    if esc>=1 and esc<=6:
            if esc==1:
                lista.append(input("digite o nome ").upper())
                lista.append(int(input("digite o telefone do usuario ")))
                lista.append(input("digite a empresa que trabalha ").upper())
            if esc==2:
                nome=input("digite o nome do contato que deseja excluir ").upper()
                while nome not in lista:
                    print("usuario não encontrado")
                    nome=input("digite o nome do contato que deseja excluir ").upper()
                if nome in lista:
                    index=lista.index(nome)
                    lista.pop(index)
                    lista.pop(index)
                    lista.pop(index)
            if esc==3:
                print(lista)
            if esc==4:
                nome=input("digite o contato que deseja alterar ").upper()
                while nome not in lista:
                    print("erro")
                    nome=input("digite o contato que deseja alterar").upper()
                if nome in lista:
                    op=int(input("oque voce deseja altera 1-nome 2-numero 3-empresa"))
                    if op==1:
                        index=lista.index(nome)
                        lista.pop(index)
                        lista.insert(index, input("digite o novo nome ").upper())
                    if op==2:
                        index=lista.index(nome+1)
                        lista.pop(index)
                        lista.insert(int(input("digite o novo telefone")))
                    if op==3:
                        index=lista.index(nome+2)
                        lista.pop(index)
                        lista.insert(input("digite o novo local de trabalho").upper())
            if esc==5:
                nome=input("digite o nome do contato que deseja listar").upper()
                while nome not in lista:
                    nome=input("digite o nome do contato que deseja listar").upper()
                if nome in lista:
                    index=lista.index(nome)
                    print(f"o nome do contato é {lista[index]} o telefone é {lista[index+1]} e o local aonde trabalha é {lista[index+2]}")