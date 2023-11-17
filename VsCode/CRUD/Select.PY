import sqlite3
# using the SQLite Table to read data.
conexao = sqlite3.connect('ModuloAcad.db')
cursor = conexao.cursor()
retorno = cursor.execute('SELECT * FROM ALUNOS;')
lista = []
for linha in retorno:
    #print(linha)
    lista.append(linha[:])
    print(lista)
#print(listaPerguntas)
conexao.close()