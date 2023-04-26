from crypt import methods
import os
import json
import psycopg2
from flask import Flask, render_template, jsonify, request, url_for, redirect

# ...

app = Flask(__name__)

def get_db_connection():
    db_connection = psycopg2.connect(host="containers-us-west-10.railway.app",database="railway",port="6830",user="postgres",password="kda3MBPqZdjCNqSNRDTZ")
    return db_connection

@app.route('/cadastra_administrador', methods=["POST"])
def cadastra_administrador():
    novo_administrador_dict = json.loads(json.dumps(request.get_json()))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM administrador;')
    administradores = cur.fetchall()
   # print(type(len(administradores)))
    cur.execute("INSERT INTO administrador VALUES("
                +str(len(administradores)+1)
                +",'"+novo_administrador_dict['celular_administrador']
                +"','"+novo_administrador_dict['endereco_administrador']
                +"','"+novo_administrador_dict['nome_administrador']
                +"','"+novo_administrador_dict['password_administrador']
                +"','"+novo_administrador_dict['username_administrador']
                +"');")
    
    cur.execute('SELECT * FROM administrador;')
    administradores = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return administradores

@app.route('/lista_administradores', methods=["GET"])
def lista_administradores():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM administrador;')
    administradores = cur.fetchall()

    cur.close()
    connection.close()
    #print(administradores)
    #render_template('lista_administradores.html', administradores=administradores)

    return jsonify(administradores)

@app.route('/edita_administrador_por_id/<int:id>', methods=["POST"])
def edita_administrador_por_id(id):
    administrador_alterado_dict = json.loads(json.dumps(request.get_json()))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM administrador;')
    administradores = cur.fetchall()

    for administrador in administradores:
        if administrador[0] == id:  #administrador[0] pega o id dos administradores
            cur.execute("UPDATE administrador SET id_administrador="+str(administrador_alterado_dict['id_administrador'])
                        +",celular_administrador='"+administrador_alterado_dict['celular_administrador']
                        +"',nome_administrador='"+administrador_alterado_dict['nome_administrador']
                        +"',password_administrador='"+administrador_alterado_dict['password_administrador']
                        +"',username_administrador='"+administrador_alterado_dict['username_administrador']
                        +"' WHERE id_administrador = "+str(id)+";")
    
    cur.execute('SELECT * FROM administrador;')
    administradores = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return administradores

@app.route('/deleta_administrador_por_id', methods=["POST"])
def deleta_administrador_por_id():
    id_deleta_administrador = request.get_json()
    print(id_deleta_administrador)
    print(type(id_deleta_administrador))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM administrador;')
    administradores = cur.fetchall()

    for administrador in administradores:
        if administrador[0] == id_deleta_administrador:
            cur.execute("DELETE FROM administrador WHERE id_administrador = "+str(id_deleta_administrador)+";")

    cur.execute('SELECT * FROM administrador;')
    administradores = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return administradores

@app.route('/deleta_administrador_por_nome', methods=["POST"])
def deleta_administrador_por_nome():
    nome_deleta_administrador = request.get_json()
    print(nome_deleta_administrador)
    print(type(nome_deleta_administrador))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM administrador;')
    administradores = cur.fetchall()

    for administrador in administradores:
        print("pesquisando por: "+str(administrador[3]).split()[0].lower()) # só aceita 1 nome com letra minuscula
        if str(administrador[3]).split()[0].lower() == str(nome_deleta_administrador).split()[0].lower():
            cur.execute("DELETE FROM administrador WHERE nome_administrador = '"+str(nome_deleta_administrador).split()[0].lower()+"';")

    cur.execute('SELECT * FROM administrador;')
    administradores = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return administradores


###############################################################################################
#CLIENTES

@app.route('/cadastra_cliente', methods=["POST"])
def cadastra_cliente():
    novo_cliente_dict = json.loads(json.dumps(request.get_json()))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM cliente;')
    clientes = cur.fetchall()
   # print(type(len(clientes)))
    cur.execute("INSERT INTO cliente VALUES("
                +str(len(clientes)+1)
                +",'"+novo_cliente_dict['celular_clientes']
                +"','"+novo_cliente_dict['endereco_clientes']
                +"','"+novo_cliente_dict['nome_clientes']
                +"','"+novo_cliente_dict['password_clientes']
                +"','"+novo_cliente_dict['username_clientes']
                +"');")
    
    cur.execute('SELECT * FROM cliente;')
    clientes = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return clientes

