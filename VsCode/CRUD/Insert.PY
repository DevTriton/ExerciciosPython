import sqlite3
# using the SQLite Table to read data.
conexao = sqlite3.connect('ModuloAcad.db')
cursor = conexao.cursor()
cursor.execute("INSERT INTO ALUNOS (NOME, IDADE, ALTURA, PESO, RGM, ID) VALUES ('Eddie', 19, 1.86, 100, 11231102940, 1); ")
conexao.commit()
conexao.close()
print("comando Inserido!!! ")