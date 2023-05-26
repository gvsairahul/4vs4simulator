import csv, os, time
import pandas as pd
import numpy as np
from out_sim1 import out_calculator,boundary_calculator, runs_calculator, change_batsman, best_bowling,notout_cal,fifty_cal
# import xlsxwriter

def ball_result(balls,batsman,bowler,target,team_wickets,team_score):
    result = out_calculator(balls,batsman,bowler,target,team_wickets,team_score)
    if result == 'notout':
        result = boundary_calculator(balls,batsman,bowler,target,team_wickets,team_score)
        if result == 'N':
            result = runs_calculator(balls,batsman,bowler,target,team_wickets,team_score)


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
        print("\n Ball: " + str((int(int(balls-1)/6))) + '.' + str(6- int((132-balls))%6) + ' - '+ bowler['name']+ " to "+ batsman['name']+' : ' + str(result) + '\n')


    else:
        team_wickets+=1
        batsman['out_to'] = bowler['name']
        bowler['wickets_taken']+=1
        bowler['dots']+=1
        print("\n Ball: " + str((int(int(balls-1)/6))) + '.' + str(6- int((132-balls))%6) + ' - '+ bowler['name']+ " to "+ batsman['name']+' : ' + str(result) + ' for '+ str(batsman['runs_scored'])+'\n')


    return [team_score,team_wickets,batsman,bowler]

def print_summary(team_score,team_wickets,attributes,current_batsmen,current_batsmen_id,target,balls):

    if int(target) == 1800 :
        if balls%6 != 0:
            print('\nScore:  ' + str(team_score) + '/' + str(team_wickets) + ' after ' + str((balls/6)) + '.' + str(6- (132-balls)%6) + ' Overs Current run rate:'
            +  str(round(float(team_score*6/balls),2)) )
        else :
            print('\nScore:  ' + str(team_score) + '/' + str(team_wickets) + ' after ' + str((balls/6))  + ' Overs Current run rate:'
            +  str(round(float(team_score*6/balls),2)) )
    elif balls != 120 and int(target) !=1800:
        if balls%6 != 0:

            print('\nScore:  ' + str(team_score) + '/' + str(team_wickets) + ' after ' + str((balls/6)) + '.' + str(6- (132-balls)%6) + ' Overs  Current run rate : '
            +  str(round(float(team_score*6/balls),2)) + ' Required Run rate : ' + str(round(float((target-team_score)*6/(120-balls)),2)))
        else :
            print('\nScore:  ' + str(team_score) + '/' + str(team_wickets) + ' after ' + str((balls/6)) +  ' Overs  Current run rate : '
            +  str(round(float(team_score*6/balls),2)) + ' Required Run rate : ' + str(round(float((target-team_score)*6/(120-balls)),2)))

        print('\nNeed ' + str(target - team_score) + ' runs to win from ' + str(120-balls) + ' Balls' )

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
