import csv, os, time
import pandas as pd
import numpy as np
from out_sim1 import out_calculator,boundary_calculator, runs_calculator, change_batsman, best_bowling,notout_cal,fifty_cal
import xlsxwriter
from helper import initialise,write_to_stats,Bowler_Select,print_scorecard,Batsman_Select,situation_cal
from bowl_a_ball import ball_result,update_result,print_summary
from match import Innings_run,Innings_run_chase,Super_over
from Pre_Match import pre_match,toss

#Batting Team
Prematch_stuff = pre_match()
BATTING_COLS = ["Player","Owner","Innings", "Not Outs","Orange Cap","Balls Faced","Highest","50","100", "6s" , "4s"]
BOWLING_COLS = ["Player","Owner","Innings","Balls","Dots","Runs conceeded","Purple Cap","Best Figures","4fer","5fer"]

Master_list = Prematch_stuff
bat_stat_rem ,bowl_stat_rem ,Player1_Name ,Player2_Name,bat_stat,bowl_stat,Player1,Player2,Batting_stats,Bowling_stats,first,second,first_rate,first_wkt,second_rate,second_wkt = [Master_list[i] for i in range(0,16)]

toss_result=toss(Player1_Name,Player2_Name)
choosing=input(toss_result + '!! You won the toss, Will u Bat or Bowl:')

if (choosing == 'Bat' and toss_result == Player1_Name) or (choosing == 'Bowl' and toss_result == Player2_Name):
    A = initialise(Player1,Player2)
    B = initialise(Player2,Player1)
    C = initialise(Player1,Player2)
    D = initialise(Player2,Player1)
    bts1 = bat_stat[bat_stat['Owner'] == Player1_Name]
    bts2 = bat_stat[bat_stat['Owner'] == Player2_Name]
    bos1 = bowl_stat[bowl_stat['Owner'] == Player1_Name]
    bos2 = bowl_stat[bowl_stat['Owner'] == Player2_Name]

elif (choosing == 'Bat' and toss_result == Player2_Name) or (choosing == 'Bowl' and toss_result == Player1_Name):
    
    B = initialise(Player1,Player2)
    A = initialise(Player2,Player1)
    D = initialise(Player1,Player2)
    C = initialise(Player2,Player1)
    bts1 = bat_stat[bat_stat['Owner'] == Player2_Name]
    bts2 = bat_stat[bat_stat['Owner'] == Player1_Name]
    bos1 = bowl_stat[bowl_stat['Owner'] == Player2_Name]
    bos2 = bowl_stat[bowl_stat['Owner'] == Player1_Name]

    x = Player1_Name
    Player1_Name = Player2_Name
    Player2_Name = x
    

attributes = A[0]
attributes2 = B[0]
attributes11 = C[0]
attributes22 = D[0]

F1 = situation_cal(first,second,first_rate,first_wkt,second_rate,second_wkt)

First = F1[0]['first']
Second = F1[0]['second']
First_rate = F1[0]['first_rate']
First_wkt = F1[0]['first_wkt']
Second_rate = F1[0]['second_rate']
Second_wkt = F1[0]['second_wkt']


Chase = Innings_run(attributes,First,First_rate,First_wkt,1800,1,121,10)

target = Chase[1] + 1

print("\nTarget is " + str(target) + "\n")

Chase2 = Innings_run_chase(attributes2,Second,Second_rate,Second_wkt,target,1,121,10)

score_final = Chase2[1]

bat_use_cols = ["name","out_to","runs_scored","balls_faced","fours","sixes"]
bowl_use_cols = ["name","balls_bowled","dots","runs_conceded","wickets_taken"]

bts11 = pd.DataFrame(attributes['batsmen'],columns = bat_use_cols)
bos22 = pd.DataFrame(attributes['bowlers'],columns = bowl_use_cols)



BAT1 = pd.merge(bts1,bts11,how = 'left',left_on = 'Player',right_on = 'name' )
BOWL2 = pd.merge(bos2,bos22,how = 'left' , left_on = 'Player',right_on = 'name')

bts22 = pd.DataFrame(attributes2['batsmen'],columns = bat_use_cols)
bos11 = pd.DataFrame(attributes2['bowlers'],columns = bowl_use_cols)


BAT2 = pd.merge(bts2,bts22,how = 'left',left_on = 'Player',right_on = 'name' )
BOWL1 = pd.merge(bos1,bos11,how = 'left' , left_on = 'Player',right_on = 'name')


BAT = pd.concat([BAT1,BAT2],axis=0)
BOWL = pd.concat([BOWL1,BOWL2],axis=0)

write_to_stats(BAT,BOWL,BATTING_COLS,BOWLING_COLS,bat_stat_rem,bowl_stat_rem,Batting_stats,Bowling_stats)

if score_final < target-1:
    print(Player1_Name + " Won by " + str(target-score_final -1) + " runs\n" )
elif score_final >= target:
    print(Player2_Name + " Won by " + str(10-Chase2[2]) + " Wickets\n")
else : 
    print("Its a Tie!!!\n")
    result = Super_over(attributes11,attributes22,first,second)
    if result == 1 :
        print("\n" + Player1_Name + " Won the Super Over\n")
    elif result == 2:
        print("\n" + Player2_Name + " Won the Super Over\n")
