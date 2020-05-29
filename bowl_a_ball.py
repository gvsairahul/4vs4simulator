import csv, os, time
import pandas as pd
import numpy as np
from out_sim1 import out_calculator,boundary_calculator, runs_calculator, change_batsman, toss, best_bowling,notout_cal,fifty_cal
from second_innings import chase
import xlsxwriter
from Super_over import superover


def ball_result(balls,batsman,bowler):
    result = out_calculator(balls,batsman,bowler)
    if result == 'notout':
        result = boundary_calculator(balls,batsman,bowler)
        if result == 'N':
            result = runs_calculator(balls,batsman,bowler)
    

    return result

def update_result(result,balls,team_score,team_wickets,batsman,bowler):
    batsman['balls_faced']+=1
    bowler['balls_bowled']+=1
    if result != 'out':
        rr = int(result)
        team_score+=rr
        batsman['runs_scored']+=rr
        bowler['runs_conceded']+=rr
        if rr == 0:
            bowler['dots']+=1
        elif rr == 4:
            batsman['fours']+=1
        elif rr == 6:
            batsman['sixes']+=1
        print("\n Ball: " + str((int(int(balls-1)/6))%20) + '.' + str(6- int((132-balls))%6) + ' - '+ bowler['name']+ " to "+ batsman['name']+' : ' + str(result) + '\n')
   
    
    else:
        team_wickets+=1
        batsman['out_to'] = bowler['name']
        bowler['wickets_taken']+=1
        bowler['dots']+=1
        print("\n Ball: " + str((int(int(balls-1)/6))%20) + '.' + str(6- int((132-balls))%6) + ' - '+ bowler['name']+ " to "+ batsman['name']+' : ' + str(result) + ' for '+ str(batsman['runs_scored'])+'\n')
   
    
    return [team_score,team_wickets,batsman,bowler]

def print_summary(team_score,team_wickets,attributes,current_batsmen,current_batsmen_id,target,balls):
    
    if int(target) == 0:
        print('Score:  ' + str(team_score) + '/' + str(team_wickets) + ' after ' + str((balls/6)%20) + '.' + str(6- (132-balls)%6) + ' Overs Current run rate:'  
        +  str(round(float(team_score*6/balls),2)) )
    
    elif balls != 120 and int(target) !=0:
        print('Score:  ' + str(team_score) + '/' + str(team_wickets) + ' after ' + str((balls/6)%20) + '.' + str(6- (132-balls)%6) + ' Overs  Current run rate : '  
        +  str(round(float(team_score*6/balls),2)) + ' Required Run rate : ' + str(round(float((target-team_score)*6/(120-balls)),2)))
    
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

        


        
