import pyodbc
import pandas as pd
import numpy as np

df=pd.read_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\req_rate_score_second.csv')
df['dot_prob'] = df['dot'].astype(float)/df['total'].astype(float)
df['sing_prob'] = df['sing'].astype(float)/df['total'].astype(float)
df['doub_prob'] = df['doub'].astype(float)/df['total'].astype(float)
df['trip_prob'] = df['triple'].astype(float)/df['total'].astype(float)
df['four_prob'] = df['four'].astype(float)/df['total'].astype(float)
df['six_prob'] = df['six'].astype(float)/df['total'].astype(float)
df['wkt_prob'] = df['wicket'].astype(float)/df['total'].astype(float)
# 

df.to_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\req_rate_score_second.csv',index = False)
# sql_query2.to_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\bowling_stats.csv')

