import pyodbc
import pandas as pd
import numpy as np

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=KALYAN_BHARGAV;DATABASE=Cricket;Trusted_Connection=yes')
cursor = connection.cursor()
sql_query = pd.read_sql_query('Select * from dbo.live_score where [over] = 18',connection)

print(sql_query)