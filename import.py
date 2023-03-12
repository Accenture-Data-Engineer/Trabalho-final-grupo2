import pyodbc
import pandas as pd
 
# TrustServerCertificate=no;
driver = '{ODBC Driver 18 for SQL Server}'
server = 'tcp:anti-fraude.database.windows.net'
port = '1443'
database = 'Anti_fraude_s_a'
uid = 'Grupo_02'
pwd = 'Projeto@2023'

conn = pyodbc.connect('Driver='+driver+';Server='+server+';PORT='+port+';Database='+database+';Uid='+uid+';Pwd='+pwd+";Encrypt=yes;")
# cursor = cnxn.cursor()
df1 = pd.read_sql_query("SELECT * FROM cliente", conn)
df2 = pd.read_sql_query("SELECT * FROM transacao", conn)
df3 = pd.read_sql_query("SELECT * FROM fraudes", conn)

client_table = df1.to_csv('client_table.csv')
transaction_table = df2.to_csv('transaction_table.csv')
# Cobrar a bonita pq está NULL ainda
fraud_table = df3.to_csv('fraud_table.csv')

# Comando para executar e enviar para o powerbi - REVER COMANDO POWERBI
df1 = pd.read_csv(r'D:\Documentos\Trabalho-final-grupo2-main\migration\client_table.csv')
df2 = pd.read_csv(r'D:\Documentos\Trabalho-final-grupo2-main\migration\transaction_table.csv')
df3 = pd.read_csv(r'D:\Documentos\Trabalho-final-grupo2-main\migration\fraud_table.csv')
print(df1, df2, df3)