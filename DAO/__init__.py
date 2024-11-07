import psycopg2


# Estabelecendo a conexão com o Banco de dados
def conectardb():
    conexao = psycopg2.connect(database="minicursobd",
                               host="localhost",
                               user="postgres",
                               password="1234",
                               port="5432")
    return conexao


# Chame a função para testar a conexão
conexao = conectardb()


def cadastrar_usuario(nome, email, senha):
    conexao = conectardb()  # Estabelece conexão com o banco de dados.
    cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL.
    cursor.execute("INSERT INTO usuario (nome, email, senha) VALUES (%s, %s,  %s)", (nome, email, senha))

    # Executa o comando INSERT para adicionar um novo usuário.
    conexao.commit()  # Salva (confirma) a transação no banco de dados.
    cursor.close()  # Fecha o cursor.
    conexao.close()  # Fecha a conexão com o banco de dados.


def buscar_usuario(nome):
    conexao = conectardb()  # Conecta ao banco.
    cursor = conexao.cursor()  # Cria um cursor para consultas.
    cursor.execute(f"SELECT nome,email FROM usuario where nome= '{nome}' ")
    # Executa o comando SELECT para obter todos os usuários.
    resultado = cursor.fetchall()  # Recupera todos os resultados da consulta em uma lista.
    cursor.close()  # Fecha o cursor.
    conexao.close()  # Fecha a conexão com o banco.
    return resultado  # Retorna a lista de usuários.


def buscar_id(nome):
    conexao = conectardb()  # Conecta ao banco.
    cursor = conexao.cursor()  # Cria um cursor para consultas.
    cursor.execute(f"SELECT id FROM usuario where nome= '{nome}' ")
    # Executa o comando SELECT para obter todos os usuários.
    resultado = cursor.fetchall()
    resultado = resultado[0][0]  # Recupera todos os resultados da consulta em uma lista.
    cursor.close()  # Fecha o cursor.
    conexao.close()  # Fecha a conexão com o banco.
    return resultado  # Retorna a lista de usuários.


def listar_usuarios():
    conexao = conectardb()  # Conecta ao banco.
    cursor = conexao.cursor()  # Cria um cursor para consultas.
    cursor.execute(f"SELECT nome,email FROM usuario")
    # Executa o comando SELECT para obter todos os usuários.
    resultado = cursor.fetchall()  # Recupera todos os resultados da consulta em uma lista.
    cursor.close()  # Fecha o cursor.
    conexao.close()  # Fecha a conexão com o banco.
    return resultado  # Retorna a lista de usuários.


def update_usuario(id, novo_nome, novo_email):
    conexao = conectardb()  # Conecta ao banco.
    cursor = conexao.cursor()  # Cria um cursor para o comando de atualização.
    cursor.execute("UPDATE usuario SET nome = %s, email = %s WHERE id = %s", (novo_nome, novo_email, id))
    # Atualiza o nome e email do usuário com o id especificado.
    conexao.commit()  # Salva a transação.
    cursor.close()  # Fecha o cursor.
    conexao.close()  # Fecha a conexão com o banco.


def remover_usuario(id):
    conexao = conectardb()  # Conecta ao banco.
    cursor = conexao.cursor()  # Cria um cursor para o comando de exclusão.
    cursor.execute("DELETE FROM usuario WHERE id = %s", (id,))
    # Executa o comando DELETE para remover o usuário com o id dado.
    conexao.commit()  # Salva a transação.
    cursor.close()  # Fecha o cursor.
    conexao.close()  # Fecha a conexão.
