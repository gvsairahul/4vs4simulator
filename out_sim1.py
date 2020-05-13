from random import choices
def toss():
    results=['Heads','Tails']
    weights=[0.5,0.5]
    return choices(results,weights=weights)[0]

def out_calculator(batsman,bowler):
    runs_scored=batsman['runs_scored']
    average=batsman['average']
    strikerate = batsman['strikerate']
    bowlers_average=bowler['average']
    runs_conceded=bowler['runs_conceded']
    wickets_taken=bowler['wickets_taken']
    economy = bowler['economy']
    results=["out","notout"]

    wbat = strikerate/(100*average)
    wbowl = economy/(6*bowlers_average)
    if (runs_scored/average)<1.0:
        out_batsmen=wbat*(runs_scored/average)
    else:
        out_batsmen=wbat
    if (runs_conceded/(bowlers_average*(wickets_taken+1)))<1.0:
        out_bowler=wbowl*(runs_conceded/(bowlers_average*(wickets_taken+1)))
    else:
        out_bowler=wbowl
    rr = (2*out_batsmen + 3* out_bowler)/5
    distribution=[rr,1-rr]
    return choices(results,weights=distribution)[0]

def boundary_calculator(balls,batsman,bowler):
    runs_scored=batsman['runs_scored']
    fours_ratio = batsman['4s ratio']
    sixes_ratio = batsman['6s ratio']
    strikerate=batsman['strikerate']/100
    runs_conceded=bowler['runs_conceded']
    wickets_taken=bowler['wickets_taken']
    economy = bowler['economy']
    results = ["4","6","N"]
    weights = []
    possible_cases_batsman=[]
    possible_cases_bowler=[]
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
            four = fours_ratio*(0.85714)
            six  = sixes_ratio*(0.85714)
        else:
            four = fours_ratio*(0.85714)*strikerate/present_strike_rate
            six = sixes_ratio*(0.85714)*(strikerate/present_strike_rate)
    
    elif balls>36 and balls<=96:
        if(present_strike_rate<strikerate):
            four = fours_ratio*(0.428571)
            six  = sixes_ratio*(0.428571)
        else:
            four = fours_ratio*(0.428571)*strikerate/present_strike_rate
            six = sixes_ratio*(0.428571)*strikerate/present_strike_rate

    elif balls>96 and balls<121:
        if(present_strike_rate<strikerate):
            four = fours_ratio*1.5
            six  = sixes_ratio*1.5
        else:
            four = fours_ratio*1.5*strikerate/present_strike_rate
            six = sixes_ratio*1.5*strikerate/present_strike_rate

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

    F = (four*3 + four1*2)/5
    S = (six*3 + six1*2)/5

    if F+S>=1:
        FF = 0.99*(F/(F+S))
        SS = 0.99*(S/F+S)
        NN = 0.01
    else:
        FF=FF
        SS=S
        NN=1-(F+S)     

    distribution = [FF,SS,NN]
    return choices(results,weights=distribution)[0]



def runs_calculator(balls,batsman,bowler):
    runs_scored=batsman['runs_scored']
    balls_faced=batsman['balls_faced']
    strikerate=batsman['strikerate']/100
    runs_conceded=bowler['runs_conceded']
    balls_bowled=bowler['balls_bowled']
    ratio=batsman['ratio']
    economy=bowler['economy']/6
    results=["0","1","2","3"]
    weights=[]
    
            

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
            dot  = 0.7
            sing = 0.18
            doub = 0.12
        else:
            dot  = 0.6
            sing = 0.24
            doub = 0.16
        if present_economy>economy:
            dot1  = 0.7
            sing1 = 0.18
            doub1 = 0.12
        else:
            dot1  = 0.6
            sing1 = 0.24
            doub1 = 0.16
    elif balls>36 and balls < 97:
        if present_strike_rate>strikerate:
            dot  = 0.4
            sing = 0.3
            doub = 0.3
        else:
            dot  = 0.25
            sing = 0.375
            doub = 0.375
        if present_economy>economy:
            dot1  = 0.4
            sing1 = 0.3
            doub1 = 0.3
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

    T = (dot+dot1)/2
    S = (sing+sing1)/2
    D = (doub+doub1)/2

    TT = 0.9916666*(T/(T+S+D))
    SS = 0.9916666*(S/(T+S+D))
    DD = 0.9916666*(D/(T+S+D))
    distribution = [TT,SS,DD,1-(TT+SS+DD)]

    return choices(results,weights=distribution)[0]

def change_batsman(current_batsmen,current_batsmen_id):
    if current_batsmen_id==min(current_batsmen):
        current_batsmen_id=max(current_batsmen)
    else:
        current_batsmen_id=min(current_batsmen)
    return current_batsmen_id
