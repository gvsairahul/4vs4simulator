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
    out_rate_1 = average1*100/strikerate1
    out_rate_2 = bowlers_average*6/economy1
    prop_bowler = bowler['prop_bowl']

    best_batsman = batsman['average']/5.92 + batsman['strikerate']/99 + batsman['4s ratio']*4.33 + batsman['6s ratio']*4.33+4*batsman['average']/batsman['strikerate']
    

       
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
        if float(runs_scored/average1)>1.0 and float(runs_scored/average1) < 1.2:
            out_batsman=wbat*(runs_scored/average1)
        else:
            out_batsman=wbat
        if float(runs_conceded/(bowlers_average*(wickets_taken+1)))<1.0 and float(runs_conceded/(bowlers_average*(wickets_taken+1)))>0.8:
            out_bowler=wbowl*(runs_conceded/(bowlers_average*(wickets_taken+1)))
        else:
            out_bowler=wbowl
    
    elif balls>120:
        out_batsman = wbat*(6- (132-balls)%6)*(0.222222)*135/(strikerate1)
        out_bowler = wbowl*(6- (132-balls)%6)*(0.25)*(7.75/(economy1))*(7.75/(economy1))
    
    # print(out_batsman)
    # print(out_bowler)
    if batsman['balls_faced']>=35:
        out_batsman*=(batsman['balls_faced']*batsman['balls_faced']/1225)
    if balls>102 and balls < 121 and bowler['Bowler_type'] == 'Spin':
        out_bowler = out_bowler*0.8
    elif balls > 120 and bowler['Bowler_type'] == 'Spin':
        out_bowler = out_bowler*0.85
    if prop_bowler < 20.2 and balls>84:
        out_bowler/=((20.2/prop_bowler)*(20.2/prop_bowler))
    if prop_bowler<21.2 and balls >=108:
        out_bowler/=((21.2/prop_bowler)) 
    if prop_bowler < 16:
        out_bowler = out_bowler*(prop_bowler/16) * math.sqrt(math.sqrt(prop_bowler/16))
    
    out_batsman = out_batsman*(8.13/best_batsman)
    best_bowler = prop_bowler*((14/economy1) +(28/bowlers_average) + (60/(bowlers_average*economy1)))/16

    out_bowler = out_bowler * (best_bowler/5.8)
    
    rr = correlate_wkt(out_batsman,out_bowler,balls,out_rate_1,out_rate_2,prop_bowler)

    if balls <=36:
        rr = rr * 1.1
    elif balls>36 and balls <=66:
        rr = rr * 0.65
    elif balls>66 and balls<=108:
        rr = rr * 0.75
    elif balls>108 and balls<121:
        rr = rr * 1.05
    xx=batsman['runs_scored']
    if xx>70:
        rr*=(xx*xx*xx*xx/24010000)    
    if bowler['balls_bowled']<6:
        rr/=2
    if bowler['wickets_taken'] >=2:
        rr = rr*0.25*best_bowler/6.5
    if prop_bowler>22:
        rr*=(prop_bowler/22)
    if prop_bowler>22.5:
        rr*=(prop_bowler/22.5)
    if prop_bowler>23:
        rr*=(prop_bowler/23)
    if(rr>=0.58):
        rr=0.58
    if best_batsman > 8.5 and batsman['balls_faced']>out_rate_1*0.7 and batsman['balls_faced']<out_rate_1*1.3:
        rr*=(8.5/best_batsman)
    if batsman['fours']+batsman['sixes']>8:
        rr*=((batsman['fours']+batsman['sixes'])/8)
    if out_rate_1 < 16:
        if batsman['balls_faced']>15:
            rr*=(batsman['balls_faced']/15)
        if batsman['balls_faced']>=25:
            rr*=(batsman['balls_faced']*batsman['balls_faced']/625)
    if out_rate_1 < 13:
        if batsman['balls_faced']>10:
            rr*=(batsman['balls_faced']/10)
        if batsman['balls_faced']>=20:
            rr*=(batsman['balls_faced']/20)
    if batsman['runs_scored']>0 and batsman['balls_faced']>8 :
        if (float(batsman['runs_scored'])/batsman['balls_faced']) < 1.1:
            rr/=(batsman['runs_scored']/1.1*batsman['balls_faced'])
    if batsman['runs_scored']>1.3*average1:
        rr*=(batsman['runs_scored']/(1.3*average1))
        if batsman['runs_scored']>2.3*average1:
            rr*=(batsman['runs_scored']/(2.3*average1))
    rr*=(25/bowlers_average)

    if economy1 < 8 and bowler['Bowler_type'] == 'Pace':
        rr*=(math.sqrt(8/economy1) * math.sqrt(math.sqrt(8/economy1)))


    if strikerate1<105:
        rr*=2.5
    distribution=[rr*0.67,1-rr*0.67]



    # print(str(round(rr,2)) + ' - wicket probability\n')
    return choices(results,weights=distribution)[0]
    # return distribution
