import os
from dotenv import load_dotenv
import pyodbc
import pandas as pd

load_dotenv()

server = os.environ['SERVER']
database = os.environ['DATABASE']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']

cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute('SELECT * FROM Clientes')
cursor.commit()

clean_clients = './data/clients/clients_clean/part-00000-dbc09eef-47f3-4e57-995d-6cc36d88e53f-c000.csv'
df_clean_clients = pd.read_csv(clean_clients)
print(df_clean_clients)

# Definir uma função para inserir uma pessoa na tabela do SQL Server
#def inserir_pessoa(pessoa):
    # cursor.execute("INSERT INTO Tabela de clientes (Id, Nome, Email, Data_cadastro, Telefone, DDD, Country_code) VALUES (?, ?)", pessoa.Nome, pessoa.Idade)
    # cursor.commit()

#for index, row in df_clean_clients.iterrows():
#    cursor.execute("INSERT INTO Clientes (Id, Nome, Email, Data_cadastro, Telefone, DDD, Country_code) values(?,?,?)", row.Id, row.Nome, row.Email, row.Data_cadastro, row.Telefone, row.DDD, row.Country_code)

 # Aplicar a função em cada linha do DataFrame usando foreach()
# df_clean_clients.foreach(lambda row: inserir_pessoa(row))