import mysql
import mysql.connector
from mysql.connector import Error

#codigo = input("informe o ID :")
nome = input("informe seu nome :")
cpf =input("informe seu cpf:")
endereco = input("informe seu endereço:")
cep = input("informe seu cep:")
telefone= input("informe seu telefone:")
email= input("informe o seu email:")
senha= input("informe sua senha:")


try:
    cone = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password ='202173',
    database ='senac_lor'
    )
   
    iserir = " INSERT INTO clientes (codigo,nome,cpf,endereco,cep,telefone,email,senha) values (null,%s,%s,%s,%s,%s,%s,%s)"
    iserir2 = (nome,cpf,endereco,cep,telefone,email,senha)
    cursor = cone.cursor()
    cursor.execute(iserir,iserir2)
    cone.commit()
    print ("iserido com sucesso!")
   
    cursor.close()
    
except Error as er:
    print ("Erro: {}".format(er))

finally:
    if (cone.is_connected()):
        cone.close()
        print("Conexão com o banco de dados finalizada!")
