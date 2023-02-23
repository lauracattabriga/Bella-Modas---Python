from distutils.util import execute
import mysql.connector
from mysql.connector import Error

from PyQt5 import uic, QtWidgets #importa o formato do QT,com o formato  das janelhas que foram criadas.

def chama_tela_login (): #Nome da tela de login
    login.show() #Chamar a tela de menu

def chama_de_menu():
    tela_menu.show()
    login.close()
   
    
def login():
    conectando = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password ='202173',
    databese ='senac_lor')


app=QtWidgets.QApplication([])#app é referente ao nome dada para as telas do QT.

login= uic.loadUi("login.ui") #Chamar o link da tela login
tela_menu=uic.loadUi("tela_menu") #Chamar o link da tela menu

login.buttEntrarlogin.clicked.connect(chama_tela_login)#Se na tela de login o usúario clicar em Entrar vai fazer o login.

login.show()  #abrir a tela login
app.exec() #EXECUTAR AS TELAS DO QT.