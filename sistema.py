from Pacotes.pgsql import *
from Pacotes.Usuário import *
import psycopg2 as pg
from Pacotes.Funções import *

login = usuarios()
login.usuario()

while True:

    banco = input('Digite o nome do banco de dados que deseja conectar-> ')
    usuario = input('Digite seu usuário de acesso ao banco de dados-> ')
    senha = input('Digite sua senha de acesso ao banco de dados-> ')
    
    bd = BancoDeDados(banco, usuario, senha)

    op = bd.verificabanco()
    if op == 1:
        continue
    elif op ==2:
        bd.criarbanco()
        break
    else:
        break

print('Conectado com sucesso')
input()

op = menu()

if op == 1:
    while True:
        query = input('\nDigite a instrução SQL-> ')
        schemas = input('\nDigite a qual schemas a tabela pertence-> ')
        try:
            bd.criartabela(query, schemas)
        except:
            print('\nErro, verifique a instrução SQL ou o schemas!')
        else:
            print('\nTabela criada com sucesso!')
            break


query = '''
funcionarios(id serial NOT NULL PRIMARY KEY,nome TEXT NOT NULL,sobrenome TEXT NOT NULL,idade INTEGER NOT NULL)'''

input()



'''conexao = bd.conect
cursor = bd.cursor

cursor.execute('select "ID_VENDENDOR", "VALOR_VENDA" from mkt."TB_VENDAS"')
dados = cursor.fetchall()
for linha in dados:
    print(linha)

cursor.close()
conexao.close()'''
