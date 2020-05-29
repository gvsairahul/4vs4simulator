import csv, os, time
import pandas as pd
import numpy as np
from out_sim1 import out_calculator,boundary_calculator, runs_calculator, change_batsman, toss, best_bowling,notout_cal,fifty_cal
import xlsxwriter
from helper import initialise,write_to_stats,Bowler_Select,print_scorecard,Batsman_Select
from bowl_a_ball import ball_result,update_result,print_summary
from match import Innings_run,Super_over

#Batting Team
col_list = ["PLAYERS","Batsman_avg","Batsman_strikerate","Bowler_economy","Bowler_average","4s ratio","6s ratio","Balls per innings"]
BATTING_COLS = ["Player","Owner","Innings", "Not Outs","Orange Cap","Balls Faced","Highest","50","100", "6s" , "4s"]
BOWLING_COLS = ["Player","Owner","Innings","Balls","Dots","Runs conceeded","Purple Cap","Best Figures","4fer","5fer"]

user_name = input("If Rahul press 1, If Kb press 2,If Ganesh press 3,If Kaushik press 4:,If Dinesh press5:")



if user_name == '2':
    path = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Master_data_sheet.csv'
    path1 = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Player_Mapping.csv'
    Player1 = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player1.csv'
    Player2 = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player2.csv'
    Report_file = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Ball2Ball_1st_innings.txt'
    Report_file2 = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Ball2Ball_2nd_innings.txt'
    Batting_stats = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\Bat_in_code.csv'
    Bowling_stats = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\Bowl_in_code.csv'

elif user_name == '1':
    path = 'C:\\Users\\rahul\\Desktop\\4vs4simulator\\Teams\\Master_data_sheet.csv'
    path1 = 'C:\\Users\\rahul\\Desktop\\4vs4simulator\\Teams\\Player_Mapping.csv'
    Player1 = 'C:\\Users\\rahul\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player1.csv'
    Player2 = 'C:\\Users\\rahul\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player2.csv'
    Report_file = 'C:\\Users\\rahul\\Desktop\\4vs4simulator\\Teams\\Ball2Ball_1st_innings.txt'
    Report_file2 = 'C:\\Users\\rahul\\Desktop\\4vs4simulator\\Teams\\Ball2Ball_2nd_innings.txt'
    Batting_stats = 'C:\\Users\\rahul\\Desktop\\4vs4simulator\\Stats\\Bat_in_code.csv'
    Bowling_stats = 'C:\\Users\\rahul\\Desktop\\4vs4simulator\\Stats\\Bowl_in_code.csv'

elif user_name == '3' :
    path = 'C:\\Users\\Ganesh\\Desktop\\4vs4simulator\\Teams\\Master_data_sheet.csv'
    path1 = 'C:\\Users\\Ganesh\\Desktop\\4vs4simulator\\Teams\\Player_Mapping.csv'
    Player1 = 'C:\\Users\\Ganesh\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player1.csv'
    Player2 = 'C:\\Users\\Ganesh\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player2.csv'
    Report_file = 'C:\\Users\\Ganesh\\Desktop\\4vs4simulator\\Teams\\Ball2Ball_1st_innings.txt'
    Report_file2 = 'C:\\Users\\Ganesh\\Desktop\\4vs4simulator\\Teams\\Ball2Ball_2nd_innings.txt'
    Batting_stats = 'C:\\Users\\Ganesh\\Desktop\\4vs4simulator\\Stats\\Bat_in_code.csv'
    Bowling_stats = 'C:\\Users\\Ganesh\\Desktop\\4vs4simulator\\Stats\\Bowl_in_code.csv'


elif user_name == '4':
    path = 'C:\\Users\\biddu\\Desktop\\4vs4simulator\\Teams\\Master_data_sheet.csv'
    path1 = 'C:\\Users\\biddu\\Desktop\\4vs4simulator\\Teams\\Player_Mapping.csv'
    Player1 = 'C:\\Users\\biddu\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player1.csv'
    Player2 = 'C:\\Users\\biddu\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player2.csv'
    Report_file = 'C:\\Users\\biddu\\Desktop\\4vs4simulator\\Teams\\Ball2Ball_1st_innings.txt'
    Report_file2 = 'C:\\Users\\biddu\\Desktop\\4vs4simulator\\Teams\\Ball2Ball_2nd_innings.txt'
    Batting_stats = 'C:\\Users\\biddu\\Desktop\\4vs4simulator\\Stats\\Bat_in_code.csv'
    Bowling_stats = 'C:\\Users\\biddu\\Desktop\\4vs4simulator\\Stats\\Bowl_in_code.csv'
