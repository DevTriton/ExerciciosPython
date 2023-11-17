import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bdyoutube',
)   

cursor = conexao.cursor()

cursor.execute("INSERT INTO Vendas (nome_prod, valor) VALUES ('arroz', "+str(18)+"); ")
conexao.commit()

cursor.close()
conexao.close()

print("feito")