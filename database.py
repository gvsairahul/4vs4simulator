import pyodbc
import pandas as pd
import numpy as np

d1 = pd.read_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Master_data_sheet.csv')
d2 = pd.read_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\grand_master_sheet.csv')

col_list = ['PLAYERS','Minidraft3']
d1=d1[col_list]
d = pd.merge(d2,d1,how = 'left' , left_on = 'player',right_on = 'PLAYERS')

d['Present_league'] = np.where(d['Minidraft3']>0,d['Minidraft3'],d['Present_league'])

d=d.drop(columns=['PLAYERS','Minidraft3'],axis=1)

d.to_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\grand_master_sheet.csv',index=False)
