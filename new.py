import csv, os, time
import pandas as pd
import numpy as np
from out_sim1 import out_calculator,boundary_calculator, runs_calculator, change_batsman, toss, best_bowling,notout_cal,fifty_cal
from second_innings import chase
import xlsxwriter
from Super_over import superover
from helper import initialise,write_to_stats
from bowl_a_ball import ball_result,update_result,print_summary

#Batting Team
col_list = ["PLAYERS","Batsman_avg","Batsman_strikerate","Bowler_economy","Bowler_average","4s","6s","Ratio","4s ratio","6s ratio"]
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
    csvData2=csv.reader(open(Player2))
    bts1 = bat_stat[bat_stat['Owner'] == Player1_Name]
    bts2 = bat_stat[bat_stat['Owner'] == Player2_Name]
    bos1 = bowl_stat[bowl_stat['Owner'] == Player1_Name]
    bos2 = bowl_stat[bowl_stat['Owner'] == Player2_Name]

elif (choosing == 'Bat' and toss_result == Player2_Name) or (choosing == 'Bowl' and toss_result == Player1_Name):
    csvData=csv.reader(open(Player2))
    csvData2=csv.reader(open(Player1))
    bts1 = bat_stat[bat_stat['Owner'] == Player2_Name]
    bts2 = bat_stat[bat_stat['Owner'] == Player1_Name]
    bos1 = bowl_stat[bowl_stat['Owner'] == Player2_Name]
    bos2 = bowl_stat[bowl_stat['Owner'] == Player1_Name]
    
non_header=False
non_header2=False
#print(csvData2)
attributes={}
attributes['batsmen']=[]
attributes['bowlers']=[]

attributes11={}
attributes11['batsmen']=[]
attributes11['bowlers']=[]

fall_of_wickets = []
attributes2={}
attributes2['batsmen']=[]
attributes2['bowlers']=[]

attributes22={}
attributes22['batsmen']=[]
attributes22['bowlers']=[]

 
kb = ""

initialise(csvData,csvData2,attributes)
initialise(csvData,csvData2,attributes11)
initialise(csvData2,csvData,attributes2)
initialise(csvData2,csvData,attributes22)


current_batsmen=[]
current_bowler_id=0
team_score=0
team_wickets=0
for j in range(len(attributes['batsmen'])):
    if attributes['batsmen'][j]['balls_faced']==0 and (j not in current_batsmen):
        print(str(j)+'  '+attributes['batsmen'][j]['name'])

answer = '0' 

while answer != '1':
    
    choser=int(input("Choose the batsman on non strike:"))
    next_batsman_id=choser
    current_batsmen.append(next_batsman_id)
    current_batsmen_id=next_batsman_id
    answer = input("If the batsman on strike is " + attributes['batsmen'][current_batsmen_id]['name'] + " Press 1:  ")    
    if answer != '1':
        current_batsmen.remove(current_batsmen_id)


for j in range(len(attributes['batsmen'])):
    if attributes['batsmen'][j]['balls_faced']==0 and (j not in current_batsmen):
        print(str(j)+'  '+attributes['batsmen'][j]['name'])
answer = '0' 

while answer != '1':
    choser=int(input("Choose the batsman on  strike:"))
    next_batsman_id=choser
    current_batsmen.append(next_batsman_id)
    current_batsmen_id=next_batsman_id
    answer = input("If the batsman on non strike is " + attributes['batsmen'][current_batsmen_id]['name'] + " Press 1:  ")    
    if answer != '1':
        current_batsmen.remove(current_batsmen_id)

for i in range(len(attributes['bowlers'])):
    print(str(i)+' '+attributes['bowlers'][i]['name'])
answer = '0' 
while answer != '1':              
    choser=int(input("Choose the id of bowler from above:"))
    current_bowler_id=choser
    answer = input("If the bowler chosen is " + attributes['bowlers'][current_bowler_id]['name'] + " Press 1:  ")    
        
print('\n')

target = 0

