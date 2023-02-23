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
    con = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password ='202173',
    database ='senac_lor'
    )
   
    i = " INSERT INTO funcionarios (codigo,nome,cpf,endereco,cep,telefone,email,senha) values (null,%s,%s,%s,%s,%s,%s,%s)"
    i2 = (nome,cpf,endereco,cep,telefone,email,senha)
    cursor = con.cursor()
    cursor.execute(i,i2)
    con.commit()
    print ("iserido com sucesso!")
    
    cursor = cursor.close()
    
except Error as er:
    print ("Erro: {}".format(er))

finally:
    if (con.is_connected()):
        con.close()
        print("Conexão com o banco de dados finalizada!")
