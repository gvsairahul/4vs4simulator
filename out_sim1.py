from random import choices
import math



def out_calculator(balls,batsman,bowler,target,team_wickets,team_score):

    # print(batsman)
           
    
    runs_scored=batsman['runs_scored']
    average1=batsman['average']
    strikerate1 = batsman['strikerate']
    bowlers_average=bowler['average']
    runs_conceded=bowler['runs_conceded']
    wickets_taken=bowler['wickets_taken']
    economy1 = bowler['economy']
    results=["out","notout"]
    prop_bowler = bowler['prop_bowl']

    
    
    if balls>120:
        wbat  = ((5.5*strikerate1)/(100*average1))
        wbowl = (5.5*economy1)/(6*bowlers_average)
    

    elif balls<=36:
        wbat  = (2*strikerate1)/(100*average1)
        wbowl = (2*economy1)/(6*bowlers_average)
    elif balls>36 and balls<97:
        wbat  = (2.66666*strikerate1)/(100*average1)
        wbowl = (2.66666*economy1)/(6*bowlers_average)
    elif balls>96 and balls<121:
        wbat  = (4.66666*strikerate1)/(100*average1)
        wbowl = (4.66666*economy1)/(6*bowlers_average)

    if balls<121:
        if (runs_scored/average1)<1.0:
            out_batsmen=wbat*(runs_scored/average1)
        else:
            out_batsmen=wbat
        if (runs_conceded/(bowlers_average*(wickets_taken+1)))<1.0:
            out_bowler=wbowl*(runs_conceded/(bowlers_average*(wickets_taken+1)))
        else:
            out_bowler=wbowl
    
    else:
        out_batsman = wbat*(6- (132-balls)%6)*(0.222222)*135/(strikerate1)
        out_bowler = wbowl*(6- (132-balls)%6)*(0.25)*(7.75/(economy1))*(7.75/(economy1))
    
    # print(out_batsman)
    # print(out_bowler)
    if balls>102 and balls < 121 and bowler['Bowler_type'] == 'Spin':
        out_bowler = out_bowler*0.8
    elif balls > 120 and bowler['Bowler_type'] == 'Spin':
        out_bowler = out_bowler*0.85

    if prop_bowler < 16:
        out_bowler = out_bowler * math.sqrt(prop_bowler/16) * math.sqrt(math.sqrt(prop_bowler/16))
    
    if balls<121:
        rr = (2*out_batsmen + 3* out_bowler)/5
    elif balls>120 and balls<123 :
        rr = 2* min(out_batsman,out_bowler)
    else:
        rr = min(out_batsman,out_bowler)
    if balls <=36:
        rr = rr * 1.1
    elif balls>36 and balls <=66:
        rr = rr * 0.75
    elif balls>66 and balls<=108:
        rr = rr * 0.85
    elif balls>108 and balls<121:
        rr = rr * 1.1
    if(rr>=1):
        rr=0.99
    
    distribution=[rr,1-rr]


    #print(str(round(rr,2)) + ' - wicket probability\n')
    return choices(results,weights=distribution)[0]

