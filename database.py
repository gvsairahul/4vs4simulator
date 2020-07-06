import pyodbc
import pandas as pd
import numpy as np

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=KALYAN_BHARGAV;DATABASE=Cricket;Trusted_Connection=yes')
cursor = connection.cursor()
# df = pd.read_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\second_innings.csv')
df = pd.read_sql_query('Select * from dbo.first_innings11 ',connection)
df['dot_prob'] = df['dot'].astype(float)/df['total'].astype(float)
df['sing_prob'] = df['sing'].astype(float)/df['total'].astype(float)
df['doub_prob'] = df['doub'].astype(float)/df['total'].astype(float)
df['trip_prob'] = df['triple'].astype(float)/df['total'].astype(float)
df['four_prob'] = df['four'].astype(float)/df['total'].astype(float)
df['six_prob'] = df['six'].astype(float)/df['total'].astype(float)
df['wkt_prob'] = df['wicket'].astype(float)/df['total'].astype(float)
# 

df.to_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\first_innings.csv')
# sql_query2.to_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\bowling_stats.csv')
