import sqlite3

resp = int(input("digite o Rgm do aluno: "))

conexao = sqlite3.connect('ModuloAcad.db')
cursor = conexao.cursor()
cursor.execute(" DELETE FROM ALUNOS WHERE RGM = "+str(resp)+" ;")
conexao.commit()
conexao.close()
print("comando Inserido!!! ")