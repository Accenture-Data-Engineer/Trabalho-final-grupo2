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