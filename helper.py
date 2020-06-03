import csv, os, time
import pandas as pd
import numpy as np
from out_sim1 import out_calculator,boundary_calculator, runs_calculator, change_batsman, best_bowling,notout_cal,fifty_cal
import xlsxwriter


def initialise(g1,g2):
    f1 = csv.reader(open(g1))
    f2 = csv.reader(open(g2))
    non_header=False
    non_header2=False
    attributes={}
    attributes['batsmen']=[]
    attributes['bowlers']=[]
    batsman_number=0
    bowler_number2=0

    for row in f1:
        if non_header:
            attributes['batsmen'].append({})
            attributes['batsmen'][batsman_number]['name']=row[1].strip(' ')
            attributes['batsmen'][batsman_number]['average']=float(row[2])
            attributes['batsmen'][batsman_number]['strikerate']=float(row[3])
            attributes['batsmen'][batsman_number]['runs_scored']=0
            attributes['batsmen'][batsman_number]['balls_faced']=0
            attributes['batsmen'][batsman_number]['fours']=0
            attributes['batsmen'][batsman_number]['sixes']=0
            attributes['batsmen'][batsman_number]['4s ratio']=float(row[6])
            attributes['batsmen'][batsman_number]['out_to']='Not Out'
            attributes['batsmen'][batsman_number]['6s ratio'] = float(row[7])
            attributes['batsmen'][batsman_number]['batting_order'] = 12
            batsman_number+=1
        non_header = True
        
    for row in f2:
        if non_header2:

            if float(row[4])>0 and float(row[5])>0:
                attributes['bowlers'].append({})
                attributes['bowlers'][bowler_number2]['name']=row[1].strip(' ')
                attributes['bowlers'][bowler_number2]['economy']=float(row[4])
                attributes['bowlers'][bowler_number2]['average']=float(row[5])
                attributes['bowlers'][bowler_number2]['balls_bowled']=0
                attributes['bowlers'][bowler_number2]['runs_conceded']=0
                attributes['bowlers'][bowler_number2]['wickets_taken']=0
                attributes['bowlers'][bowler_number2]['dots']=0
                attributes['bowlers'][bowler_number2]['prop_bowl'] = float(row[8])
                attributes['bowlers'][bowler_number2]['Bowler_type'] = row[9].strip(' ')
                bowler_number2+=1
        non_header2=True

    return [attributes]


def write_to_stats(BAT,BOWL,BATTING_COLS,BOWLING_COLS,Bat_rem,Bowl_rem,Bat_stats,Bowl_stats):
    
    BAT['Orange Cap'] = BAT['Orange Cap'] + BAT['runs_scored']

    BAT['Balls Faced'] = BAT['Balls Faced'] + BAT['balls_faced']

    BAT['6s'] = BAT['6s']+ BAT['sixes']

    BAT['4s'] = BAT['4s'] + BAT['fours']

    BAT['Innings'] = np.where(BAT['balls_faced'] !=0, BAT['Innings'] + 1 , BAT['Innings'])

    BAT['100'] = np.where(BAT['runs_scored'] >=100, BAT['100']+1 , BAT['100'])


    BAT['Highest'] = np.where(BAT['Highest'] < BAT['runs_scored'] ,  BAT['runs_scored'] , BAT['Highest'])

    BAT['Not Outs'] = BAT.apply(lambda row: notout_cal(row['Not Outs'],row['balls_faced'],row['out_to']),axis=1)

    BAT['50'] = BAT.apply(lambda row: fifty_cal(row['50'],row['runs_scored']),axis=1)

    BAT=BAT[BATTING_COLS]

    BOWL['Runs conceeded'] = BOWL['Runs conceeded'] + BOWL['runs_conceded']

    BOWL['Dots'] = BOWL['Dots'] + BOWL['dots']

    BOWL['Purple Cap'] = BOWL['Purple Cap'] + BOWL['wickets_taken']

    BOWL['Balls'] = BOWL['Balls'] + BOWL['balls_bowled']

    BOWL['Innings'] = np.where(BOWL['balls_bowled'] !=0 , BOWL['Innings'] + 1,BOWL['Innings'])

    BOWL['4fer'] = np.where(BOWL['wickets_taken'] == 4 , BOWL['4fer'] + 1 , BOWL['4fer'])

    BOWL['5fer'] = np.where(BOWL['wickets_taken'] >4 , BOWL['5fer']+1 , BOWL['5fer'])


    BOWL['Best Figures'] = BOWL.apply(lambda row: best_bowling(row['Best Figures'], row['wickets_taken'] , row['runs_conceded']),axis=1)

    BOWL = BOWL[BOWLING_COLS]

    bat_final = pd.concat([BAT,Bat_rem],axis=0)
    bat_final = bat_final[BATTING_COLS]
    bowl_final = pd.concat([BOWL,Bowl_rem],axis=0)
    bowl_final = bowl_final[BOWLING_COLS]
    bat_final.sort_values("Orange Cap",axis=0,ascending = False,inplace = True ,kind = 'quicksort',na_position = 'last' )
    bowl_final.sort_values("Purple Cap",axis=0,ascending = False,inplace = True ,kind = 'quicksort',na_position = 'last' )

    bat_final.to_csv(Bat_stats)
    bowl_final.to_csv(Bowl_stats)


