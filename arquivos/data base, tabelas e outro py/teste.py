from sqlite3 import connect
from PyQt5 import uic, QtWidgets
import mysql.connector
from mysql.connector import errorcode



conexao = mysql.connector.connect(  #conexao do banco de dados.
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
    
    for (usua,senha)in cursor:
        if usua ==''and senha=='':        
          login.Erro.setText("Nome de usuario ou senha icorreta")
        else:
            login.hide()
            menu.show()
            
def chama_cadastro_funcionario(): #chamar tela de cadastro de funcionarioww

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
    
    cadastro_sucesso()

def consultar_funcionarios(): # consulta na tabela funcionarios
    
    cursor= conexao.cursor()
    consulta = "SELECT * from funcionarios "
    cursor.execute(consulta)
    campos= cursor.fetchall()
    consulta_f.tableWidget.setRowCount(len(campos))
    consulta_f.tableWidget.setColumnCount(8)
    for l in range(len(campos)):
        for c in range(0,8):
            consulta_f.tableWidget.setItem(l, c, QtWidgets.QTableWidgetItem(str(campos[l][c])))
    cursor.close()
    cadastro_fun.close()
    consulta_f.show()
    
    chama_cadastro_funcionario()

def  chama_cadastro_fun():
    consulta_f.close()
    cadastro_fun.show()
    
def fechar_tela_de_cadastro_fun():
    consulta_f.close()
    cadastro_fun.show()
   
def alter_funcionarios(): # alteração de dados da tabela funcionários
    nome = cadastro_fun.Nome.text() 
    cpf = cadastro_fun.Cpf.text()
    endereco = cadastro_fun.Endereco.text()
    telefone = cadastro_fun.Telefone.text()
    cep = cadastro_fun.Cep.text()
    email = cadastro_fun.Email.text()
    senha = cadastro_fun.Senha.text()
    cursor= conexao.cursor()
    alterar = """UPDATE funcionarios SET cpf='{}', endereco='{}', cep='{}', telefone='{}', email='{}', senha='{}'.format(codigo, nome, cpf, endereco, cep, telefone, email, senha)"""    
    campos_ok = (nome, cpf, endereco, cep, telefone, email, senha)
    cursor.execute(alterar,campos_ok)
    conexao.commit()
 
    
    cadastro_sucesso()
        
def chama_cadastro_prod(): #chamar a tela de cadastro de produto

    nome = cadastro_de_produtos.Nome.text() 
    codigo= cadastro_de_produtos.Codigo.text()
    quantidade = cadastro_de_produtos.Quantidade.text()
    colecao = cadastro_de_produtos.Colecao.text()
    marca = cadastro_de_produtos.Marca.text()
    valor = cadastro_de_produtos.Valor.text()
    tamanho = cadastro_de_produtos.Tamanho.text()
    cursor= conexao.cursor()
    
    inserirdados_1 = """INSERT INTO produtos (codigo, nome, id, quantidade, colecao, marca, valor, tamanho) values(null, %s, %s, %s, %s, %s,%s, %s)"""   # adicina os dados na tabela produtos
    campos_ok = (nome, codigo, quantidade, colecao, marca, valor, tamanho)
    cursor.execute(inserirdados_1, campos_ok)
    conexao.commit()
    cursor.close()
    
    cadastro_sucesso()
    
def chama_cadastro_cliente():#chamar a tela de cadastro de cliente

    
    nome = cadastro.nome.text() 
    cpf = cadastro.cpf.text()
    endereco = cadastro.endereco.text()
    cep = cadastro.cep.text()
    telefone = cadastro.telefone.text()
    email = cadastro.email.text()
    
    cursor= conexao.cursor()
    
    inser= """INSERT INTO clientes (codigo, nome, cpf, endereco, cep, telefone, email) values(null, %s, %s, %s, %s, %s, %s)"""    
    campos = (nome, cpf, endereco, cep, telefone, email)
    
    cursor.execute(inser, campos)
    conexao.commit()
    
    cadastro_sucesso()

def chama_de_menu():
    login.close()
    estoque.close()
    cadastro_com_sucesso.close()
    menu.show()
    cadastro_fun.close()
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
    vendas.close()
    
def chama_tela_cadastro():
    menu.close()
    cadastro.show()
    
def voltar_tela_menu():
    cadastro.close()
    menu.show()
    compra_realizada.close()
    menu.show()
    vendas.close()
    menu.show()
    cadastro_de_produtos.close()
    menu.show()
    finalizar_compras.close()
    menu.show()

def troca_de_usuario():
    cadastro.close()
    menu.close()
    login.show()
        
def tela_de_vendas():
    estoque.close()
    menu.close()
    vendas.show()

def tela_finalizar():
    vendas.close()
    compra_realizada.show()

def cadastro_sucesso():
    cadastro.close()
    cadastro_com_sucesso.show()
    cadastro_de_produtos.close()
    cadastro_com_sucesso.close()
    
def cadastrar_produtos():
    estoque.close()
    cadastro_de_produtos.show()

def close():
    menu.close()

def finalizar_compra():
    vendas.close()
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
vendas=uic.loadUi("tela_iniciar_vendas.ui")
compra_realizada=uic.loadUi("tela_venda_realizada.ui")
cadastro_de_produtos=uic.loadUi("cadastrodeprodutos.ui")
finalizar_compras=uic.loadUi("finalizarvenda.ui")
cadastro_fun=uic.loadUi("cadastrofuncionario.ui")
consulta_f=uic.loadUi("consulta_f.ui")





menu.Voltar.clicked.connect(Voltar_2)
menu.Cadastrodeclientes.clicked.connect(chama_tela_cadastro)
login.cadastrar_1.clicked.connect(chama_tela_de_cadastro1)
login.Senha.setEchoMode(QtWidgets.QLineEdit.Password)
menu.Iniciarvendas.clicked.connect(tela_de_vendas)
cadastro.Voltar.clicked.connect(chama_de_menu)
cadastro.Voltar.clicked.connect(voltar_tela_menu)
cadastro.Cadastrar.clicked.connect(chama_cadastro_cliente)
cadastro_com_sucesso.Voltar.clicked.connect(chama_de_menu)
cadastro_fun.Alterar.clicked.connect(alter_funcionarios)
cadastro_fun.Voltar.clicked.connect(tela_login)
menu.Estoque.clicked.connect(chama_tela_de_estoque)
estoque.Voltar.clicked.connect(chama_de_menu)
estoque.Cadastrodeprodutos.clicked.connect(cadastrar_produtos)
cadastro_de_produtos.Cadastrar.clicked.connect(chama_cadastro_prod)
cadastro_de_produtos.Voltar.clicked.connect(voltar_tela_menu)
vendas.Voltar.clicked.connect(voltar_tela_menu)
vendas.Teladecompra.clicked.connect(finalizar_compra)
finalizar_compras.Finalizarcompra.clicked.connect(venda_realizada)
compra_realizada.Voltaraomenuprincipal.clicked.connect(voltar_tela_menu)
finalizar_compras.Sair.clicked.connect(voltar_tela_menu)
menu.Trocardeusuario.clicked.connect(troca_de_usuario)
menu.Sair.clicked.connect(close)
login.Entrar.clicked.connect(logar)
cadastro_fun.Consultar.clicked.connect(consultar_funcionarios)




login.Entrar.clicked.connect(logar)


cadastro_fun.Cadastrar.clicked.connect(chama_cadastro_funcionario)#chamar tela de cadastro pra ser feito o cadastro do funcionario.
consulta_f.Voltar.clicked.connect(chama_cadastro_fun)


login.show()
app.exec()

        
            
app=QtWidgets.QApplication([])
login =uic.loadUi("login.ui")

login.show()
app.exec()


    vendas.close()
           
def tela_de_vendas():
    estoque.close()
    menu.close()
    vendas.show()

def tela_finalizar():
    vendas.close()
    compra_realizada.show()
vendas=uic.loadUi("tela_iniciar_vendas.ui")
vendas.Voltar.clicked.connect(voltar_tela_menu)
vendas.Teladecompra.clicked.connect(finalizar_compra)

def alter_funcionarios(): # alteração de dados da tabela funcionários
    nome = cadastro_fun.Nome.text() 
    cpf = cadastro_fun.Cpf.text()
    endereco = cadastro_fun.Endereco.text()
    telefone = cadastro_fun.Telefone.text()
    cep = cadastro_fun.Cep.text()
    email = cadastro_fun.Email.text()
    senha = cadastro_fun.Senha.text()
    cursor= conexao.cursor()
    alterar = """UPDATE funcionarios SET cpf='{}', endereco='{}', cep='{}', telefone='{}', email='{}', senha='{}'.format(codigo, nome, cpf, endereco, cep, telefone, email, senha)"""    
    campos_ok = (nome, cpf, endereco, cep, telefone, email, senha)
    cursor.execute(alterar,campos_ok)
    conexao.commit()
    
    
    
    
    #con
def consulta_produto():
   
    cursor=con.cursor()
    
    codigo=conprodutos.ent_cod.text()
    
    if codigo =="":
        editbanco= "Select * from produtos"
        cursor.execute(editbanco)
        campos=cursor.fetchall()
        tbprodutos.tableWidget.setRowCount(len(campos))
        tbprodutos.tableWidget.setColumnCount(6)
        for l in range(len(campos)):
            for c in range(0,6):
                tbprodutos.tableWidget.setItem(l,c,QtWidgets.QTableWidgetItem(str(campos[l][c])))
        cursor.close()
        tbprodutos.show()
        conprodutos.hide()
    else:
    editbanco= ("Select * from produtos where codigo= '{}'".format(codigo))
    cursor.execute(editbanco)
    campos=cursor.fetchall()
        
    nome=conprodutos.ent_nome.setText(str(campos[0][1]))
    quantidade=conprodutos.ent_qt.setText(str(campos[0][2]))
    preco_kg=conprodutos.ent_pr.setText(str(campos[0][3]))
    preco_total=conprodutos.ent_prt.setText(str(campos[0][4]))
    fornecedor=conprodutos.ent_for.setText(str(campos[0][5]))















def consulta_produto():
   
    cursor=con.cursor()
    
    codigo=conprodutos.ent_cod.text()
    
    if codigo =="":
        editbanco= "Select * from produtos"
        cursor.execute(editbanco)
        campos=cursor.fetchall()
        tbprodutos.tableWidget.setRowCount(len(campos))
        tbprodutos.tableWidget.setColumnCount(6)
        for l in range(len(campos)):
            for c in range(0,6):
                tbprodutos.tableWidget.setItem(l,c,QtWidgets.QTableWidgetItem(str(campos[l][c])))
        cursor.close()
        tbprodutos.show()
        conprodutos.hide()
        
    else:
        editbanco= ("Select * from produtos where codigo= '{}'".format(codigo))
        cursor.execute(editbanco)
        campos=cursor.fetchall()
        
        nome=conprodutos.ent_nome.setText(str(campos[0][1]))
        quantidade=conprodutos.ent_qt.setText(str(campos[0][2]))
        preco_kg=conprodutos.ent_pr.setText(str(campos[0][3]))
        preco_total=conprodutos.ent_prt.setText(str(campos[0][4]))
        fornecedor=conprodutos.ent_for.setText(str(campos[0][5]))





cadastro_fun.Consultar.clicked.connect(consultar_funcionarios)
def consultar_funcionarios(): # consulta na tabela funcionarios
       
    cursor= conexao.cursor()
    consulta = "SELECT * from funcionarios "
    cursor.execute(consulta)
    campos= cursor.fetchall()
    consulta_f.tableWidget.setRowCount(len(campos))
    consulta_f.tableWidget.setColumnCount(8)
    for l in range(len(campos)):
        for c in range(0,7):
            consulta_f.tableWidget.setItem(l, c, QtWidgets.QTableWidgetItem(str(campos[l][c])))
    cursor.close()
    cadastro_fun.close()
    consulta_f.show()
    
    chama_cadastro_funcionario()
    
    
    
    
        else:
        editbanco= ("Select * from produtos where codigo= '{}'".format(codigo))
        cursor.execute(editbanco)
        campos=cursor.fetchall()
        
        codigo=cadastro_fun.Codigo.setText((str(campos[0][0]))
        =cadastro_fun.Nome.setText(str(campos[0][1]))
                =cadastro_fun.Cpf.setText(str(campos[0][2]))
                =cadastro_fun.Endereco.setText(str(campos[0][3]))
                =cadastro_fun.Cep.setText(str(campos[0][4]))
                =cadastro_fun.Telefone.setText(str(campos[0][5]))
                =cadastro_fun.Email.setText(str(campos[0][6]))
                =cadastro_fun.Senha.setText(str(campos[0][7]))
        
    
    
    
    
    def update_produtos():
    cursor=con.cursor()
    
    codigo=conprodutos.ent_cod.text()
    nome=conprodutos.ent_nome.text()
    quantidade=conprodutos.ent_qt.text()
    preco_kg=conprodutos.ent_pr.text()
    preco_total=conprodutos.ent_prt.text()
    fornecedor=conprodutos.ent_for.text()
    
    editbanco=("UPDATE produtos SET nome='{}',quantidade='{}',preco_kg='{}',preco_total='{}',fornecedor='{}' where codigo= '{}'".format(nome,quantidade,preco_kg,preco_total,fornecedor,codigo))
    cursor.execute(editbanco)
    con.commit()
    cursor.close()

    limp_campconsulta()