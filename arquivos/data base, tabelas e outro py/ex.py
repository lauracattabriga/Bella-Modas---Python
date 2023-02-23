from PyQt5 import uic, QtWidgets
import mysql.connector
from mysql.connector import errorcode

conexao = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password ='202173',
    database ='senac_lor'
    )
    
    
def chama_tela_login (): #Nome da tela de login
    login.show() #Chamar a tela de menu
    
def chama_tela_login (): #Chamar tela de login

        global nome
        
        usuario = login.Usuario.text()
        senha = login.Senha.text()
        cursor= conexao.cursor()
        
        ver= ("select usuario,senha from tb_pessoas WHERE usuario = '{}' or senha='{}'",format(usuario,senha))
                       
                       
        cursor.execute(ver)
    
        for (usuario,senha)in cursor:
            if usuario == usuario or senha== senha:        
                login.hide() #fechar a tela de menu
                
    
        else:
            login.id.selText("Nome de usuario ou senha icorreta")
            
app=QtWidgets.QApplication([])
login =uic.loadUi("login.ui")

login.show()
app.exec()