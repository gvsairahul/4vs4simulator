import pyodbc
import pandas as pd
import numpy as np

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=KALYAN_BHARGAV;DATABASE=Cricket;Trusted_Connection=yes')
cursor = connection.cursor()
sql_query = pd.read_sql_query('Select distinct batsman as player from dbo.live_Score ',connection)
sql_query2 = pd.read_sql_query('Select distinct bowler as player from dbo.live_Score ',connection)

print(sql_query)