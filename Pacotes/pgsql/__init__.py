import psycopg2 as pg
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class BancoDeDados():#classe banco com seus atributos e metodos

    #Def construtor que define os atribustos quando é chamado a classe
    def __init__(self, bancodedados, usuario, senha): 
        self.banco = bancodedados
        self.usuario = usuario
        self.senha = senha
        try:
            self.conexao = pg.connect(host='', database = self.banco, 
                                 user = self.usuario, password = self.senha)
            self.cursor = self.conexao.cursor()
        except:
            print()
        else:
            print()

    def verificabanco(self):#Verifica se o banco existe
        while True:
            try:
                #Tenta fazer a conexao chamado o metodo conect
                self.conect()
            except:#Se der erro, entra em um lopp para obter uma opção valida do usuário    
                print('\nErro ao conectar com o banco de dados! '\
                    'Verifique se o nome, usuario e senha estão corretos')
                while True:
                    try:
                        criarbanco = int(input('\nSe deseja alterar as informações digite 1, '\
                            'se deseja criar um novo banco com essas informações '\
                            'digite 2. responda 1 ou 2 -> '))
                    except:
                        print('\nOpção invalida, tente novamente!')
                        continue
                    else:
                        break #Com a opção valida obtida
                
                #retorna 1 se o usuário quiser alterar as informações
                if criarbanco == 1:
                    return 1
                #retorna 2 se o usuário quiser criar um banco novo com as informações
                else:
                    return 2
            #retorna 3 se o banco existir e a conexão deu certo
            else:
                return 3
            break

    def conect(self):#Metodo que retorna a conexao com o banco de dados
        self.conect = pg.connect(host='', database = self.banco, 
                                 user = self.usuario, password = self.senha)
        return self.conect

    
    def criarbanco(self):#Cria o banco de dados
        #loop para sair apenas quando o banco for criado
        while True:
            try:
                print('\nCriando o banco de dados!')
                #conecta com o sgbd
                conexao = pg.connect(host='',user = self.usuario, 
                                        password = self.senha)
                conexao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                cursor = conexao.cursor()

                #tenta criar o banco de dados
                cursor.execute(f'CREATE DATABASE {self.banco}')
            except:
                #Se der erro, o usuário e senha do sgbd estão incorretos
                #Abaixo alteramos o atributo usurio e senha e retornamos o loop
                print('\nErro ao criar o banco de dados! Verifique seu usuário e senha do sgbd')
                self.usuario = input('\nDigite novamente seu usuário do sgbd-> ')
                self.senha = input('\nDigite novamente sua senha do sgbd-> ')
                continue
            else:
                #o banco foi criado, fornece a msg e para o loop
                print('\nO banco de dados foi criado com sucesso!')
                break
    
    def criartabela(self,query,schemas='public'):#Metodo para criar tabela
        
        #Divide a query em duas parte com "(", onde a primeira parte e o nome da tabela
        nometabela = query.split('(')

        #Excluir a tabela se ela existir, passando o schemas e o nometabela com strip para tirar
        #espacos em branco antes e depois do nome
        self.cursor.execute(f'DROP TABLE IF EXISTS {schemas}.{nometabela[0].strip()}')
        
        #criar a tabela passando o shemas(por padrao é o public), e a query
        self.cursor.execute(f'CREATE TABLE {schemas}.{query}')

        #commit na conexão para gravar a operação
        self.conexao.commit()

        print('tabela criada com sucesso')


    def inserirdados(self, tabela, tupla, schemas='public'):
        try:
            self.cursor.execute(f'INSERT INTO {tabela}(nome, sobrenome, idade) VALUES{tupla}')
            self.conexao.commit()#grava os dados no BD, se não os dados não são registrados
        except:
            print('Erro ao inserir os dados!')
        else:
            print('Dados cadastrado com sucesso!')
    
    
    def lertabela(self, tabela, schemas='public'): #Retorna uma lista com dados da tabela
        self.cursor.execute(f'SELECT * FROM {tabela}')
        return self.cursor.fetchall()#retorna uma lista de tuplas que representa as linhas da tb
        