for i in range(1,121):
    
    result = ball_result(i,attributes['batsmen'][current_batsmen_id],attributes['bowlers'][current_bowler_id])

    update_result(result,i,team_runs,team_wickets,attributes['batsmen'][current_batsmen_id],attributes['bowlers'][current_bowler_id])

    if str(result) == '1' or str(result) == '3':
        current_batsmen_id=change_batsman(current_batsmen,current_batsmen_id)
    
    elif str(result) == 'out':
        if team_wickets==10:
            print("Team is all out at "+str(team_score))
            kb = kb + "Team is all out at "+str(team_score) + '\n'
            break
        else:
            for j in range(len(attributes['batsmen'])):
                if attributes['batsmen'][j]['balls_faced']==0 and (j not in current_batsmen):
                    print(str(j)+'  '+attributes['batsmen'][j]['name'])
            answer = '0' 
            while answer != '1':
                current_batsmen.remove(current_batsmen_id)
                choser=int(input("Choose the next batsman :"))
                next_batsman_id=choser
                current_batsmen.append(next_batsman_id)
                current_batsmen_id=next_batsman_id
                answer = input("If the batsman is " + attributes['batsmen'][current_batsmen_id]['name'] + " Press 1: ")    

            attributes['batsmen'][next_batsman_id]['batting_order']=team_wickets+2
    
    if i%6==0 and i!=120:
        time.sleep(4)
        #os.system('cls')
        overs=int(i/6)
        print_summary(team_runs,team_wickets,target,i)
        for j in (current_batsmen):
            if j!=current_batsmen_id:
                print(attributes['batsmen'][j]['name']+"* runs:"
                + str(attributes['batsmen'][j]['runs_scored'])+ " balls:"
                + str(attributes['batsmen'][j]['balls_faced'])+ " fours:"
                + str(attributes['batsmen'][j]['fours'])+ " sixes:"
                + str(attributes['batsmen'][j]['sixes']))
            else:
                print(attributes['batsmen'][j]['name']+" runs:"
                + str(attributes['batsmen'][j]['runs_scored'])+ " balls:"
                + str(attributes['batsmen'][j]['balls_faced'])+ " fours:"
                + str(attributes['batsmen'][j]['fours'])+ " sixes:"
                + str(attributes['batsmen'][j]['sixes']))
        print('\n')
        current_batsmen_id=change_batsman(current_batsmen,current_batsmen_id)
        for j in range(len(attributes['bowlers'])):
            if attributes['bowlers'][j]['balls_bowled']<=18 and j!=current_bowler_id:
                overs=str(int(attributes['bowlers'][j]['balls_bowled']/6))
                spare_balls=str(int(attributes['bowlers'][j]['balls_bowled']%6))
                overs=overs+'.'+spare_balls
                print(str(j)+' '+attributes['bowlers'][j]['name']+" "+overs+'-'+str(attributes['bowlers'][j]['dots'])
                    +'-'+str(attributes['bowlers'][j]['runs_conceded'])+'-'+str(attributes['bowlers'][j]['wickets_taken']))
        
        answer = '0' 
        while answer != '1':
            choser=int(input("Choose the id of bowler from above:"))
            current_bowler_id=choser
            answer = input("If the bowler chosen is " + attributes['bowlers'][current_bowler_id]['name'] + " Press 1: ")    
        
        
        
        



for i in range(len(attributes['batsmen'])):
    if attributes['batsmen'][i]['balls_faced']>0:
        attributes['batsmen'][i].pop('average', None)
        attributes['batsmen'][i].pop('ratio', None)
        attributes['batsmen'][i].pop('strikerate', None)
        if str(attributes['batsmen'][i]['out_to'])!='Not Out':
            print(attributes['batsmen'][i]['name']+' '+str(attributes['batsmen'][i]['runs_scored'])
                +"("+str(attributes['batsmen'][i]['balls_faced'])+") "+" Out To:"
                +str(attributes['batsmen'][i]['out_to'])+" 4s:"
                +str(attributes['batsmen'][i]['fours'])+" 6s:"
                +str(attributes['batsmen'][i]['sixes']))
        else:
            print(attributes['batsmen'][i]['name']+' '+str(attributes['batsmen'][i]['runs_scored'])
                +"("+str(attributes['batsmen'][i]['balls_faced'])+") "
                +str(attributes['batsmen'][i]['out_to'])+" 4s:"
                +str(attributes['batsmen'][i]['fours'])+" 6s:"
                +str(attributes['batsmen'][i]['sixes']))
print('\nFall Of Wickets\n')
for i in range(len(fall_of_wickets)):
    print(str(fall_of_wickets[i])+'- '+str(i+1))
print('\nBowling Scorecard\n')
for i in range(len(attributes['bowlers'])):
    if attributes['bowlers'][i]['balls_bowled']>0:
        attributes['bowlers'][i].pop('economy',None)
        attributes['bowlers'][i].pop('average',None)
        overs=str(int(attributes['bowlers'][i]['balls_bowled']/6))
        spare_balls=str(int(attributes['bowlers'][i]['balls_bowled']%6))
        overs=overs+'.'+spare_balls
        print(attributes['bowlers'][i]['name']+" "+overs+'-'+str(attributes['bowlers'][i]['dots'])
            +'-'+str(attributes['bowlers'][i]['runs_conceded'])+'-'+str(attributes['bowlers'][i]['wickets_taken']))
    
    




f_1 = open(Report_file,'w')
n = f_1.write(kb)
f_1.close()

chasing = chase(team_score+1,attributes2,Report_file2,attributes11,attributes22)

bat_use_cols = ["name","out_to","runs_scored","balls_faced","fours","sixes"]
bowl_use_cols = ["name","balls_bowled","dots","runs_conceded","wickets_taken"]

bts11 = pd.DataFrame(attributes['batsmen'],columns = bat_use_cols)
bos22 = pd.DataFrame(attributes['bowlers'],columns = bowl_use_cols)



BAT1 = pd.merge(bts1,bts11,how = 'left',left_on = 'Player',right_on = 'name' )
BOWL2 = pd.merge(bos2,bos22,how = 'left' , left_on = 'Player',right_on = 'name')

bts22 = pd.DataFrame(chasing[0]['batsmen'],columns = bat_use_cols)
bos11 = pd.DataFrame(chasing[0]['bowlers'],columns = bowl_use_cols)


BAT2 = pd.merge(bts2,bts22,how = 'left',left_on = 'Player',right_on = 'name' )
BOWL1 = pd.merge(bos1,bos11,how = 'left' , left_on = 'Player',right_on = 'name')


BAT = pd.concat([BAT1,BAT2],axis=0)
BOWL = pd.concat([BOWL1,BOWL2],axis=0)

write_to_stats(BAT,BOWL,BATTING_COLS,BOWLING_COLS,bat_stat_rem,bowl_stat_rem,Batting_stats,Bowling_stats)

f = open(Player1, "w+")
f.close()
f=open(Player2,"w+")
f.close()

#workbook.close()