elif user_name == '5':
    path = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Teams/Master_data_sheet.csv'
    path1 = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Teams/Player_Mapping.csv'
    Player1 = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Teams/Data_for_simulation - Player1.csv'
    Player2 = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Teams/Data_for_simulation - Player2.csv'
    Report_file = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Teams/Ball2Ball_1st_innings.txt'
    Report_file2 = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Teams/Ball2Ball_2nd_innings.txt'
    Batting_stats = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Stats/Bat_in_code.csv'
    Bowling_stats = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Stats/Bowl_in_code.csv'

   


rrr=pd.read_csv(path,dtype = str)
# rrr1=rrr

bat_stat = pd.read_csv(Batting_stats)
bowl_stat = pd.read_csv(Bowling_stats)

bat_stat = bat_stat[BATTING_COLS]
bowl_stat = bowl_stat[BOWLING_COLS]

#rrr = rrr.rename(columns={'S.NO': 'Batting_Order'})

id_1 = input("Player1 id:")

id_2 = input("Player2 id:")


bb = pd.read_csv(path1,dtype=str)
p1 = bb[bb['Player_id']==id_1]['Name']
p2 = bb[bb['Player_id']==id_2]['Name']
for row in p2:
    Player2_Name = row

for row in p1:
    Player1_Name = row



print('Player 1: ' + Player1_Name)
print('Player 2: ' + Player2_Name)


result1 = rrr[rrr['Draft2_Player_id'] == id_1]
result2 = rrr[rrr['Draft2_Player_id'] == id_2]


bowl_stat_rem = bowl_stat[(bowl_stat['Owner'] != Player2_Name) & (bowl_stat['Owner'] != Player1_Name)]

bat_stat_rem = bat_stat[(bat_stat['Owner'] != Player2_Name) & (bat_stat['Owner'] != Player1_Name)]


result1 = result1[col_list]
result2 = result2[col_list]


result1.to_csv(Player1)

result2.to_csv(Player2)



toss_result=toss(Player1_Name,Player2_Name)
choosing=input(toss_result + '!! You won the toss, Will u Bat or Bowl:')

if (choosing == 'Bat' and toss_result == Player1_Name) or (choosing == 'Bowl' and toss_result == Player2_Name):
    csvData=csv.reader(open(Player1))
    csvData1=csv.reader(open(Player1))
    csvData3=csv.reader(open(Player2))
    csvData2=csv.reader(open(Player2)) 
    bts1 = bat_stat[bat_stat['Owner'] == Player1_Name]
    bts2 = bat_stat[bat_stat['Owner'] == Player2_Name]
    bos1 = bowl_stat[bowl_stat['Owner'] == Player1_Name]
    bos2 = bowl_stat[bowl_stat['Owner'] == Player2_Name]

elif (choosing == 'Bat' and toss_result == Player2_Name) or (choosing == 'Bowl' and toss_result == Player1_Name):
    csvData=csv.reader(open(Player2))
    csvData2=csv.reader(open(Player1)) 
    csvData3=csv.reader(open(Player1))
    csvData1=csv.reader(open(Player2))
    bts1 = bat_stat[bat_stat['Owner'] == Player2_Name]
    bts2 = bat_stat[bat_stat['Owner'] == Player1_Name]
    bos1 = bowl_stat[bowl_stat['Owner'] == Player2_Name]
    bos2 = bowl_stat[bowl_stat['Owner'] == Player1_Name]

    x = Player1_Name
    Player1_Name = Player2_Name
    Player2_Name = x
    

 
kb = ""

A = initialise(csvData,csvData2)
B = initialise(csvData3,csvData1)


attributes = A[0]
attributes2 = B[0]

# print(attributes)
# print(attributes2)

attributes11 = A[0]
attributes22 = B[0]

Chase = Innings_run(attributes,1800,1,121)

target = Chase[1] + 1

print("\nTarget is " + str(target) + "\n")

Chase2 = Innings_run(attributes2,target,1,121)

score_final = Chase2[1]

if score_final < target-1:
    print(Player1_Name + " Won by " + str(target-score_final -1) + " runs\n" )
elif score_final >= target:
    print(Player2_Name + " Won by " + str(10-Chase2[2]) + " Wickets\n")
else : 
    print("Its a Tie!!!\n")
    result = Super_over(attributes11,attributes22)
    if result == 2 :
        print("\n" + Player1_Name + " Won the Super Over\n")
    elif result == 1:
        print("\n" + Player2_Name + " Won the Super Over\n")



# f_1 = open(Report_file,'w')
# n = f_1.write(kb)
# f_1.close()

# chasing = chase(team_score+1,attributes2,Report_file2,attributes11,attributes22)

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
