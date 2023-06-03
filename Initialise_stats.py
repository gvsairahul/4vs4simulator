
import pandas as pd
import numpy as np

master = 'C:\\Users\\vzg00\\OneDrive\\Desktop\\simulator\\4vs4simulator\\Teams\\Master_data_sheet.csv'
mapping = 'C:\\Users\\vzg00\\OneDrive\\Desktop\\simulator\\4vs4simulator\\Teams\\Player_Mapping.csv'

bat_stat1 = 'C:\\Users\\vzg00\\OneDrive\\Desktop\\simulator\\4vs4simulator\\Stats\\Bat_in_code.csv'
bowl_stat1 = 'C:\\Users\\vzg00\\OneDrive\\Desktop\\simulator\\4vs4simulator\\Stats\\Bowl_in_code.csv'

BATTING_COLS = ["Player","Owner","Innings", "Not Outs","Orange Cap","Balls Faced","Highest","50","100", "6s" , "4s"]
BOWLING_COLS = ["Player","Owner","Innings","Balls","Dots","Runs conceeded","Purple Cap","Best Figures","4fer","5fer"]

data =  pd.read_csv(master,usecols=['PLAYERS' , 'Player_id','Bowling Style'])
data1 = pd.read_csv(mapping)
data = data[data['Player_id'] > 1]
data2 = pd.merge(data,data1,how = 'left',left_on = 'Player_id',right_on = 'Player_id')
print(data2)
imp = ['PLAYERS' , 'Name' , 'Bowling Style']
data2 =  data2[imp]
bat_stat = pd.DataFrame(columns = BATTING_COLS)
bowl_stat = pd.DataFrame(columns = BOWLING_COLS)
print(bat_stat)
print(bowl_stat)

bat_stat['Player'] = data2['PLAYERS']
bat_stat['Owner'] = data2['Name']


data2 = data2[(data2['Bowling Style'] == 'Pace') | (data2['Bowling Style'] == 'Spin')]

bowl_stat['Player'] = data2['PLAYERS']
bowl_stat['Owner'] = data2['Name']

bat_stat = bat_stat.fillna(0)
bowl_stat = bowl_stat.fillna(0)

bowl_stat['Best Figures'] = '0 for 0'

bat_stat.to_csv(bat_stat1)
bowl_stat.to_csv(bowl_stat1)
