import csv, os, time
from out_sim1 import out_calculator, runs_calculator, change_batsman, toss
from second_innings import chase

#Batting Team
csvFile='C:\\Users\\rahul\\Desktop\\FourvsFour\\Simulator\\Teams\\Data_for_simulation - CSK2019f.csv'
#Bowling Team
csvFile2='C:\\Users\\rahul\\Desktop\\FourvsFour\\Simulator\\Teams\\Data_for_simulation - MI2019F.csv'
call=input("Heads or Tails:")
toss_result=toss()
if call==toss_result:
    choosing=input('Player1,You won the toss, Will u Bat or Bowl:')
    if choosing=='Bat':
        csvData=csv.reader(open(csvFile))
        csvData2=csv.reader(open(csvFile2))
    else:
        csvData2=csv.reader(open(csvFile))
        csvData=csv.reader(open(csvFile2))
else:
    choosing=input('Player2,You won the toss, Will u Bat or Bowl:')
    if choosing=='Bat':
        csvData2=csv.reader(open(csvFile))
        csvData=csv.reader(open(csvFile2))
    else:
        csvData=csv.reader(open(csvFile))
        csvData2=csv.reader(open(csvFile2))

non_header=False
non_header2=False


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
        attributes['batsmen'][batsman_number]['average']=float(row[2])
        attributes['batsmen'][batsman_number]['strikerate']=float(row[3])
        attributes['batsmen'][batsman_number]['runs_scored']=0
        attributes['batsmen'][batsman_number]['balls_faced']=0
        attributes['batsmen'][batsman_number]['fours']=0
        attributes['batsmen'][batsman_number]['sixes']=0
        attributes['batsmen'][batsman_number]['ratio']=float(row[8])
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
    non_header=True

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
    non_header2=True
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
        runs=runs_calculator(i,attributes['batsmen'][current_batsmen_id],attributes['bowlers'][current_bowler_id])
        print("Ball "+str(i)+' - '+attributes['bowlers'][current_bowler_id]['name']+" to "+attributes['batsmen'][current_batsmen_id]['name']+' : '+str(runs))
        team_score+=runs
        attributes['batsmen'][current_batsmen_id]['runs_scored']+=runs
        attributes['bowlers'][current_bowler_id]['runs_conceded']+=runs
        if runs==0:
            attributes['bowlers'][current_bowler_id]['dots']+=1
        if runs==4:
            attributes['batsmen'][current_batsmen_id]['fours']+=1
        elif runs==6:
            attributes['batsmen'][current_batsmen_id]['sixes']+=1
        if runs==1:
            current_batsmen_id=change_batsman(current_batsmen,current_batsmen_id)
    else:
        print("Ball "+str(i)+": "+attributes['batsmen'][current_batsmen_id]['name']+' '+result+' at '+ str(attributes['batsmen'][current_batsmen_id]['runs_scored']))
        attributes['batsmen'][current_batsmen_id]['out_to']=attributes['bowlers'][current_bowler_id]['name']
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
        current_batsmen.remove(current_batsmen_id)
        current_batsmen.append(next_batsman_id)
        current_batsmen_id=next_batsman_id
    time.sleep(3)
    if i%6==0 and i!=120:
        os.system('cls')
        print('Summary :'+str(team_score)+'/'+str(team_wickets)+' after '+str(int(i/6))+' overs '+'\n\n'+'Current Batsmen :')
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
                print(str(j)+' '+attributes['bowlers'][j]['name']+' overs_left:'+str(int((24-attributes['bowlers'][j]['balls_bowled'])/6)))
        choser=int(input("Choose the id of bowler from above:"))
        current_bowler_id=choser
        print('\n')
if int(attributes['bowlers'][current_bowler_id]['balls_bowled']%6)==0:
    print('Summary :'+str(team_score)+'/'+str(team_wickets)+' after '+str(int(i/6))+' overs '+'\n')
else:
    print('Summary :'+str(team_score)+'/'+str(team_wickets)+' after '+str(int(i/6))+str((attributes['bowlers'][current_bowler_id]['balls_bowled'])%6)+' overs '+'\n')
print('Batting Scorecard')
for i in range(len(attributes['batsmen'])):
    if attributes['batsmen'][i]['balls_faced']>0:
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
print('\nBowling Scorecard\n')
for i in range(len(attributes['bowlers'])):
    if attributes['bowlers'][i]['balls_bowled']>0:
        overs=str(int(attributes['bowlers'][i]['balls_bowled']/6))
        spare_balls=str(int(attributes['bowlers'][i]['balls_bowled']%6))
        overs=overs+'.'+spare_balls
        print(attributes['bowlers'][i]['name']+" "+overs+'-'+str(attributes['bowlers'][i]['dots'])
        +'-'+str(attributes['bowlers'][i]['runs_conceded'])+'-'+str(attributes['bowlers'][i]['wickets_taken']))

chase(team_score+1,attributes2)
