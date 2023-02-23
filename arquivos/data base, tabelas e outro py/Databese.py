from distutils.util import execute
import mysql.connector
from mysql.connector import Error

try:
    conectando = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password ='202173',
    databese ='senac_lor')


    iserir = """ INSERT INTO produtos (
        codigo,
        nome,
        quantidade,
        colecao,
        marca,
        valor)
        values (null,'Calça',100,'Inverno','DZ',80.00)
        """

    cursor = conectando.cursor()
    cursor = execute (iserir)
    conectando.commit()
    print ("iserido com sucesso!")

    cursor.close()
 
except Error as error:
    print ("Erro: {}".format(error))

finally:
    if (conectando.is_connected()):
        conectando.close()
        print("Conexão ao Mysql.")

