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
            
            
