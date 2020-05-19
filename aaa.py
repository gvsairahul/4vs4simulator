import csv, os, time
import pandas as pd
import numpy as np
from out_sim1 import out_calculator,boundary_calculator, runs_calculator, change_batsman, toss, best_bowling,notout_cal,fifty_cal
from second_innings import chase
import xlsxwriter

#Batting Team
col_list = ["PLAYERS","Batsman_avg","Batsman_strikerate","Bowler_economy","Bowler_average","4s","6s","Ratio","4s ratio","6s ratio"]
BATTING_COLS = ["Player","Owner","Innings", "Not Outs","Orange Cap","Balls Faced","Highest","50","100", "6s" , "4s"]
BOWLING_COLS = ["Player","Owner","Innings","Balls","Dots","Runs conceeded","Purple Cap","Best Figures","4fer","5fer"]


Batting_stats = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\Bat_in_code.csv'
Bowling_stats = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\Bowl_in_code.csv'


bat_stat = pd.read_csv(Batting_stats)
bowl_stat = pd.read_csv(Bowling_stats)

bat_stat = bat_stat[(bat_stat['Owner'] == 'Ganesh')  |(bat_stat['Owner'] == 'Chaitu') ]
bowl_stat = bowl_stat[(bowl_stat['Owner'] == 'Chaitu') ]

print(bat_stat)

print(bowl_stat)

for row in bowl_stat['Best Figures']:
    print(len(row))

