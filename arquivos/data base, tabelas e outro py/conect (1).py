import mysql.connector
from mysql.connector import errorcode

try:
	db_connection = mysql.connector.connect(
   host='localhost',
   user='root', 
   password='', 
   database='senac_lor')
	print("Conexão realizada com sucesso!")

except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Tabela não existe")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Usuario ou senha incorreta")
	else:
		print(error)
else:
	db_connection.close()


from mysql.connector import (connection)
db_connection = connection.MySQLConnection(
  host='127.0.0.1', 
  user='root',
  password='',
  database='senac_lor')
db_connection.close()