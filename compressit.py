import pandas as pd 
import numpy as np

data = pd.read_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\Bowler_to_Batsman.csv')

data = data[data['Batsman'] != data['Bowler']]

data['Out'] = round(data['Out'],4)

dd = pd.read_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\Bat_in_code.csv')
Col_Test1 = ["Batsman","Bowler","Ball","0","1","2","3","4","6","Out","Owner"]


d1 = pd.merge(data,dd,how = 'inner',left_on='Batsman',right_on= 'Player')

d1 = d1[Col_Test1]
d1 = d1.rename(columns={'Owner':'Owner_Bat'})

Col_Test2 = ["Batsman","Bowler","Ball","0","1","2","3","4","6","Out","Owner_Bat","Owner"]

d2 = pd.merge(d1,dd,how = 'inner',left_on='Bowler',right_on='Player')

d2 = d2[Col_Test2]

d2 = d2.rename(columns={'Owner':'Owner_Bowl'})

d2 = d2[d2['Owner_Bat'] != d2['Owner_Bowl']]



d2.to_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\Bowler_to_Batsman.csv')

