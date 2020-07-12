
import pandas as pd 
import numpy as np

master = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\grand_master_sheet.csv'
mapping = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Player_Mapping.csv'

bat_stat1 = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\Bat_in_code.csv'
bowl_stat1 = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\Bowl_in_code.csv'

BATTING_COLS = ["Player","Owner","Innings", "Not Outs","Orange Cap","Balls Faced","Highest","50","100", "6s" , "4s"]
BOWLING_COLS = ["Player","Owner","Innings","Balls","Dots","Runs conceeded","Purple Cap","Best Figures","4fer","5fer"]

data =  pd.read_csv(master,usecols=['player' , 'Present_league'])
data1 = pd.read_csv(mapping)
data = data[data['Present_league'] >= 1]
data2 = pd.merge(data,data1,how = 'left',left_on = 'Present_league',right_on = 'Player_id')
print(data2)
imp = ['player' , 'Name']
data2 =  data2[imp]
bat_stat = pd.DataFrame(columns = BATTING_COLS)
bowl_stat = pd.DataFrame(columns = BOWLING_COLS)
print(bat_stat)
print(bowl_stat)

bat_stat['Player'] = data2['player']
bat_stat['Owner'] = data2['Name']



bowl_stat['Player'] = data2['player']
bowl_stat['Owner'] = data2['Name']

bat_stat = bat_stat.fillna(0)
bowl_stat = bowl_stat.fillna(0)

bowl_stat['Best Figures'] = '0 for 0'

bat_stat.to_csv(bat_stat1)
bowl_stat.to_csv(bowl_stat1)


