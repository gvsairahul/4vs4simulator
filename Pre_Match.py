import csv, os, time
import pandas as pd
import numpy as np
from random import choices


def pre_match():
    col_list = ["player","balls_Faced","dot_prob","sing_prob","doub_prob","trip_prob","four_prob","six_prob","wkt_prob","balls_bowled","dot_conc_prob","sing_conc_prob","doub_conc_prob","trip_conc_prob","four_conc_prob","six_conc_prob","wkt_conc_prob"]
    BATTING_COLS = ["Player","Owner","Innings", "Not Outs","Orange Cap","Balls Faced","Highest","50","100", "6s" , "4s"]
    BOWLING_COLS = ["Player","Owner","Innings","Balls","Dots","Runs conceeded","Purple Cap","Best Figures","4fer","5fer"]

    user_name = input("Host id:")
    source_dict = {'1':'C:\\Users\\rahul\\Desktop\\4vs4simulator\\'
                ,'2':'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\'
                ,'3':'C:\\Users\\Ganesh\\Desktop\\4vs4simulator\\'
                ,'4':'C:\\Users\\biddu\\Desktop\\4vs4simulator\\'
                ,'5':'C:\\Users\\Aditya\\Desktop\\4vs4simulator\\'
                ,'7':'C:\\Users\\Thinkpad X250\\Desktop\\4vs4simulator\\'
                ,'8':'C:\\Users\\xyz\\Desktop\\4vs4simulator\\'
                 }


    if str(user_name) != '6':
        path = source_dict[user_name] + 'Teams\\grand_master_sheet.csv'
        path1 = source_dict[user_name] + 'Teams\\Player_Mapping.csv'
        Player1 = source_dict[user_name] + 'Teams\\Data_for_simulation - Player1.csv'
        Player2 = source_dict[user_name] + 'Teams\\Data_for_simulation - Player2.csv'
        Batting_stats = source_dict[user_name] + 'Stats\\Bat_in_code.csv'
        Bowling_stats = source_dict[user_name] + 'Stats\\Bowl_in_code.csv'
        first = source_dict[user_name] + 'Stats\\first_innings.csv'
        second = source_dict[user_name] + 'Stats\\second_innings.csv'
    elif str(user_name) == '6':
        path = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Teams/Master_data_sheet.csv'
        path1 = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Teams/Player_Mapping.csv'
        Player1 = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Teams/Data_for_simulation - Player1.csv'
        Player2 = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Teams/Data_for_simulation - Player2.csv'
        Batting_stats = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Stats/Bat_in_code.csv'
        Bowling_stats = '/Users/dineshkotnani/Downloads/4vs4simulator-master/Stats/Bowl_in_code.csv'

   
    rrr=pd.read_csv(path,dtype = str)
# rrr1=rrr

    bat_stat = pd.read_csv(Batting_stats)
    bowl_stat = pd.read_csv(Bowling_stats)

    bat_stat = bat_stat[BATTING_COLS]
    bowl_stat = bowl_stat[BOWLING_COLS]

#rrr = rrr.rename(columns={'S.NO': 'Batting_Order'})

    id_1 = input("Player1 id:")

    id_2 = input("Player2 id:")


    bb = pd.read_csv(path1,dtype=str)
    p1 = bb[bb['Player_id']==id_1]['Name']
    p2 = bb[bb['Player_id']==id_2]['Name']
    for row in p2:
        Player2_Name = row

    for row in p1:
        Player1_Name = row



    print('Player 1: ' + Player1_Name)
    print('Player 2: ' + Player2_Name)


    result1 = rrr[rrr['Present_league'] == id_1]
    result2 = rrr[rrr['Present_league'] == id_2]


    bowl_stat_rem = bowl_stat[(bowl_stat['Owner'] != Player2_Name) & (bowl_stat['Owner'] != Player1_Name)]

    bat_stat_rem = bat_stat[(bat_stat['Owner'] != Player2_Name) & (bat_stat['Owner'] != Player1_Name)]


    result1 = result1[col_list]
    result2 = result2[col_list]


    result1.to_csv(Player1,index=False)

    result2.to_csv(Player2,index=False)

    return [bat_stat_rem,bowl_stat_rem,Player1_Name,Player2_Name,bat_stat,bowl_stat,Player1,Player2,Batting_stats,Bowling_stats,first,second]


def toss(p1,p2):
    results=[p1,p2]
    weights=[0.5,0.5]
    return choices(results,weights=weights)[0]
