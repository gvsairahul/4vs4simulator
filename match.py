import csv, os, time
import pandas as pd
import numpy as np
from out_sim1 import out_calculator,boundary_calculator, runs_calculator, change_batsman, toss, best_bowling,notout_cal,fifty_cal
import xlsxwriter
from helper import initialise,write_to_stats,Bowler_Select,print_scorecard,Batsman_Select
from bowl_a_ball import ball_result,update_result,print_summary



def Innings_run(attributes,target,a,b):
    fall_of_wickets = []
    current_batsmen=[]
    current_batsmen_id = 12
    current_bowler_id=12
    team_score=0
    team_wickets=0
    current_batsmen_id = Batsman_Select(attributes,current_batsmen_id,current_batsmen,1)
    current_batsmen.append(current_batsmen_id)
    attributes['batsmen'][current_batsmen_id]['batting_order'] = 1
    next_batsmen_id = Batsman_Select(attributes,current_batsmen_id,current_batsmen,2)
    current_batsmen.append(next_batsmen_id)
    attributes['batsmen'][current_batsmen_id]['batting_order'] = 2
    current_bowler_id = Bowler_Select(attributes,current_bowler_id)
    alll=120

    for i in range(a,b):
    
        result = ball_result(i,attributes['batsmen'][current_batsmen_id],attributes['bowlers'][current_bowler_id])
    
        update_result(result,i,team_score,team_wickets,attributes['batsmen'][current_batsmen_id],attributes['bowlers'][current_bowler_id])
    
        if result != 'out':
            team_score += int(result)
    
        if str(result) == '1' or str(result) == '3':
            current_batsmen_id=change_batsman(current_batsmen,current_batsmen_id)
    
        elif str(result) == 'out':
            team_wickets+=1
            if team_wickets==10:
                alll = i
                print("Team is all out at "+str(team_score))
            #kb = kb + "Team is all out at "+str(team_score) + '\n'
                break
            elif team_wickets != 10 and i != b-1:
                current_batsmen.remove(current_batsmen_id)
                current_batsmen_id = Batsman_Select(attributes,current_batsmen_id,current_batsmen,3)
                current_batsmen.append(current_batsmen_id)
                attributes['batsmen'][current_batsmen_id]['batting_order']=team_wickets+2
        if team_score >= target:
            break
        if i%6==0 and i!=b-1:
            #time.sleep(4)
            #os.system('cls')
            overs=int(i/6)
            print_summary(team_score,team_wickets,attributes,current_batsmen,current_batsmen_id,target,i)
        
        
            current_batsmen_id=change_batsman(current_batsmen,current_batsmen_id)

            current_bowler_id = Bowler_Select(attributes,current_bowler_id)


    print_scorecard(attributes,team_score,alll,team_wickets,fall_of_wickets)

    return [attributes,team_score,team_wickets]


def Super_over(attributes1,attributes2):
    A = Innings_run(attributes2,1800,121,127)

    B = Innings_run(attributes1,A[1] + 1,121,127)

    if A[1] > B[1]:
        return 2
    elif B[1] > A[1]:
        return 1
    else : 
        return Super_over(attributes2,attributes1)

