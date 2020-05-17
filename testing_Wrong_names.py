import csv, os, time
import pandas as pd
import numpy as np
from out_sim1 import out_calculator,boundary_calculator, runs_calculator, change_batsman, toss
from second_innings import chase
import xlsxwriter


Batting_stats = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\Tournament_Stats_Batting.csv'
Bowling_stats = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\Tournament_Stats_Bowling.csv'

path = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Master_data_sheet.csv'

testing_bat = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Wrong_Names_Bat.csv'

testing_bowl = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Wrong_Names_Bowl.csv'


rrr=pd.read_csv(path,dtype = str)
# rrr1=rrr

bat_stat = pd.read_csv(Batting_stats,dtype = str)
bowl_stat = pd.read_csv(Bowling_stats,dtype = str)

rrr.Draft2_Player_id.notnull()
BAT1 = pd.merge(rrr,bat_stat,how = 'right',left_on = 'PLAYERS',right_on = 'Player')

BOWL1 = pd.merge(rrr,bowl_stat,how = 'right',left_on = 'PLAYERS',right_on = 'Player')

use_colum = ["PLAYERS","Player"]
BAT1 = BAT1[use_colum]
BOWL1 = BOWL1[use_colum]

BAT1.to_csv(testing_bat)
BOWL1.to_csv(testing_bowl)

