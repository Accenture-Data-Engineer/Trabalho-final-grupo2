import os
from dotenv import load_dotenv
import pandas as pd
import sqlalchemy
import glob

# Carregando variáveis de ambiente
load_dotenv()

#Variáveis para conexão
server = os.environ['SERVER']
database = os.environ['DATABASE']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
driver = 'ODBC Driver 18 for SQL Server'
cnx_str = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'

engine = sqlalchemy.create_engine(cnx_str)

# Informando caminho de origem dos dados
path_clients = './data/clients/clients_clean'
path_transaction = './data/transaction/transaction_clean'
clients = glob.glob(path_clients + '/*.csv')
transaction = glob.glob(path_transaction + '/*.csv')

df_clients = pd.read_csv(clients[0])
df_transaction = pd.read_csv(transaction[0])

# Transformações necessárias para entendimento dos dados no banco de dados
df_clients['Data_cadastro'] = pd.to_datetime(df_clients['Data_cadastro'], format='%Y-%m-%d %H:%M:%S')
df_clients['Data_cadastro'] = df_clients['Data_cadastro'].dt.tz_localize(None)

df_transaction['DataHora'] = pd.to_datetime(df_transaction['DataHora'], format='%Y-%m-%d %H:%M:%S')
df_transaction['DataHora'] = df_transaction['DataHora'].dt.tz_localize(None)

# Coluna de Id fora da normalização (Ids repetidos)
df_transaction = df_transaction.drop('Id', axis=1)

print(df_clients.info())
print(df_transaction.info())

#Enviando para o banco de dados via SQL Alchemy
df_clients.to_sql('Cliente', engine, if_exists='append', index=False)
df_transaction.to_sql('Transacao', engine, if_exists='append', index=False)