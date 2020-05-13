import csv, os, time
import pandas as pd
import numpy as np
from out_sim1 import out_calculator,boundary_calculator, runs_calculator, change_batsman, toss
from second_innings import chase

#Batting Team
col_list = ["PLAYERS","Batsman_avg","Batsman_strikerate","Bowler_economy","Bowler_average","4s","6s","Ratio","4s ratio","6s ratio"]

user_name = input("If Rahul press 1, If Kb press 2:")

if user_name == '2':
    path = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Master_data_sheet.csv'
    path1 = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Player_Mapping.csv'
    Player1 = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player1.csv'
    Player2 = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player2.csv'

elif user_name == '1':
    path = 'C:\\Users\\rahul\\Desktop\\4vs4simulator\\Teams\\Master_data_sheet.csv'
    path1 = 'C:\\Users\\rahul\\Desktop\\4vs4simulator\\Teams\\Player_Mapping.csv'
    Player1 = 'C:\\Users\\rahul\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player1.csv'
    Player2 = 'C:\\Users\\rahul\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player2.csv'


    # handle header line, save it for writing to output file
    # header = next(Player).strip("\n").split(",")    


rrr=pd.read_csv(path,dtype = str)
# rrr1=rrr


#rrr = rrr.rename(columns={'S.NO': 'Batting_Order'})

id_1 = input("Player1 id:")
idd_1 = input("Player 1 - Auction or draft with number:")
id_2 = input("Player2 id:")
idd_2 = input("Player 2 - Auction or draft with number:")

bb = pd.read_csv(path1,dtype=str)
p1 = bb[bb['Player_id']==id_1]['Name']
p2 = bb[bb['Player_id']==id_2]['Name']
for row in p2:
    Player2_Name = row

for row in p1:
    Player1_Name = row

print('Player 1: ' + Player1_Name)
print('Player 2: ' + Player2_Name)

if idd_1 == 'D1' or idd_1 == 'd1' :
    result1 = rrr[rrr['Draft1_Player_id'] == id_1]
elif idd_1 == 'A1' or idd_1 == 'a1':
    result1 = rrr[rrr['Auction1_Player_id'] == id_1]
elif idd_1 == 'A2' or idd_1 == 'a2':
    result1 = rrr[rrr['Auction2_Player_id'] == id_1]
elif idd_1 == 'A3' or idd_1 == 'a3':
    result1 = rrr[rrr['Auction3_Player_id'] == id_1]

if idd_2 == 'D1' or idd_2 == 'd1' :
    result2 = rrr[rrr['Draft1_Player_id'] == id_2]
elif idd_2 == 'A1' or idd_2 == 'a1':
    result2 = rrr[rrr['Auction1_Player_id'] == id_2]
elif idd_2 == 'A2' or idd_2 == 'a2':
    result2 = rrr[rrr['Auction2_Player_id'] == id_2]
elif idd_2 == 'A3' or idd_2 == 'a3':
    result2 = rrr[rrr['Auction3_Player_id'] == id_2]
           


    


# print(result1)
# print(result2)

result1 = result1[col_list]
result2 = result2[col_list]

result1.to_csv(Player1)

result2.to_csv(Player2)


# result1 = result1(result1['Draft_Player_id'] == 5)
# result2 = result2(result2['Draft_Player_id'] == 3)

# print('result1 = ')
# print(result1)
# print('result2 = ')  
# print(result2)

# for row in result1:
#     print(row)












# reader1 = csv.reader(open(path))

# result2 = filter(lambda row: row[12] == '12', reader1)



#     # result1 = filter(lambda row: row[9] == '5', reader2)
#     # #
#     # result2 = filter(lambda row: row[12] == '12', reader1)

    


    
        
    
    



# extract the variables you wan

#master = csv.reader(open(path))

call=input("Heads or Tails:")
toss_result=toss()
if call==toss_result:
    choosing=input(Player1_Name + '!! You won the toss, Will u Bat or Bowl:')
    if choosing=='Bat':
        csvData=csv.reader(open(Player1))
        csvData2=csv.reader(open(Player2))
    else:
        csvData2=csv.reader(open(Player1))
        csvData=csv.reader(open(Player2))
else:
    choosing=input(Player2_Name + '!! You won the toss, Will u Bat or Bowl:')
    if choosing=='Bat':
        csvData2=csv.reader(open(Player1))
        csvData=csv.reader(open(Player2))
    else:
        csvData=csv.reader(open(Player1))
        csvData2=csv.reader(open(Player2))
    
