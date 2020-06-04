import pandas as pd 
import numpy as np
from helper import initialise
from out_sim1 import out_calculator,boundary_calculator, runs_calculator, change_batsman, best_bowling,notout_cal,fifty_cal


master = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Master_data_sheet.csv'

col_list = ["PLAYERS","Batsman_avg","Batsman_strikerate","Bowler_economy","Bowler_average","4s ratio","6s ratio","Balls per innings","Bowler Style"]

Col_Test = ["Batsman","Bowler","Ball","0","1","2","3","4","6","Out"]

master1 = pd.read_csv(master)
master1 = master1[master1['Draft3_Player_id'] > 0]

master1 = master1[col_list]


Player1 = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player1.csv'
Player2 =  'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Teams\\Data_for_simulation - Player2.csv'

master1.to_csv(Player1)
master1.to_csv(Player2)

ff = pd.DataFrame(columns=Col_Test)


A = initialise(Player1,Player2)
attributes = A[0]

for j in range(len(attributes['batsmen'])):
    print(attributes['batsmen'][j]['name'])
        
    for kk in range(len(attributes['bowlers'])):
           

        list =[1,37,67,85,91,97,103,109]
        kkkk=0
        for i in list :
            out = out_calculator(i,attributes['batsmen'][j],attributes['bowlers'][kk],1800,2,75)
            bound = boundary_calculator(i,attributes['batsmen'][j],attributes['bowlers'][kk],1800,2,75)
            runs = runs_calculator(i,attributes['batsmen'][j],attributes['bowlers'][kk],1800,2,75)
            four = round(bound[0] * (1-out),3)
            six = round(bound[1] * (1-out),3)
            run1 = round(1-out-four-six,3)
            dot = round(runs[0]*run1,3)
            sing = round(runs[1]*run1,3)
            doub = round(runs[2]*run1,3)
            triple = round(run1/120,3)
            out = round(out,3)
            x1 = i
            if x1 == 1:
                x2 = 36
            elif x1 == 37:
                x2 = 66
            elif x1 == 67:
                x2 = 84 
            elif x1 == 85:
                x2 = 91 
            elif x1 == 91:
                x2 = 96 
            elif x1 == 97:
                x2 = 102 
            elif x1 == 102:
                x2 = 108 
            elif x1 == 109:
                x2 = 120     
            
         
            sttt = str(x1) +' to ' + str(x2)
            ff = ff.append(pd.DataFrame({'Batsman' : [attributes['batsmen'][j]['name']] ,'Bowler' : attributes['bowlers'][kk]['name'] ,'Ball' : sttt, '0' : [dot] , '1' : [sing] ,'2' : [doub] , '3' : [triple] , '4' : [four], '6' : [six] , 'Out' : [out]}))
            kkkk+=1
 
           


ff.to_csv('C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\Bowler_to_Batsman.csv')        



#print(attributes)