def Bowler_Select(attributes,current_bowler_id) :
    lll=[]
    for j in range(len(attributes['bowlers'])):
        if attributes['bowlers'][j]['balls_bowled']<=18 and j!=current_bowler_id:
            overs=str(int(attributes['bowlers'][j]['balls_bowled']/6))
            spare_balls=str(int(attributes['bowlers'][j]['balls_bowled']%6))
            overs=overs+'.'+spare_balls
            print(str(j)+' '+attributes['bowlers'][j]['name']+" "+overs+'-'+str(attributes['bowlers'][j]['dots'])
            +'-'+str(attributes['bowlers'][j]['runs_conceded'])+'-'+str(attributes['bowlers'][j]['wickets_taken']))
            lll.append(str(j))
    answer = '0' 
    while answer != '1':
        choser=input("Choose the valid id of bowler from above:")
        if str(choser) not in lll or choser == '':
            answer = '2'
        else:
            answer = input("If the bowler chosen is " + attributes['bowlers'][int(choser)]['name'] + " Press 1: ")    
         

    return int(choser)

def Batsman_Select(attributes,current_batsman_id,current_batsmen,order):
    ll=[]
    for j in range(len(attributes['batsmen'])):
        if attributes['batsmen'][j]['balls_faced']==0 and (j not in current_batsmen):
            print(str(j)+'  '+attributes['batsmen'][j]['name'])
            ll.append(str(j))
    answer = '0' 
     
    while answer != '1':
        if order == 3:
            choser=input("Choose the next batsman : ")
        elif order == 1:
            choser = input("Choose the opener on strike : ")
        elif order == 2:
            choser = input("Choose the opener on Non Strike : ")
        if choser not in ll or choser == '':
            answer='2'
        else:
            answer = input("If the batsman is " + attributes['batsmen'][int(choser)]['name'] + " Press 1: ")    
    return int(choser)



def print_scorecard(attributes,team_score,balls,team_wickets,fall_of_wickets):
    ll = []
    for i in range(len(attributes['batsmen'])):
        if attributes['batsmen'][i]['balls_faced'] > 0:
            ll.append(attributes['batsmen'][i]['batting_order'])
    ll.sort()
    for k in ll:
        for i in range(len(attributes['batsmen'])):
            if attributes['batsmen'][i]['balls_faced']>0:
                attributes['batsmen'][i].pop('average', None)
                attributes['batsmen'][i].pop('ratio', None)
                attributes['batsmen'][i].pop('strikerate', None)
                if str(attributes['batsmen'][i]['out_to'])!='Not Out' and attributes['batsmen'][i]['batting_order'] ==k:
                    str1 = attributes['batsmen'][i]['name']
                    str2 = "Out To:" +str(attributes['batsmen'][i]['out_to'])
                    str3 = str(attributes['batsmen'][i]['runs_scored'])+"("+str(attributes['batsmen'][i]['balls_faced'])+") "
                    str6 = "4s:"+str(attributes['batsmen'][i]['fours'])+" 6s:"+str(attributes['batsmen'][i]['sixes'])
                    str7 = ""
                    str4 = ""
                    str5 = ""
                    l1 = len(str1)
                    l2 = len(str2)
                    l3 =len(str3)

                    for i in range(1,25-l1):
                        str4 = str4 + " "
                    for i in range(1,32-l2):
                        str5 = str5 + " "
                    for i in range(1,10-l3):
                        str7 = str7+ " "
                    print(str1+str4+str2+str5+str3+str7+str6)
                
                elif str(attributes['batsmen'][i]['out_to']) == 'Not Out' and attributes['batsmen'][i]['batting_order'] ==k:
                    str1 = attributes['batsmen'][i]['name']
                    str2 = str(attributes['batsmen'][i]['out_to'])
                    str3 = str(attributes['batsmen'][i]['runs_scored'])+"("+str(attributes['batsmen'][i]['balls_faced'])+") " 
                    str6 = "4s:"+str(attributes['batsmen'][i]['fours'])+" 6s:"+str(attributes['batsmen'][i]['sixes'])
                    l1 = len(str1)
                    l2 = len(str2)
                    l3 = len(str3)
                    str4 = ""
                    str5 = ""
                    str7 = ""
                    for i in range(1,25-l1):
                        str4 = str4 + " "
                    for i in range(1,32-l2):
                        str5 = str5 + " "
                    for i in range(1,10-l3):
                        str7 = str7 + " "
                    print(str1+str4+str2+str5+str3+str7+str6)
    if balls%6 == 0:
        print('\nScore after ' + str(balls/6) + ' Overs : ' + str(team_score) + '/' + str(team_wickets))
    else:
        print('\nScore after ' + str(int(balls/6)) +'.' +str(int(balls%6)) + ' Overs : ' + str(team_score) + '/' + str(team_wickets))
    
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
            str1 = attributes['bowlers'][i]['name']
            str2 = overs+'-'+str(attributes['bowlers'][i]['dots'])+'-'+str(attributes['bowlers'][i]['runs_conceded'])+'-'+str(attributes['bowlers'][i]['wickets_taken'])

            str3 =""

            for i in range(1,25 -len(str1)):
                str3 = str3 + " "
            print(str1+str3+str2)
    