def boundary_calculator(balls,batsman,bowler,target,team_wickets,team_score):
    runs_scored=batsman['runs_scored']
    fours_ratio = batsman['4s ratio']
    balls_bowled=bowler['balls_bowled']
    balls_faced=batsman['balls_faced']
    sixes_ratio = batsman['6s ratio']
    avg = batsman['average']
    prop_bowler = bowler['prop_bowl']
    strikerate=batsman['strikerate']/100
    runs_conceded=bowler['runs_conceded']
    out_rate = strikerate/avg
    fours_ratio = fours_ratio*(1/(1-out_rate))
    sixes_ratio = sixes_ratio*(1/(1-out_rate))
    economy = bowler['economy']
    results = ["4","6","N"]

    
    if(float(fours_ratio) == 0.0):
        fours_ratio = 0.01
    if(float(sixes_ratio == 0.0)):
        sixes_ratio = 0.005    
    if balls_faced!=0:
        present_strike_rate=runs_scored/balls_faced
    else:
        present_strike_rate=strikerate
    if balls_bowled!=0:
        present_economy=runs_conceded/balls_bowled
    else:
        present_economy=economy
    
    if balls<=36:
        if(present_strike_rate<strikerate):
            four = fours_ratio*(1.05)
            six  = sixes_ratio*(1.05)
        else:
            four = fours_ratio*(1.05)*strikerate/present_strike_rate
            six = sixes_ratio*(1.05)*(strikerate/present_strike_rate)
    
    elif balls>36 and balls<=96:
        if(present_strike_rate<strikerate):
            four = fours_ratio*(0.7)
            six  = sixes_ratio*(0.7)
        else:
            four = fours_ratio*(0.7)*strikerate/present_strike_rate
            six = sixes_ratio*(0.7)*strikerate/present_strike_rate

    elif balls>96 and balls<121:
        if(present_strike_rate<strikerate):
            four = fours_ratio*1.3
            six  = sixes_ratio*1.3
        else:
            four = fours_ratio*1.3*strikerate/present_strike_rate
            six = sixes_ratio*1.3*strikerate/present_strike_rate
    
    elif balls>120:
        four = fours_ratio * 1.5  * (strikerate/1.35)*(strikerate/1.35)*(strikerate/1.35)
        six = sixes_ratio * 1.5 * (strikerate/1.35)*(strikerate/1.35)*(strikerate/1.35)

    if balls<=36:
        if(present_economy<economy):
            four1 =  (economy/7.5)*(0.1071428)
            six1  =  (economy/7.5)*(0.05714285)
        else:
            four1 =  (economy/7.5)*(economy/present_economy)*(0.1071428)
            six1  =  (economy/7.5)*(economy/present_economy)*(0.1071428)
    
    elif balls>36 and balls<=96:
        if(present_economy<economy):
            four1 =  (economy/7.5)*(3/56)
            six1  =  (economy/7.5)*(0.0285714)
        else:
            four1 =  (economy/7.5)*(economy/present_economy)*(0.1071428)
            six1  =  (economy/7.5)*(economy/present_economy)*(0.0285714)
    
    
    elif balls>96 and balls<121:
        if(present_economy<economy):
            four1 =  (economy/7.5)*(0.1875)
            six1  =  (economy/7.5)*(0.1)
        else:
            four1 =  (economy/7.5)*(economy/present_economy)*(0.1875)
            six1  =  (economy/7.5)*(economy/present_economy)*(0.1)

    elif balls>120:
        four1 = (economy/7.75)*(economy/7.75) * (0.3) * (economy/7.75) 
        six1  = (economy/7.75)*(economy/7.75) * (0.2) * (economy/7.75)

    if balls > 90:
        four1 = four1 * math.sqrt(math.sqrt(16/prop_bowler))
        six1 = six1 * math.sqrt(math.sqrt(16/prop_bowler))
    if balls<121:
        F = (four*2 + four1*3)/5
        S = (six*2 + six1*3)/5
    elif balls>120:
        F = 0.65*max(four,four1)
        S = 0.65*max(six,six1)
    
    F=1.15*F
    S = 1.15*S
    
    if F+S>=1:
        FF = 0.99*(F/(F+S))
        SS = 0.99*(S/F+S)
        NN = 0.01
    else:
        FF=F
        SS=S
        NN=1-(F+S)     

    
    distribution = [FF,SS,NN]
    #print(str(round(FF,2)) + ' - 4 probability\n' + str(round(SS,2)) +  ' - 6 probablity\n' + str(round(NN,2)) + ' - runs or dots probability\n')
    return choices(results,weights=distribution)[0]