@app.route('/lista_clientes', methods=["GET"])
def lista_clientes():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM cliente;')
    clientes = cur.fetchall()

    cur.close()
    connection.close()
    #print(clientes)
    #render_template('lista_clientes.html', clientes=clientes)

    return jsonify(clientes)

@app.route('/edita_cliente_por_id/<int:id>', methods=["POST"])
def edita_cliente_por_id(id):
    cliente_alterado_dict = json.loads(json.dumps(request.get_json()))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM cliente;')
    cliente = cur.fetchall()

    for cliente in cliente:
        if cliente[0] == id:  #cliente[0] pega o id dos clientes
            cur.execute("UPDATE cliente SET id_cliente="+str(cliente_alterado_dict['id_cliente'])
                        +",celular_cliente='"+cliente_alterado_dict['celular_cliente']
                        +"',nome_cliente='"+cliente_alterado_dict['nome_cliente']
                        +"',password_cliente='"+cliente_alterado_dict['password_cliente']
                        +"',username_cliente='"+cliente_alterado_dict['username_cliente']
                        +"' WHERE id_cliente = "+str(id)+";")
    
    cur.execute('SELECT * FROM cliente;')
    clientes = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return clientes

@app.route('/deleta_cliente_por_id', methods=["POST"])
def deleta_cliente_por_id():
    id_deleta_cliente = request.get_json()
    print(id_deleta_cliente)
    print(type(id_deleta_cliente))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM cliente;')
    clientes = cur.fetchall()

    for cliente in clientes:
        if cliente[0] == id_deleta_cliente:
            cur.execute("DELETE FROM cliente WHERE id_cliente = "+str(id_deleta_cliente)+";")

    cur.execute('SELECT * FROM cliente;')
    clientes = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return clientes

@app.route('/deleta_cliente_por_nome', methods=["POST"])
def deleta_cliente_por_nome():
    nome_deleta_cliente = request.get_json()
    print(nome_deleta_cliente)
    print(type(nome_deleta_cliente))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM cliente;')
    clientes = cur.fetchall()

    for cliente in clientes:
        print("pesquisando por: "+str(cliente[3]).split()[0].lower()) # só aceita 1 nome com letra minuscula
        if str(cliente[3]).split()[0].lower() == str(nome_deleta_cliente).split()[0].lower():
            cur.execute("DELETE FROM cliente WHERE nome_cliente = '"+str(nome_deleta_cliente).split()[0].lower()+"';")

    cur.execute('SELECT * FROM cliente;')
    clientes = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return clientes


###############################################################################################
#PRODUTOS

@app.route('/cadastra_produto', methods=["POST"])
def cadastra_produto():
    novo_produto_dict = json.loads(json.dumps(request.get_json()))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM produto;')
    produtos = cur.fetchall()
   # print(type(len(produtos)))
    cur.execute("INSERT INTO produto VALUES("
                +str(len(produtos)+1)
                +",'"+novo_produto_dict['id_produto']
                +"','"+novo_produto_dict['descricao_produto']
                +"','"+novo_produto_dict['imagem']
                +"','"+novo_produto_dict['modelo_marca_produto']
                +"','"+novo_produto_dict['nome_produto']
                +"','"+novo_produto_dict['path_imagem_produto']
                +"','"+novo_produto_dict['preco_revenda_unidade']
                +"');")
    
    cur.execute('SELECT * FROM produto;')
    produtos = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return produtos

@app.route('/lista_produtos', methods=["GET"])
def lista_produtos():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM produto;')
    produtos = cur.fetchall()

    cur.close()
    connection.close()
    #print(produtos)
    #render_template('lista_produtos.html', produtos=produtos)

    return jsonify(produtos)

@app.route('/edita_produto_por_id/<int:id>', methods=["POST"])
def edita_produto_por_id(id):
    produto_alterado_dict = json.loads(json.dumps(request.get_json()))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM produto;')
    produtos = cur.fetchall()

    for produto in produtos:
        if produto[0] == id:  #produto[0] pega o id dos produtos
            cur.execute("UPDATE produto SET id_produto="+str(produto_alterado_dict['id_produto'])
                        +",descricao_produto='"+produto_alterado_dict['descricao_produto']
                        +"',imagem='"+produto_alterado_dict['imagem']
                        +"',modelo_marca_produto='"+produto_alterado_dict['modelo_marca_produto']
                        +"',nome_produto='"+produto_alterado_dict['nome_produto']
                        +"',path_imagem_produto='"+produto_alterado_dict['path_imagem_produto']
                        +"',preco_revenda_unidade='"+produto_alterado_dict['preco_revenda_unidade']
                        +"' WHERE id_produto = "+str(id)+";")
    
    cur.execute('SELECT * FROM produto;')
    produtos = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return produtos

