import pyodbc
import pandas as pd
import numpy as np

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=KALYAN_BHARGAV;DATABASE=Cricket;Trusted_Connection=yes')
cursor = connection.cursor()
sql_query = pd.read_sql_query('Select * from dbo.batting ',connection)
sql_query2 = pd.read_sql_query('Select * from dbo.bowling ',connection)

sql_query.to_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\batting_stats.csv')
sql_query2.to_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\bowling_stats.csv')
