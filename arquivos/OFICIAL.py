from sqlite3 import connect
from PyQt5 import uic, QtWidgets
import mysql.connector
from mysql.connector import errorcode

conexao = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password ='202173',
    database ='senac_lor'
    )

def logar (): #Chamar tela de login

    global user
     
    usua = login.Usuario.text()
    senha = login.Senha.text()
    cursor= conexao.cursor()
        
    ver= ("select nome,senha from funcionarios WHERE nome = '{}' or senha='{}'".format(usua,senha))
                       
                       
    cursor.execute(ver)
    
    for (nome,senha)in cursor:
        if usua ==''and senha=='':        
          login.Erro.setText("Nome de usuario ou senha icorreta")
        else:
            login.hide()
            menu.show()
            
def chama_cadastro_funcionario(): #inserir na tabela funcionarios os dados solicitados

    nome = cadastro_fun.Nome.text() 
    cpf = cadastro_fun.Cpf.text()
    endereco = cadastro_fun.Endereco.text()
    telefone = cadastro_fun.Telefone.text()
    cep = cadastro_fun.Cep.text()
    email = cadastro_fun.Email.text()
    senha = cadastro_fun.Senha.text()
    cursor= conexao.cursor()
    inserirdados = """INSERT INTO funcionarios (codigo, nome, cpf, endereco, cep, telefone, email, senha) values(null, %s, %s, %s, %s, %s, %s, %s)"""    
    campos_ok = (nome, cpf, endereco, cep, telefone, email, senha)
    cursor.execute(inserirdados, campos_ok)
    conexao.commit()
    cursor.close()
    
def consulta_funcionarios(): #atualizar dados na tabela funcionarios
    
    cursor=conexao.cursor()
    
    codigo=cadastro_fun.Codigo.text()
    
    if codigo == "":
        editbanco= "Select * from funcionarios"
        cursor.execute(editbanco)
        campos=cursor.fetchall()
        consultar_f.tableWidget.setRowCount(len(campos))
        consultar_f.tableWidget.setColumnCount(8)
        for l in range(len(campos)):
            for c in range(0,8):
                consultar_f.tableWidget.setItem(l,c,QtWidgets.QTableWidgetItem(str(campos[l][c])))
        cursor.close()
        cadastro_fun.hide()
        consultar_f.show()
        
    else:
        editbanco= ("Select * from funcionarios where codigo= '{}'".format(codigo))
        cursor.execute(editbanco)
        campos=cursor.fetchall()
        
        codigo= cadastro_fun.Codigo.setText(str(campos[0][0]))
        nome=cadastro_fun.Nome.setText(str(campos[0][1]))
        cpf=cadastro_fun.Cpf.setText(str(campos[0][2]))
        endereco=cadastro_fun.Endereco.setText(str(campos[0][3]))
        cep=cadastro_fun.Cep.setText(str(campos[0][4]))
        telefone=cadastro_fun.Telefone.setText(str(campos[0][5]))
        email=cadastro_fun.Email.setText(str(campos[0][6]))
        senha=cadastro_fun.Senha.setText(str(campos[0][7]))
    
def chama_cadastro_produtos():
    nome = cadastro_de_produtos.Nome.text() 
    codigo = cadastro_de_produtos.Codigo.text()
    quantidade = cadastro_de_produtos.Quantidade.text()
    colecao = cadastro_de_produtos.Colecao.text()
    marca = cadastro_de_produtos.Marca.text()
    valor = cadastro_de_produtos.Valor.text()
    tamanho = cadastro_de_produtos.Tamanho.text()
    cursor= conexao.cursor()
    inserirdados_prod = """INSERT INTO produtos (codigo, nome, id, quantidade, colecao, marca, valor,tamanho) values(null, %s, %s, %s, %s, %s, %s, %s)"""    
    campos_ok = (nome, codigo, quantidade, colecao, marca, valor,tamanho)
    cursor.execute(inserirdados_prod, campos_ok)
    conexao.commit()
    cursor.close()
    
