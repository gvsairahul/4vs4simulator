import csv, os, time
import pandas as pd
import numpy as np
from out_sim1 import out_calculator,boundary_calculator, runs_calculator, change_batsman, toss, best_bowling,notout_cal,fifty_cal
from second_innings import chase
import xlsxwriter
from Super_over import superover

def initialise(f1,f2,attributes):
    batsman_number=0
    bowler_number=0
    non_header=False
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
            attributes['batsmen'][batsman_number]['ratio']=float(row[8])
            attributes['batsmen'][batsman_number]['out_to']='Not Out'
            batsman_number+=1
            non_header = True
    non_header = False
    for row in f2:
        if non_header and float(row[4])>0 and float(row[5])>0:
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

def write_to_stats(BAT,BOWL,BATTING_COLS,BOWLING_COLS,Bat_rem,Bowl_rem,Bat_stats,Bowl_stats):
    
    BAT['Orange Cap'] = BAT['Orange Cap'] + BAT['runs_scored']

    BAT['Balls Faced'] = BAT['Balls Faced'] + BAT['balls_faced']

    BAT['6s'] = BAT['6s']+ BAT['sixes']

    BAT['4s'] = BAT['4s'] + BAT['fours']

    BAT.loc[BAT['balls_faced'] !=0, 'Innings' ] = BAT['Innings'] + 1

    BAT.loc[BAT['runs_scored'] >=100 , '100'] = BAT['100']+1

    BAT.loc[BAT['Highest'] < BAT['runs_scored'] , 'Highest'] = BAT['runs_scored']

    BAT['Not Outs'] = BAT.apply(lambda row: notout_cal(row['Not Outs'],row['balls_faced'],row['out_to']),axis=1)

    BAT['50'] = BAT.apply(lambda row: fifty_cal(row['50'],row['runs_scored']),axis=1)

    BAT=BAT[BATTING_COLS]

    BOWL['Runs conceeded'] = BOWL['Runs conceeded'] + BOWL['runs_conceded']

    BOWL['Dots'] = BOWL['Dots'] + BOWL['dots']

    BOWL['Purple Cap'] = BOWL['Purple Cap'] + BOWL['wickets_taken']

    BOWL['Balls'] = BOWL['Balls'] + BOWL['balls_bowled']

    BOWL.loc[BOWL['balls_bowled'] !=0, 'Innings' ] = BOWL['Innings'] + 1

    BOWL.loc[BOWL['wickets_taken'] == 4 , '4fer'] = BOWL['4fer']+1

    BOWL.loc[BOWL['wickets_taken'] >4  , '5fer'] = BOWL['5fer']+1

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

    