def boundary_calculator(balls,batsman,bowler,target,team_wickets,team_score):
    runs_scored=batsman['runs_scored']
    fours_ratio = batsman['4s ratio']
    balls_bowled=bowler['balls_bowled']
    balls_faced=batsman['balls_faced']
    sixes_ratio = batsman['6s ratio']
    avg = batsman['average']
    avg1 = bowler['average']
    prop_bowler = bowler['prop_bowl']
    strikerate=batsman['strikerate']/100
    runs_conceded=bowler['runs_conceded']
    out_rate = strikerate/avg
    fours_ratio = fours_ratio*(1/(1-out_rate))
    sixes_ratio = sixes_ratio*(1/(1-out_rate))
    economy = bowler['economy']
    results = ["4","6","N"]
    best_batsman = batsman['average']/15.92 + batsman['strikerate']/32 + batsman['4s ratio']*6.33 + batsman['6s ratio']*6.33+0.9*batsman['average']/batsman['strikerate']
    if prop_bowler < 5:
        prop_bowler = 5
    
    if(float(fours_ratio) == 0.0):
        fours_ratio = 0.01
    if(float(sixes_ratio == 0.0)):
        sixes_ratio = 0.005    
    if balls_faced!=0:
        present_strike_rate=runs_scored/balls_faced
    else:
        present_strike_rate=strikerate
    if balls_bowled!=0:
        present_economy=runs_conceded*6/balls_bowled
    else:
        present_economy=economy
    if present_economy<6:
        present_economy=6
    if balls<=36:
        if(present_strike_rate<strikerate):
            four = fours_ratio*(1.05)
            six  = sixes_ratio*(1.05)
        else:
            four = fours_ratio*(1.05)*0.9
            six = sixes_ratio*(1.05)*(0.9)
    
    elif balls>36 and balls<=96:
        if(present_strike_rate<strikerate):
            four = fours_ratio*(0.68)
            six  = sixes_ratio*(0.68)
        else:
            four = fours_ratio*(0.62)*0.9
            six = sixes_ratio*(0.58)*0.9

    elif balls>96 and balls<121:
        if(present_strike_rate<strikerate):
            four = fours_ratio*1.3
            six  = sixes_ratio*1.3
        else:
            four = fours_ratio*1.3*0.9
            six = sixes_ratio*1.3*0.9
    
    elif balls>120:
        four = fours_ratio * 1.5  * (strikerate/1.35)*(strikerate/1.35)*(strikerate/1.35)
        six = sixes_ratio * 1.5 * (strikerate/1.35)*(strikerate/1.35)*(strikerate/1.35)

    if balls < 84 and 1/out_rate < 10:
        four = four * math.sqrt(1/(10*out_rate))
        six  = six * math.sqrt(1/(10*out_rate))

    if balls<=36:
        if(present_economy<economy):
            four1 =  (economy*economy/64)*(0.1071428)
            six1  =  (economy*economy/64)*(0.05714285)
        else:
            four1 =  (economy/7.5)*(1.1)*(0.1071428)
            six1  =  (economy/7.5)*(1.1)*(0.1071428)
    
    elif balls>36 and balls<=96:
        if(present_economy<economy):
            four1 =  (economy/7.5)*(4/112)
            six1  =  (economy/7.5)*(0.031285714)
        else:
            four1 =  (economy/7.5)*(1.1)*(0.01391071428)
            six1  =  (economy/7.5)*(1.3)*(0.018285714)
    
    
    elif balls>96 and balls<121:

            four1 =  (economy/7.75)*(1.1)*(0.1875) *(economy/7.75)
            six1  =  (economy/7.75)*(1.1)*(0.1)*(economy/7.75)

    elif balls>120:
        four1 = (economy/7.75)*(economy/7.75) * (0.3) * (economy/7.75) 
        six1  = (economy/7.75)*(economy/7.75) * (0.2) * (economy/7.75)
    if balls<37 and economy < 7.8:
        four1*=(economy/7.8)
        six1*=(economy/7.8)
    if balls > 90 and prop_bowler < 16:
        four1 = four1 * math.sqrt(math.sqrt(16/prop_bowler))
        six1 = six1 * math.sqrt(math.sqrt(16/prop_bowler))
    if batsman['balls_faced']<7:
        four/=2
        six/=2
    if batsman['balls_faced']>12 and batsman['balls_faced'] <=28:
        four*=math.sqrt(batsman['balls_faced']/12)
        six*=math.sqrt(batsman['balls_faced']/12)
    if batsman['balls_faced']>30:
        four*=batsman['balls_faced']/18.95
        six*=batsman['balls_faced']/18.95
    
    if batsman['fours']>7:
        four*=(7/batsman['fours'])
    if batsman['sixes']>5:
        six*=(5/batsman['sixes'])
    if bowler['Bowler_type'] == 'Spin':
        four1/=1.3
        six1*=1.3
    else:
        four1*=1.2
        six/=1.4
    best_bowler = prop_bowler*((24/economy) +(25/avg1) + (60/(avg1*economy)))/16
    if best_bowler <0.5:
        best_bowler = 0.5
    if bowler['Bowler_type'] == 'Spin' : 
        best_bowler = best_bowler * 0.8
    if balls>36 and balls<97 and economy <11:
        four1 = four1/(3-economy/4)
        six1  = six1/(3-economy/4)
    elif balls > 36 and balls < 97 and economy >=11 : 
        four1 = 2.25*four1
        six1 = 2.25*six1
    elif balls<37 and economy <9:
        four1 = four1/math.sqrt((3-economy/3.5))
        six1 = six1/math.sqrt((3-economy/3.5))
    elif balls<37 and economy > 9:
        four1 = four1*(2.33333)
        six1 = six1 *(2)
    
    elif balls>96 :
        four1 = four1*6.1/best_bowler
        six1 =  six1*6.1/best_bowler

    if balls>36 and balls < 73 and best_bowler > 7.5:
        four/=1.5
        six/=1.23
        four1/=1.5
        six/=1.23
    else:
        four*=1.21
        six*=1.1
        four1*=1.21
        six1*=1.1
    four = four*math.sqrt(best_batsman/7)
    six = six*math.sqrt(best_batsman/7)
    if prop_bowler < 20.2 and balls>90:
        four1*=math.sqrt((20.2/prop_bowler))
        six1*=math.sqrt((20.2/prop_bowler))
    if prop_bowler<21.2 and balls >=108:
        four1*=math.sqrt((21.2/prop_bowler))
        six1*=math.sqrt((21.2/prop_bowler))    
    four*=1.29
    six*=1.29
    four1*=math.sqrt(7.5/best_bowler)
    six1*=math.sqrt(7.5/best_bowler)

    if balls>96 and economy< 7.75 and bowler['Bowler_type'] == 'Pace' :
        four1*= (economy/7.75)
        six1*= (economy/7.75)

    if balls<97:
        F = (four*2 + four1*3)/5
        S = (six*2 + six1*3)/5
    elif balls>96:
        F = (1.462*four*four1)/((four+four1))
        S = (1.462*six*six1)/((six+six1))
    elif balls>120:
        F = 0.55*max(four,four1)
        S = 0.55*max(six,six1)
    
    if balls < 90 and prop_bowler < 13 and balls_bowled > 6 :
        four1 = four1* math.sqrt(13/prop_bowler)
        six1 = six * math.sqrt(13/prop_bowler)


    F=F*math.sqrt((best_batsman/8.5) *(17/prop_bowler)*1.3627*avg/25)
    S = S*math.sqrt((best_batsman/8.5)*(17/prop_bowler)*1.3627*avg/25)
    if economy < 8 and balls < 96 and balls > 36:
        F = F*(economy/8)
        S = S*(economy/8)*(economy/8)
    if batsman['balls_faced']<6 and strikerate < 1.75 and balls<=96:
        F/=(3/strikerate)
        S/=(2/strikerate)    
    if F+S>=0.88:
        FF = 0.88*(F/(F+S))
        SS = 0.88*(S/F+S)
        NN = 0.12
    else:
        FF=F
        SS=S
        NN=1-(F+S)     

    if balls < 37:
        if FF>0.13: 
            FF=0.13
        if SS>0.1:
            SS=0.1
    elif balls < 97 and balls > 36:
        if FF>0.11:
            FF=0.11
        if SS>0.1:
            SS=0.1
    
    NN = 1-(FF+SS)
    

    distribution = [FF,SS,NN]
    # print(str(round(FF,2)) + ' - 4 probability\n' + str(round(SS,2)) +  ' - 6 probablity\n' + str(round(NN,2)) + ' - runs or dots probability\n')
    return choices(results,weights=distribution)[0]
    # return distribution



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

    T = 1.15*(2*dot+dot1)/3
    S = (2*sing+sing1)/3
    D = (2*doub+doub1)/3
    if batsman['balls_faced']<5 and balls<=96:
        T*1.25
    best_batsman = batsman['average']/15.92 + batsman['strikerate']/32 + batsman['4s ratio']*6.33 + batsman['6s ratio']*6.33+0.9*batsman['average']/batsman['strikerate']
    if batsman['balls_faced']>10:
        S=2*S
        D=1.3*D
    if bowler['balls_bowled']>6:
        if bowler['runs_conceded']/bowler['balls_bowled']>1.3:
            T/=2
            S*=1.3
            D*=1.06
        elif bowler['balls_bowled'] > 12 and bowler['runs_conceded']/bowler['balls_bowled']>1.4:
            T/=3
            S*=1.5
            
    T = T*7/best_batsman
    T = T*(economy*0.75)*(economy*0.75)*2.8
    if balls<121:
        TT = 0.9916666*(T/(T+S+D))
        SS = 0.9916666*(S/(T+S+D))
        DD = 0.9916666*(D/(T+S+D))
    else:
        TT = 0.95*(T/(T+S+D))
        SS = 0.95*(S/(T+S+D))
        DD = 0.95*(D/(T+S+D))

    if batsman['balls_faced'] > 3 and batsman['runs_scored'] <2:
        TT = 0.15
        SS=0.7
        DD = 0.143
    distribution = [TT,SS,DD,1-(TT+SS+DD)]

    # print(str(round(TT,2)) + ' - Dot prob \n' + str(round(SS,2)) + ' - Single prob \n' + str(round(DD,2)) + ' - Double prob \n')

    return choices(results,weights=distribution)[0]

    # return distribution

    # print(str(round(TT,2)) + ' - Dot prob \n' + str(round(SS,2)) + ' - Single prob \n' + str(round(DD,2)) + ' - Double prob \n')

    

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


