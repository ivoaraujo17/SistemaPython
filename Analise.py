import pandas as pd 

import psycopg2 as pg


conexao = pg.connect(database = 'Vendas', 

                    user = 'postgres',

                    password = 12345)

cursor = conexao.cursor()
cursor.execute('select * from mkt."TB_VENDAS"')