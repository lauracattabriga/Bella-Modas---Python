import mysql
import mysql.connector
from mysql.connector import Error

#codigo = input("informe o ID do produto:")
nome = input("informe o nome do produto:")
quantidade =input("informe a quantidade:")
colecao = input("informe qual coleção:")
marca = input("informe a marca do produto:")
valor= input("informe o valor:")
tamanho= input("informe o tamanho:")

try:
    conectando = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password ='202173',
    database ='senac_lor'
    )
   
    iserir = " INSERT INTO produtos (codigo,nome,quantidade,colecao,marca,valor,tamanho) values (null,%s,%s,%s,%s,%s,%s)"
    iserir2 = (nome,quantidade,colecao,marca,valor,tamanho)
    cursor = conectando.cursor()
    cursor.execute(iserir,iserir2)
    conectando.commit()
    print ("iserido com sucesso!")
   
    cursor = cursor.close()
    
except Error as er:
    print ("Erro: {}".format(er))

finally:
    if (conectando.is_connected()):
        conectando.close()
        print("Conexão com o banco de dados finalizada!")