def correlate_wkt(x,y,balls,a,b,c):
    if c<16 and c>=12 and x<y:
        return x+ y*(math.sqrt(c/12)-1)
    elif c<16 and c>=12 and x>=y:
        return y+x*(c/12 - 1)
    
    elif c<12:
        if x > math.sqrt(y):
            return 0.4*(x-math.sqrt(y))
        else:
            return 0.002
    else:
        if balls < 36:
            if a > 19:
                if b<=16:
                    return 2*x*y/(x+y)
                elif b > 16 and b < 26:
                    return 1.85*x*y/(x+y)
                else:
                    return 1.5*x*y/(x+y)
            else :
                if b<=16:
                    return 2.25*x*y/(x+y)
                elif b > 16 and b < 26:
                    return 2*x*y/(x+y)
                else :
                    return 1.75*x*y/(x+y)
        elif balls>=36 and balls < 84:
            if a > 16:
                if b<=16:
                    return 2*x*y/(x+y)
                elif b > 16 and b < 26:
                    return 1.85*x*y/(x+y)
                else:
                    return 1.5*x*y/(x+y)
            else :
                if b<=16:
                    return 2.25*x*y/(x+y)
                elif b > 16 and b < 26:
                    return 2*x*y/(x+y)
                else :
                    return 1.75*x*y/(x+y)
        else : 
            if a > 13:
                if b<=16:
                    return 2*x*y/(x+y)
                elif b > 16 and b < 26:
                    return 1.85*x*y/(x+y)
                else:
                    return 1.5*x*y/(x+y)
            else :
                if b<=16:
                    return 2.25*x*y/(x+y)
                elif b > 16 and b < 26:
                    return 2*x*y/(x+y)
                else :
                    return 1.75*x*y/(x+y)    

 