def chama_cadastro_clientes():#inserir na tabela clientes os dados solicitados

    nome = cadastro.nome.text() 
    cpf = cadastro.cpf.text()
    endereco = cadastro.endereco.text()
    telefone = cadastro.telefone.text()
    cep = cadastro.cep.text()
    email = cadastro.email.text()
    cursor= conexao.cursor()
    inserirdados = """INSERT INTO clientes (codigo, nome, cpf, endereco, cep, telefone, email) values(null, %s, %s, %s, %s, %s, %s)"""    
    campos_ok = (nome, cpf, endereco, cep, telefone, email)
    cursor.execute(inserirdados, campos_ok)
    conexao.commit()
    cursor.close()

#Função para limpar campos na tela de cadastro de funcionários
def limp_campos_funcionarios():
    
    codigo= cadastro_fun.Codigo.setText(str())
    nome=cadastro_fun.Nome.setText(str())
    cpf=cadastro_fun.Cpf.setText(str())
    endereco=cadastro_fun.Endereco.setText(str())
    cep=cadastro_fun.Cep.setText(str())
    telefone=cadastro_fun.Telefone.setText(str())
    email=cadastro_fun.Email.setText(str())
    senha=cadastro_fun.Senha.setText(str())

def deleta_dados_funcionario(): #Deleta um registro na tabela funcionarios
    
    cursor=conexao.cursor()
    
    codigo= cadastro_fun.Codigo.text()
    
    editabanco=("DELETE from funcionarios WHERE CODIGO ='{}'".format(codigo))
    cursor.execute(editabanco)
    conexao.commit()
    cursor.close()
    
    limp_campos_funcionarios()

def update_funcionarios(): #Atualização de dados de funcionarios
   
    cursor=conexao.cursor()
    
    codigo=cadastro_fun.Codigo.text()
    nome=cadastro_fun.Nome.text()
    cpf=cadastro_fun.Cpf.text()
    endereco=cadastro_fun.Endereco.text()
    cep=cadastro_fun.Cep.text()
    telefone=cadastro_fun.Telefone.text()
    email=cadastro_fun.Email.text()
    senha=cadastro_fun.Senha.text()
    
    editbanco=("UPDATE funcionarios SET nome='{}', cpf='{}', endereco='{}', cep='{}', telefone='{}', email='{}', senha='{}' where codigo = '{}' ".format(nome, cpf, endereco, cep, telefone, email, senha, codigo))
    cursor.execute(editbanco)
    conexao.commit()
    cursor.close()

    limp_campos_funcionarios()   
    
# TRANSIÇÕES DE TELAS 
def chama_cadastro_fun():
    consultar_f.close()
    cadastro_fun.show()
    menu.close()
    cadastro_fun.show()

def fechar_tela_de_cadastro_fun():
    consulta_f.close()
    cadastro_fun.show()

def chama_de_menu():
    login.close()
    estoque.close()
    cadastro_com_sucesso.close()
    menu.show()

def chama_tela_de_cadastro1():
    login.close()
    cadastro_fun.show()
    
def chama_tela_de_cadastro():
    login.close()
    cadastro.show()

def chama_tela_de_estoque():
    menu.close()
    estoque.show()
    finalizar_compras.close()
    
def chama_tela_cadastro():
    menu.close()
    cadastro.show()
    
def voltar_tela_menu():
    cadastro.close()
    menu.show()
    compra_realizada.close()
    menu.show()
    finalizar_compras.show()
    menu.show()
    cadastro_de_produtos.close()
    menu.show()
    finalizar_compras.close()
    menu.show()
    
def troca_de_usuario():
    cadastro.close()
    menu.close()
    login.show()
    
def fecha_tela_de_fu():
    cadastro_fun.close()
    menu.show()
    
def cadastro_sucesso():
    cadastro.close()
    cadastro_com_sucesso.show()
    cadastro_de_produtos.close()
    cadastro_com_sucesso.show()

