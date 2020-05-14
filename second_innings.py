import csv, os, time
from out_sim1 import out_calculator, runs_calculator, change_batsman, toss,boundary_calculator
def chase(target,attributes):
    print("The target is "+str(target))
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

            bound = boundary_calculator(i,attributes['batsmen'][current_batsmen_id],attributes['bowlers'][current_bowler_id])
            if bound == 'N':
                runs1=runs_calculator(i,attributes['batsmen'][current_batsmen_id],attributes['bowlers'][current_bowler_id])
            
                print("Ball "+str(i)+' - '+attributes['bowlers'][current_bowler_id]['name']+" to "+attributes['batsmen'][current_batsmen_id]['name']+' : '+ runs1)
            
                runs = int(runs1)
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
            #time.sleep(4)
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

    return [attributes,team_score,team_wickets]