def runs_calculator(balls,batsman,bowler,target,team_wickets,team_score):
    runs_scored=batsman['runs_scored']
    balls_faced=batsman['balls_faced']
    strikerate=batsman['strikerate']/100
    runs_conceded=bowler['runs_conceded']
    balls_bowled=bowler['balls_bowled']
    #ratio=batsman['ratio']
    economy=bowler['economy']/6
    results=["0","1","2","3"]
    # crr = team_score*6/balls
    # if target == 1800:
    #     rrr = 9
    # else:
    #     if balls < 114:
    #         rrr = (target-team_score)/(120-balls)
     
    # if rrr>15:
    #     rrr=15
            

    if balls_faced!=0:
        present_strike_rate=runs_scored/balls_faced
    else:
        present_strike_rate=strikerate
    if balls_bowled!=0:
        present_economy=runs_conceded/balls_bowled
    else:
        present_economy=economy
    
    if balls<=36:
        if present_strike_rate>strikerate:
            dot  = 0.55
            sing = 0.28
            doub = 0.17
        else:
            dot  = 0.5
            sing = 0.35
            doub = 0.15
        if present_economy>economy:
            dot1  = 0.55
            sing1 = 0.28
            doub1 = 0.17
        else:
            dot1  = 0.5
            sing1 = 0.35
            doub1 = 0.15
    elif balls>36 and balls < 97:
        if present_strike_rate>strikerate:
            dot  = 0.3
            sing = 0.35
            doub = 0.35
        else:
            dot  = 0.25
            sing = 0.375
            doub = 0.375
        if present_economy>economy:
            dot1  = 0.3
            sing1 = 0.35
            doub1 = 0.35
        else:
            dot1  = 0.25
            sing1 = 0.375
            doub1 = 0.375
    elif balls>96 and balls < 121:
        if present_strike_rate>strikerate:
            dot  = 0.22
            sing = 0.39
            doub = 0.39
        else:
            dot  = 0.16
            sing = 0.42
            doub = 0.42
        if present_economy>economy:
            dot1  = 0.22
            sing1 = 0.39
            doub1 = 0.39
        else:
            dot1  = 0.16
            sing1 = 0.42
            doub1 = 0.42
    
    elif balls > 120:
        dot = 0.07*(1.35/strikerate)*(1.35/strikerate)*(1.35/strikerate)
        dot1 = 0.1*(1.29666666/economy)*(1.2966666/economy)*(1.2966666/economy)

        sing = 0.51*(strikerate/1.35)*(strikerate/1.35)*(strikerate/1.35)
        sing1 = 0.5*(1/((1.291666/economy)*(1.2916666/economy))) *1/((1.2966666/economy))

        doub = 0.42 *(strikerate/1.35)*(strikerate/1.35)*(strikerate/1.35)
        doub1 = 0.4*(1/((1.291666/economy)*(1.291666/economy)))*1/((1.2966666/economy))

    T = (2*dot+dot1)/3
    S = (2*sing+sing1)/3
    D = (2*doub+doub1)/3
    if balls<121:
        TT = 0.9916666*(T/(T+S+D))
        SS = 0.9916666*(S/(T+S+D))
        DD = 0.9916666*(D/(T+S+D))
    else:
        TT = 0.95*(T/(T+S+D))
        SS = 0.95*(S/(T+S+D))
        DD = 0.95*(D/(T+S+D))

    TT =1.15 * TT
    distribution = [TT,SS,DD,1-(TT+SS+DD)]

    #print(str(round(TT,2)) + ' - Dot prob \n' + str(round(SS,2)) + ' - Single prob \n' + str(round(DD,2)) + ' - Double prob \n')

    return choices(results,weights=distribution)[0]

def change_batsman(current_batsmen,current_batsmen_id):
    if current_batsmen_id==min(current_batsmen):
        current_batsmen_id=max(current_batsmen)
    else:
        current_batsmen_id=min(current_batsmen)
    return current_batsmen_id


def best_bowling(a,b,c):
    if len(a) == 7:
        if int(a[6]) > b:
            return a
        elif b > int(a[6]):
            return str(c) + ' for ' + str(b)
        else:
            if int(a[0]) <= c:
                return a
            else:
                return str(c) + ' for ' + str(b)
    elif len(a) == 8:
        if int(a[7]) > b:
            return a
        elif b > int(a[7]):
            return str(c) + ' for ' + str(b)
        else:
            if int(a[0]+a[1]) <= c:
                return a
            else:
                return str(c) + ' for ' + str(b)


def notout_cal(a,b,c):
    if b>0 and c == 'Not Out':
        return a+1
    else:
        return a

def fifty_cal(a,b):
    if b>=50 and b<100:
        return a+1
    else:
        return a