non_header=False
non_header2=False


#print(csvData2)
attributes={}
attributes['batsmen']=[]
attributes['bowlers']=[]
batsman_number=0
bowler_number=0

attributes2={}
attributes2['batsmen']=[]
attributes2['bowlers']=[]
batsman_number2=0
bowler_number2=0

for row in csvData:
    if non_header:
        attributes['batsmen'].append({})
        attributes['batsmen'][batsman_number]['name']=row[1].strip(' ')
       # print(row[2]+'\n'+row[3]+'\n')
        attributes['batsmen'][batsman_number]['average']=float(row[2])
        attributes['batsmen'][batsman_number]['strikerate']=float(row[3])
        attributes['batsmen'][batsman_number]['runs_scored']=0
        attributes['batsmen'][batsman_number]['balls_faced']=0
        attributes['batsmen'][batsman_number]['fours']=0
        attributes['batsmen'][batsman_number]['sixes']=0
        attributes['batsmen'][batsman_number]['ratio']=float(row[8])
        attributes['batsmen'][batsman_number]['4s ratio']=float(row[9])
        attributes['batsmen'][batsman_number]['6s ratio']=float(row[10])
        attributes['batsmen'][batsman_number]['out_to']='Not Out'
        batsman_number+=1
        if float(row[4])>0 and float(row[5])>0:
            attributes2['bowlers'].append({})
            attributes2['bowlers'][bowler_number2]['name']=row[1].strip(' ')
            attributes2['bowlers'][bowler_number2]['economy']=float(row[4])
            attributes2['bowlers'][bowler_number2]['average']=float(row[5])
            attributes2['bowlers'][bowler_number2]['balls_bowled']=0
            attributes2['bowlers'][bowler_number2]['runs_conceded']=0
            attributes2['bowlers'][bowler_number2]['wickets_taken']=0
            attributes2['bowlers'][bowler_number2]['dots']=0
            bowler_number2+=1
    non_header = True

for row in csvData2:
    if non_header2:
        attributes2['batsmen'].append({})
        attributes2['batsmen'][batsman_number2]['name']=row[1].strip(' ')
        attributes2['batsmen'][batsman_number2]['average']=float(row[2])
        attributes2['batsmen'][batsman_number2]['strikerate']=float(row[3])
        attributes2['batsmen'][batsman_number2]['runs_scored']=0
        attributes2['batsmen'][batsman_number2]['balls_faced']=0
        attributes2['batsmen'][batsman_number2]['fours']=0
        attributes2['batsmen'][batsman_number2]['sixes']=0
        attributes2['batsmen'][batsman_number2]['ratio']=float(row[8])
        attributes2['batsmen'][batsman_number2]['out_to']='Not Out'
        batsman_number2+=1
        if float(row[4])>0 and float(row[5])>0:
            attributes['bowlers'].append({})
            attributes['bowlers'][bowler_number]['name']=row[1].strip(' ')
            attributes['bowlers'][bowler_number]['economy']=float(row[4])
            attributes['bowlers'][bowler_number]['average']=float(row[5])
            attributes['bowlers'][bowler_number]['balls_bowled']=0
            attributes['bowlers'][bowler_number]['runs_conceded']=0
            attributes['bowlers'][bowler_number]['wickets_taken']=0
            attributes['bowlers'][bowler_number]['dots']=0
            bowler_number+=1
    non_header2 = True
current_batsmen=[]
current_bowler_id=0
team_score=0
team_wickets=0
for j in range(len(attributes['batsmen'])):
    if attributes['batsmen'][j]['balls_faced']==0 and (j not in current_batsmen):
        print(str(j)+'  '+attributes['batsmen'][j]['name'])
choser=int(input("Choose the  batsman on strike:"))
current_batsmen.append(choser)
current_batsmen_id=choser
for j in range(len(attributes['batsmen'])):
    if attributes['batsmen'][j]['balls_faced']==0 and (j not in current_batsmen):
        print(str(j)+'  '+attributes['batsmen'][j]['name'])
choser=int(input("Choose the  batsman on non strike:"))
current_batsmen.append(choser)
for i in range(len(attributes['bowlers'])):
    print(str(i)+' '+attributes['bowlers'][i]['name'])
choser=int(input("Choose the id of bowler from above:"))
current_bowler_id=choser
print('\n')

