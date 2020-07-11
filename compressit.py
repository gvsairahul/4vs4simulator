import pandas as pd 
import numpy as np

master = 'C:\\Users\\KB131141191\\Desktop\\4vs4simulator\\Stats\\grand_master_sheet.csv'
# data1 = data1[data1['actual_name'] != 'NULL']
# col = ["player","actual_name"]
# data1 = data1[col]

data = pd.read_csv(master,index_col=False)

#player,balls_Faced,dots,singles,doubles,triples,fours,sixes,wickets,dot_prob,sing_prob,doub_prob,trip_prob,four_prob,six_prob,wkt_prob,
# dots_conc,singles_conc,doubles_conc,triples_conc,fours_conc,sixes_conc,wickets_conc,balls_bowled,dot_conc_prob,sing_conc_prob,doub_conc_prob,trip_conc_prob,four_conc_prob,six_conc_prob,wkt_conc_prob

data['dot_prob']=np.where(data['balls_Faced']!=0,data['dots'].astype(float)/data['balls_Faced'].astype(float),0)
data['sing_prob']=np.where(data['balls_Faced']!=0,data['singles'].astype(float)/data['balls_Faced'].astype(float),0)
data['doub_prob']=np.where(data['balls_Faced']!=0,data['doubles'].astype(float)/data['balls_Faced'].astype(float),0)
data['trip_prob']=np.where(data['balls_Faced']!=0,data['triples'].astype(float)/data['balls_Faced'].astype(float),0)
data['four_prob']=np.where(data['balls_Faced']!=0,data['fours'].astype(float)/data['balls_Faced'].astype(float),0)
data['six_prob']=np.where(data['balls_Faced']!=0,data['sixes'].astype(float)/data['balls_Faced'].astype(float),0)
data['wkt_prob']=np.where(data['balls_Faced']!=0,data['wickets'].astype(float)/data['balls_Faced'].astype(float),0)

data['dot_conc_prob']=np.where(data['balls_bowled']!=0,data['dots_conc'].astype(float)/data['balls_bowled'].astype(float),0)
data['sing_conc_prob']=np.where(data['balls_bowled']!=0,data['singles_conc'].astype(float)/data['balls_bowled'].astype(float),0)
data['doub_conc_prob']=np.where(data['balls_bowled']!=0,data['doubles_conc'].astype(float)/data['balls_bowled'].astype(float),0)
data['trip_conc_prob']=np.where(data['balls_bowled']!=0,data['triples_conc'].astype(float)/data['balls_bowled'].astype(float),0)
data['four_conc_prob']=np.where(data['balls_bowled']!=0,data['fours_conc'].astype(float)/data['balls_bowled'].astype(float),0)
data['six_conc_prob']=np.where(data['balls_bowled']!=0,data['sixes_conc'].astype(float)/data['balls_bowled'].astype(float),0)
data['wkt_conc_prob']=np.where(data['balls_bowled']!=0,data['wickets_conc'].astype(float)/data['balls_bowled'].astype(float),0)

data.to_csv(master,index=False)