def abrir_tela_cadastrar_produtos():
    estoque.close()
    cadastro_de_produtos.show()

def close():
    menu.close()

def finalizar_compra():
    finalizar_compras.close()
    finalizar_compras.show()

def venda_realizada():
    compra_realizada.show()
    finalizar_compras.close()

def tela_login():
    cadastro_fun.close()
    login.show()
    
def Voltar_2():
    menu.hide()
    login.show()

app=QtWidgets.QApplication([])

login= uic.loadUi("login.ui")
menu=uic.loadUi("tela_menu.ui")
cadastro=uic.loadUi("tela_cadastro.ui")
cadastro_com_sucesso=uic.loadUi("tela_cadastrado_com_sucesso.ui")
estoque=uic.loadUi("tela_de_estoque.ui")
compra_realizada=uic.loadUi("tela_venda_realizada.ui")
cadastro_de_produtos=uic.loadUi("cadastrodeprodutos.ui")
finalizar_compras=uic.loadUi("finalizarvenda.ui")
cadastro_fun=uic.loadUi("cadastrofuncionario.ui")
consultar_f=uic.loadUi("consulta_f.ui")




#botões tela de menu
menu.Voltar.clicked.connect(Voltar_2)
menu.Cadastrodeclientes.clicked.connect(chama_tela_cadastro)
menu.Iniciarvendas.clicked.connect(finalizar_compra)
menu.Estoque.clicked.connect(chama_tela_de_estoque)
menu.Trocardeusuario.clicked.connect(troca_de_usuario)
menu.Sair.clicked.connect(close)
menu.Funcionarios.clicked.connect(chama_cadastro_fun)

#botões tela de login
login.Senha.setEchoMode(QtWidgets.QLineEdit.Password)
login.Entrar.clicked.connect(logar)


#botões tela de cadastro de cliente
cadastro.Voltar.clicked.connect(chama_de_menu)
cadastro.Voltar.clicked.connect(voltar_tela_menu)
cadastro.Cadastrar.clicked.connect(cadastro_sucesso)
cadastro.Cadastrar.clicked.connect(chama_cadastro_clientes)
cadastro_com_sucesso.Voltar.clicked.connect(chama_de_menu)


#botões tela de cadastro de fúncionario
cadastro_fun.Cadastrar.clicked.connect(chama_cadastro_fun)
cadastro_fun.Voltar.clicked.connect(fecha_tela_de_fu)
cadastro_fun.Cadastrar.clicked.connect(chama_cadastro_funcionario)#chamar tela de cadastro pra ser feito o cadastro do funcionario.
cadastro_fun.Cadastrar.clicked.connect(cadastro_sucesso)
cadastro_fun.Consultar.clicked.connect(consulta_funcionarios)#não funcional como o desejado (voltar pra olhar)
cadastro_fun.Deletar.clicked.connect(deleta_dados_funcionario)
cadastro_fun.Limpar_campos.clicked.connect(limp_campos_funcionarios)
cadastro_fun.Alterar.clicked.connect(update_funcionarios)

#botões tela de estoque
estoque.Voltar.clicked.connect(chama_de_menu)
estoque.Cadastrodeprodutos.clicked.connect(abrir_tela_cadastrar_produtos)

#botões tela de cadastro de produto
cadastro_de_produtos.Cadastrar.clicked.connect(cadastro_sucesso)
cadastro_de_produtos.Voltar.clicked.connect(voltar_tela_menu)
cadastro_de_produtos.Cadastrar.clicked.connect(chama_cadastro_produtos)
compra_realizada.Voltaraomenuprincipal.clicked.connect(voltar_tela_menu)


#botões tela de venda finalizada com sucesso
finalizar_compras.Finalizarcompra.clicked.connect(venda_realizada)
finalizar_compras.Sair.clicked.connect(voltar_tela_menu)


#botões tela do banco de dados dos funcionários
consultar_f.Voltar.clicked.connect(chama_cadastro_fun)

  
login.show()
app.exec()