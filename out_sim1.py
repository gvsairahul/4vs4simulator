from random import choices
def toss():
    results=['Heads','Tails']
    weights=[0.5,0.5]
    return choices(results,weights=weights)[0]

def out_calculator(batsman,bowler):
    runs_scored=batsman['runs_scored']
    average=batsman['average']
    bowlers_average=bowler['average']
    runs_conceded=bowler['runs_conceded']
    wickets_taken=bowler['wickets_taken']
    results=["out","notout"]
    if (runs_scored/average)<1.0:
        out_batsmen=0.1*(runs_scored/average)
    else:
        out_batsmen=0.1
    if (runs_conceded/(bowlers_average*(wickets_taken+1)))<1.0:
        out_bowler=0.1*(runs_conceded/(bowlers_average*(wickets_taken+1)))
    else:
        out_bowler=0.1
    distribution=[max(out_bowler,out_batsmen),1-max(out_bowler,out_batsmen)]
    return choices(results,weights=distribution)[0]

def runs_calculator(balls,batsman,bowler):
    runs_scored=batsman['runs_scored']
    balls_faced=batsman['balls_faced']
    strikerate=batsman['strikerate']/100
    runs_conceded=bowler['runs_conceded']
    balls_bowled=bowler['balls_bowled']
    ratio=batsman['ratio']
    economy=bowler['economy']/6
    results=[]
    weights=[]
    for i in range(7):
        if i !=5 and i!=3:
            results.append(i)
            weights.append(0.0)
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
    if present_strike_rate<strikerate:
        for i in results:
            if i>strikerate:
                possible_cases_batsman.append(i)
    else:
        for i in results:
            if i<strikerate:
                possible_cases_batsman.append(i)
    if present_economy<economy:
        for i in results:
            if i>economy:
                possible_cases_bowler.append(i)
    else:
        for i in results:
            if i<economy:
                possible_cases_bowler.append(i)
    for i in range(len(results)):
        if (results[i]==0):
            if results[i] in possible_cases_batsman:
                weights[i]+=0.5*(1/len(possible_cases_batsman))
            if results[i] in possible_cases_bowler:
                weights[i]+=0.5*(1/len(possible_cases_bowler))
        elif (results[i]<=2) and (results[i]!=0):
            if results[i] in possible_cases_batsman:
                if balls<=36 and balls>=90:
                    weights[i]+=0.1*(1/len(possible_cases_batsman))
                else:
                    weights[i]+=0.5*(1/len(possible_cases_batsman))
            if results[i] in possible_cases_bowler:
                if balls<=36 and balls>=90:
                    weights[i]+=0.1*(1/len(possible_cases_bowler))
                else:
                    weights[i]+=0.5*(1/len(possible_cases_bowler))
        elif results[i]==4:
            if results[i] in possible_cases_batsman:
                weights[3]+=0.5*(1/len(possible_cases_batsman))
            if results[i] in possible_cases_bowler:
                weights[3]+=0.5*(1/len(possible_cases_bowler))
        else:
            if results[i] in possible_cases_batsman:
                weights[4]+=(0.5*ratio*weights[3])
            if results[i] in possible_cases_bowler:
                weights[4]+=(0.5*ratio*weights[3])
    return choices(results,weights=weights)[0]

def change_batsman(current_batsmen,current_batsmen_id):
    if current_batsmen_id==min(current_batsmen):
        current_batsmen_id=max(current_batsmen)
    else:
        current_batsmen_id=min(current_batsmen)
    return current_batsmen_id
