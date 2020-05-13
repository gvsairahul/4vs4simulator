import csv, os,time
from out_sim1 import out_calculator, runs_calculator, change_batsman, toss
from second_innings import chase
import xlsxwriter
#ids and associations
ids_csv='C:\\Users\\rahul\\Desktop\\FourvsFour\\Simulator\\Teams\\Master_data_sheet - Sheet2.csv'
ids_data=csv.reader(open(ids_csv))
#Master_data_sheet
master_csv='C:\\Users\\rahul\\Desktop\\FourvsFour\\Simulator\\Teams\\Master_data_sheet - Sheet1.csv'
master_data=csv.reader(open(master_csv))
associations={}
for row in ids_data:
    print(str(row[1])+' '+row[0])
    associations[row[1]]=row[0]
player1_id=input("Choose the home team id: ")
player2_id=input("Choose the away team id: ")
call=input(associations[player2_id]+ " calls the toss, Heads or Tails:")
toss_result=toss()
if call==toss_result:
    choosing=input(associations[player2_id]+',You won the toss, Will u Bat or Bowl:')
    if choosing=='Bat':
        first_innings_id=player2_id
        second_innings_id=player1_id
    else:
        first_innings_id=player1_id
        second_innings_id=player2_id
else:
    choosing=input(associations[player1_id]+',You won the toss, Will u Bat or Bowl:')
    if choosing=='Bat':
        first_innings_id=player1_id
        second_innings_id=player2_id
    else:
        first_innings_id=player2_id
        second_innings_id=player1_id
print(associations[first_innings_id])

non_header=False


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

for row in master_data:
    if non_header:
        if row[9]==first_innings_id:
            attributes['batsmen'].append({})
            attributes['batsmen'][batsman_number]['batting_order']=0
            attributes['batsmen'][batsman_number]['name']=row[1].strip(' ')
            attributes['batsmen'][batsman_number]['out_to']='Not Out'
            attributes['batsmen'][batsman_number]['runs_scored']=0
            attributes['batsmen'][batsman_number]['balls_faced']=0
            attributes['batsmen'][batsman_number]['fours']=0
            attributes['batsmen'][batsman_number]['sixes']=0
            attributes['batsmen'][batsman_number]['ratio']=float(row[8])
            attributes['batsmen'][batsman_number]['average']=float(row[2])
            attributes['batsmen'][batsman_number]['strikerate']=float(row[3])
            batsman_number+=1
            if float(row[4])>0 and float(row[5])>0:
                attributes2['bowlers'].append({})
                attributes2['bowlers'][bowler_number2]['name']=row[1].strip(' ')
                attributes2['bowlers'][bowler_number2]['balls_bowled']=0
                attributes2['bowlers'][bowler_number2]['dots']=0
                attributes2['bowlers'][bowler_number2]['runs_conceded']=0
                attributes2['bowlers'][bowler_number2]['wickets_taken']=0
                attributes2['bowlers'][bowler_number2]['economy']=float(row[4])
                attributes2['bowlers'][bowler_number2]['average']=float(row[5])
                bowler_number2+=1
        elif row[9]==second_innings_id:
            attributes2['batsmen'].append({})
            attributes2['batsmen'][batsman_number2]['batting_order']=0
            attributes2['batsmen'][batsman_number2]['name']=row[1].strip(' ')
            attributes2['batsmen'][batsman_number2]['out_to']='Not Out'
            attributes2['batsmen'][batsman_number2]['runs_scored']=0
            attributes2['batsmen'][batsman_number2]['balls_faced']=0
            attributes2['batsmen'][batsman_number2]['fours']=0
            attributes2['batsmen'][batsman_number2]['sixes']=0
            attributes2['batsmen'][batsman_number2]['ratio']=float(row[8])
            attributes2['batsmen'][batsman_number2]['average']=float(row[2])
            attributes2['batsmen'][batsman_number2]['strikerate']=float(row[3])
            batsman_number2+=1
            if float(row[4])>0 and float(row[5])>0:
                attributes['bowlers'].append({})
                attributes['bowlers'][bowler_number]['name']=row[1].strip(' ')
                attributes['bowlers'][bowler_number]['balls_bowled']=0
                attributes['bowlers'][bowler_number]['dots']=0
                attributes['bowlers'][bowler_number]['runs_conceded']=0
                attributes['bowlers'][bowler_number]['wickets_taken']=0
                attributes['bowlers'][bowler_number]['economy']=float(row[4])
                attributes['bowlers'][bowler_number]['average']=float(row[5])
                bowler_number+=1
    non_header=True