for i in range(1,121):
    result=out_calculator(attributes['batsmen'][current_batsmen_id],attributes['bowlers'][current_bowler_id])
    attributes['batsmen'][current_batsmen_id]['balls_faced']+=1
    attributes['bowlers'][current_bowler_id]['balls_bowled']+=1
    if result=='notout':

        bound = boundary_calculator(i,attributes['batsmen'][current_batsmen_id],attributes['bowlers'][current_bowler_id])
        if bound == 'N':
            runs=runs_calculator(i,attributes['batsmen'][current_batsmen_id],attributes['bowlers'][current_bowler_id])
            
            print("Ball "+str(i)+' - '+attributes['bowlers'][current_bowler_id]['name']+" to "+attributes['batsmen'][current_batsmen_id]['name']+' : '+str(runs))
            team_score+=runs
            attributes['batsmen'][current_batsmen_id]['runs_scored']+=runs
            attributes['bowlers'][current_bowler_id]['runs_conceded']+=runs
            if runs==0:
                attributes['bowlers'][current_bowler_id]['dots']+=1
            if runs==1 or runs==3:
                current_batsmen_id=change_batsman(current_batsmen,current_batsmen_id)
        else :
            if bound == '4':
                print("Ball "+str(i)+' - '+attributes['bowlers'][current_bowler_id]['name']+" to "+attributes['batsmen'][current_batsmen_id]['name']+' : '+'4')
                team_score+=4
                attributes['batsmen'][current_batsmen_id]['runs_scored']+=4
                attributes['bowlers'][current_bowler_id]['runs_conceded']+=4
                attributes['batsmen'][current_batsmen_id]['fours']+=1
            elif bound == '6':
                print("Ball "+str(i)+' - '+attributes['bowlers'][current_bowler_id]['name']+" to "+attributes['batsmen'][current_batsmen_id]['name']+' : '+'6')
                team_score+=6
                attributes['batsmen'][current_batsmen_id]['runs_scored']+=6
                attributes['bowlers'][current_bowler_id]['runs_conceded']+=6
                attributes['batsmen'][current_batsmen_id]['sixes']+=1
            

        
    else:
        print("Ball "+str(i)+": "+attributes['batsmen'][current_batsmen_id]['name']+' '+result+' at '+ str(attributes['batsmen'][current_batsmen_id]['runs_scored']))
        attributes['batsmen'][current_batsmen_id]['out_to']=attributes['bowlers'][current_bowler_id]['name']
        fall_of_wickets.append(team_score)
        team_wickets+=1
        attributes['bowlers'][current_bowler_id]['wickets_taken']+=1
        if team_wickets==10:
            print("Team is all out at "+str(team_score))
            break
        for j in range(len(attributes['batsmen'])):
            if attributes['batsmen'][j]['balls_faced']==0 and (j not in current_batsmen):
                print(str(j)+'  '+attributes['batsmen'][j]['name'])
        choser=int(input("Choose the next batsman :"))
        next_batsman_id=choser
        attributes['batsmen'][next_batsman_id]['batting_order']=team_wickets+2
        current_batsmen.remove(current_batsmen_id)
        current_batsmen.append(next_batsman_id)
        current_batsmen_id=next_batsman_id

    
        if i%6==0 and i!=120:
            time.sleep(4)
            os.system('cls')
            overs=int(i/6)
            print('Summary :'+str(team_score)+'/'+str(team_wickets)+' after '+str(overs)+' overs Required run rate:'+str(round(((target-team_score)/(20-overs)),2))
                    +' Required runs:'+str(target-team_score)+'\n\n'+'Current Batsmen :')
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
            choser=int(input("Choose the id of bowler from above:"))
            current_bowler_id=choser
            print('\n')
    if int(attributes['bowlers'][current_bowler_id]['balls_bowled']%6)==0:
        print('Summary :'+str(team_score)+'/'+str(team_wickets)+' after '+str(int(i/6))+' overs '+'\n')
    else:
        print('Summary :'+str(team_score)+'/'+str(team_wickets)+' after '+str(int(i/6))+'.'+str((attributes['bowlers'][current_bowler_id]['balls_bowled'])%6)+' overs '+'\n')
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
        print(str(fall_of_wickets[i])+'- '+str(i))
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
    
chase(team_score+1,attributes2)
f = open(Player1, "w+")
f.close()
f=open(Player2,"w+")
f.close()