@app.route('/deleta_produto_por_id', methods=["POST"])
def deleta_produto_por_id():
    id_deleta_produto = request.get_json()
    print(id_deleta_produto)
    print(type(id_deleta_produto))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM produto;')
    produtos = cur.fetchall()

    for produto in produtos:
        if produto[0] == id_deleta_produto:
            cur.execute("DELETE FROM produto WHERE id_produto = "+str(id_deleta_produto)+";")

    cur.execute('SELECT * FROM produto;')
    clientes = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return produtos


###############################################################################################
#SERVIÇOS

@app.route('/cadastra_servico', methods=["POST"])
def cadastra_servico():
    novo_servico_dict = json.loads(json.dumps(request.get_json()))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM servico;')
    servicos = cur.fetchall()
   # print(type(len(servicos)))
    cur.execute("INSERT INTO servico VALUES("
                +str(len(servicos)+1)
                +",'"+novo_servico_dict['id_servico']
                +"','"+novo_servico_dict['data_abertura_servico']
                +"','"+novo_servico_dict['descricao_servico']
                +"','"+novo_servico_dict['disposicao_layout_generico']
                +"','"+novo_servico_dict['disposicao_remoto_servico']
                +"','"+novo_servico_dict['id_estrangeiro_administrador']
                +"','"+novo_servico_dict['id_estrangeiro_cliente']
                +"','"+novo_servico_dict['nome_estrangeiro_administrador']
                +"','"+novo_servico_dict['nome_estrangeiro_cliente']
                +"','"+novo_servico_dict['preco_servico']
                +"','"+novo_servico_dict['status_servico']
                +"','"+novo_servico_dict['tipo_dispositivo_servico']
                +"','"+novo_servico_dict['tipo_plataforma_sistema']
                +"','"+novo_servico_dict['titulo_servico']
                +"');")
    
    cur.execute('SELECT * FROM servico;')
    servicos = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return servicos

@app.route('/lista_servicos', methods=["GET"])
def lista_servicos():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM servico;')
    servicos = cur.fetchall()

    cur.close()
    connection.close()
    #print(servicos)
    #render_template('lista_servicos.html', servicos=servicos)

    return jsonify(servicos)

@app.route('/edita_servico_por_id/<int:id>', methods=["POST"])
def edita_servico_por_id(id):
    servico_alterado_dict = json.loads(json.dumps(request.get_json()))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM servico;')
    servicos = cur.fetchall()

    for servico in servicos:
        if servico[0] == id:  #servico[0] pega o id dos servicos
            cur.execute("UPDATE servico SET id_servico="+str(servico_alterado_dict['id_servico'])
                        +",data_abertura_servico='"+servico_alterado_dict['data_abertura_servico']
                        +"',descricao_servico='"+servico_alterado_dict['descricao_servico']
                        +"',disposicao_layout_generico='"+servico_alterado_dict['disposicao_layout_generico']
                        +"',disposicao_remoto_servico='"+servico_alterado_dict['disposicao_remoto_servico']
                        +"',id_estrangeiro_administrador='"+servico_alterado_dict['id_estrangeiro_administrador']
                        +"',id_estrangeiro_cliente='"+servico_alterado_dict['id_estrangeiro_cliente']
                        +"',nome_estrangeiro_administrador='"+servico_alterado_dict['nome_estrangeiro_administrador']
                        +"',nome_estrangeiro_cliente='"+servico_alterado_dict['nome_estrangeiro_cliente']
                        +"',preco_servico='"+servico_alterado_dict['preco_servico']
                        +"',status_servico='"+servico_alterado_dict['status_servico']
                        +"',tipo_dispositivo_servico='"+servico_alterado_dict['tipo_dispositivo_servico']
                        +"',tipo_plataforma_sistema='"+servico_alterado_dict['tipo_plataforma_sistema']
                        +"',titulo_servico='"+servico_alterado_dict['titulo_servico']
                        +"' WHERE id_servico = "+str(id)+";")
    
    cur.execute('SELECT * FROM servico;')
    servicos = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return servicos