current_batsmen=[]
current_bowler_id=0
team_score=0
team_wickets=0
fall_of_wickets=[]
for j in range(len(attributes['batsmen'])):
    if attributes['batsmen'][j]['balls_faced']==0 and (j not in current_batsmen):
        print(str(j)+'  '+attributes['batsmen'][j]['name'])
choser=int(input("Choose the  batsman on strike:"))
current_batsmen.append(choser)
current_batsmen_id=choser
attributes['batsmen'][current_batsmen_id]['batting_order']=1
for j in range(len(attributes['batsmen'])):
    if attributes['batsmen'][j]['balls_faced']==0 and (j not in current_batsmen):
        print(str(j)+'  '+attributes['batsmen'][j]['name'])
choser=int(input("Choose the  batsman on non strike:"))
attributes['batsmen'][choser]['batting_order']=2
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
        fall_of_wickets.append(team_score)
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
print('Batting Scorecard')
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
    print(str(fall_of_wickets[i])+'-'+str(i))
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

second_innings_results=chase(team_score+1,attributes2)
if second_innings_results[1]>(team_score):
    print(associations[second_innings_id]+" won by "+str(10-second_innings_results[2])+" wickets")
elif second_innings_results[1]<(team_score+1):
    print(associations[first_innings_id]+" won by "+str(team_score-second_innings_results[1])+" runs")
else:
    print("It's a tie")

workbook=xlsxwriter.Workbook('C:\\Users\\rahul\\Desktop\\FourvsFour\\Simulator\\reports\\'+associations[player1_id]+'vs'+associations[player2_id]+'.xlsx')
batsman_first_innings=workbook.add_worksheet('batsman_first_innings')
batsman_second_innings=workbook.add_worksheet('batsman_second_innings')
bowler_first_innings=workbook.add_worksheet('bowler_first_innings')
bowler_second_innings=workbook.add_worksheet('bowler_second_innings')

for i in range(len(attributes['batsmen'])):
    if attributes['batsmen'][i]['balls_faced']>0:
        k=0
        for j in attributes['batsmen'][i]:
            batsman_first_innings.write(0,k,j)
            batsman_first_innings.write(attributes['batsmen'][i]['batting_order'],k,attributes['batsmen'][i][j])
            k+=1

for i in range(len(second_innings_results[0]['batsmen'])):
    if second_innings_results[0]['batsmen'][i]['balls_faced']>0:
        k=0
        for j in second_innings_results[0]['batsmen'][i]:
            batsman_second_innings.write(0,k,j)
            batsman_second_innings.write(second_innings_results[0]['batsmen'][i]['batting_order'],k,second_innings_results[0]['batsmen'][i][j])
            k+=1
k2=0
for i in range(len(attributes['bowlers'])):
    if attributes['bowlers'][i]['balls_bowled']>0:
        k=0
        for j in attributes['bowlers'][i]:
            bowler_first_innings.write(0,k,j)
            bowler_first_innings.write(k2+1,k,attributes['bowlers'][i][j])
            k+=1
        k2+=1
k3=0
for i in range(len(attributes2['bowlers'])):
    if attributes2['bowlers'][i]['balls_bowled']>0:
        k=0
        for j in second_innings_results[0]['bowlers'][i]:
            bowler_second_innings.write(0,k,j)
            bowler_second_innings.write(k3+1,k,second_innings_results[0]['bowlers'][i][j])
            k+=1
        k3+=1
workbook.close()
