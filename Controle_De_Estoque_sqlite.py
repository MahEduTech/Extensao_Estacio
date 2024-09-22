import sqlite3

banco = sqlite3.connect('Controle_De_Estoque.db')

cursor = banco.cursor()

cursor.execute ("CREATE TABLE vendas (nome text)")

cursor.execute ("INSERT INTO vendas VALUES('Marieta')")

banco.commit()

#cursor. execute ("SELECT * FROM PRODUTOS")
#print(cursor.fetchall())