@app.route('/deleta_servico_por_id', methods=["POST"])
def deleta_servico_por_id():
    id_deleta_servico = request.get_json()
    print(id_deleta_servico)
    print(type(id_deleta_servico))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM servico;')
    servicos = cur.fetchall()

    for servico in servicos:
        if servico[0] == id_deleta_servico:
            cur.execute("DELETE FROM servico WHERE id_servico = "+str(id_deleta_servico)+";")

    cur.execute('SELECT * FROM servico;')
    servicos = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return servicos

###############################################################################################
#VENDAS

@app.route('/cadastra_venda', methods=["POST"])
def cadastra_venda():
    novo_venda_dict = json.loads(json.dumps(request.get_json()))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM venda;')
    vendas = cur.fetchall()
   # print(type(len(vendas)))
    cur.execute("INSERT INTO venda VALUES("
                +str(len(vendas)+1)
                +",'"+novo_venda_dict['id_venda']
                +"','"+novo_venda_dict['customizacao_venda']
                +"','"+novo_venda_dict['id_estrangeiro_cliente']
                +"','"+novo_venda_dict['id_estrangeiro_produto']
                +"','"+novo_venda_dict['nome_estrangeiro_cliente']
                +"','"+novo_venda_dict['nome_estrangeiro_produto']
                +"','"+novo_venda_dict['observacao_venda']
                +"','"+novo_venda_dict['quant_item_venda']
                +"');")
    
    cur.execute('SELECT * FROM venda;')
    vendas = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return vendas

@app.route('/lista_vendas', methods=["GET"])
def lista_vendas():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM venda;')
    vendas = cur.fetchall()

    cur.close()
    connection.close()
    #print(vendas)
    #render_template('lista_vendas.html', vendas=vendas)

    return jsonify(vendas)

@app.route('/edita_venda_por_id/<int:id>', methods=["POST"])
def edita_venda_por_id(id):
    venda_alterado_dict = json.loads(json.dumps(request.get_json()))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM venda;')
    vendas = cur.fetchall()

    for venda in vendas:
        if venda[0] == id:  #venda[0] pega o id dos vendas
            cur.execute("UPDATE venda SET id_venda="+str(venda_alterado_dict['id_venda'])
                        +",customizacao_venda='"+venda_alterado_dict['customizacao_venda']
                        +"',id_estrangeiro_cliente='"+venda_alterado_dict['id_estrangeiro_cliente']
                        +"',id_estrangeiro_produto='"+venda_alterado_dict['id_estrangeiro_produto']
                        +"',nome_estrangeiro_cliente='"+venda_alterado_dict['nome_estrangeiro_cliente']
                        +"',nome_estrangeiro_produto='"+venda_alterado_dict['nome_estrangeiro_produto']
                        +"',observacao_venda='"+venda_alterado_dict['observacao_venda']
                        +"',quant_item_venda='"+venda_alterado_dict['quant_item_venda']
                        +"' WHERE id_venda = "+str(id)+";")
    
    cur.execute('SELECT * FROM venda;')
    vendas = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return vendas

@app.route('/deleta_venda_por_id', methods=["POST"])
def deleta_venda_por_id():
    id_deleta_venda = request.get_json()
    print(id_deleta_venda)
    print(type(id_deleta_venda))

    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM venda;')
    vendas = cur.fetchall()

    for venda in vendas:
        if venda[0] == id_deleta_venda:
            cur.execute("DELETE FROM venda WHERE id_venda = "+str(id_deleta_venda)+";")

    cur.execute('SELECT * FROM venda;')
    vendas = cur.fetchall()

    connection.commit()
    cur.close()
    connection.close()

    return vendas



# def get_db_connection():
#     conn = psycopg2.connect(host='localhost',
#                             database='flask_db',
#                             user=os.environ['DB_USERNAME'],
#                             password=os.environ['DB_PASSWORD'])
#     return conn


# @app.route('/')
# def index():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM books;')
#     books = cur.fetchall()
#     cur.close()
#     conn.close()
#     return render_template('index.html', books=books)


# @app.route('/create/', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         author = request.form['author']
#         pages_num = int(request.form['pages_num'])
#         review = request.form['review']

#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute('INSERT INTO books (title, author, pages_num, review)'
#                     'VALUES (%s, %s, %s, %s)',
#                     (title, author, pages_num, review))
#         conn.commit()
#         cur.close()
#         conn.close()
#         return redirect(url_for('index'))
    
#     return render_template('create.html')


if __name__ == '__name__':
    app.run(host="0.0.0.0", port=5000, debug=True)
