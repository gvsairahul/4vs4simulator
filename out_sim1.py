from random import choices
import math
from corelation import correlate



def result_calculator(batsman,bowler,situation,sit1) :
    # sit_prob = situation_prob(situation)
    bat_prob = batsman_prob(batsman)
    bowl_prob = bowler_prob(bowler)
    sit_prob = situation_prob(situation,sit1)
    default_sit = [0,0.3,0.4,0.05,0.002,0.12,0.07,0.058]
    

    ll = ['0','1','2','3','4','6','out']
    if sit_prob[0] == 1:

        aa = correlate(bat_prob,bowl_prob,sit_prob[1])
    else : 
        print('New Situation')
        aa = correlate(bat_prob,bowl_prob,default_sit)
    # aa = [0.1,0.1,0.1,0.1,0.1,0.1,0.1]
    # for i in range(0,7):
    #     aa[i] = bat_prob[i]*bat_prob[7]+bowl_prob[i]*bowl_prob[7]
    # s=0
    # for i in range(0,7):
    #     s+=aa[i]
    # for i in range(0,7):
    #     aa[i]/=s
    # for i in range(0,7):
    #     print(str(ll[i])+ ' - ' + str(aa[i]))
    return choices(ll,weights=aa)[0]
    


def situation_calculator(score,wickets,chase,balls,target):
    SR = score_range(score)
    ball = int(balls)

    if chase==1:
        rr  = float((target-score)*6.00/(121-ball))
    else : 
        if ball != 1:
            rr = float(score)*6.00/float(ball-1)
        else : 
            rr = 4.99
    rr_range = rate_range(rr)
    if ball%6 !=0:
        over = int(ball/6)  + 1
    else:
        over = ball/6
    return [SR,rr_range,over,wickets,chase]


def score_range(score) : 
    ss = int(score)

    if ss == 0:
        return '0 to 10'
    elif ss%10 == 0:
        return str(ss)+ ' to ' + str(ss+10)
    else : 
        return str(ss-ss%10) + ' to ' + str(ss-ss%10+ 10) 

def rate_range(rr):
    if rr<=5:
        return '0 to 5'
    elif rr >15:
        return '>15'
    elif rr >13 and rr<=15:
        return '13 to 15'
    elif rr >12 and rr<=13:
        return '12 to 13'
    elif rr >11 and rr<=12:
        return '11 to 12'
    elif rr >10 and rr<=11:
        return '10 to 11'
    elif rr >5 and rr<=6:
        return '5 to 6'
    elif rr >6 and rr<=7:
        return '6 to 7'
    elif rr >7 and rr<=7.5:
        return '7 to 7.5'
    elif rr >7.5 and rr<=8:
        return '7.5 to 8'
    elif rr >8 and rr<=8.5:
        return '8 to 8.5'
    elif rr >8.5 and rr<=9:
        return '8.5 to 9'
    elif rr >9 and rr<=9.5:
        return '9 to 9.5'
    elif rr >9.5 and rr<=10:
        return '9.5 to 10'

        
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


def out_calculator():
    return 1
def boundary_calculator():
    return 2
def runs_calculator():
    return 3

def situation_prob(attributes,sit_key):
    found=0
    l2 = [0,0,0,0,0,0,0,0]
    # [SR,rr_range,over,wickets,chase]
    if sit_key[4] == 0:
        for j in range(len(attributes)):
            # print(str(attributes[j]['score']) + ' = ' + str(sit_key[0]) + ' ?')
            # print(str(attributes[j]['rr']) + ' = ' + str(sit_key[1]) + ' ?')
            # print(str(attributes[j]['over']) + ' = ' + str(sit_key[2]) + ' ?')
            # print(str(attributes[j]['wickets']) + ' = ' + str(sit_key[3]) + ' ?')
            if attributes[j]['score'] == sit_key[0] and attributes[j]['rr'] == sit_key[1] and attributes[j]['over'] == int(sit_key[2]) and attributes[j]['wickets'] == int(sit_key[3]):
                
                found=1
                l2 = [attributes[j]['total'],attributes[j]['dot_prob'],attributes[j]['sing_prob'],attributes[j]['doub_prob'],attributes[j]['trip_prob'],attributes[j]['four_prob'],attributes[j]['six_prob'],attributes[j]['wkt_prob']]
                break
    elif sit_key[4] == 1:
        for j in range(len(attributes)):
            if attributes[j]['score'] == sit_key[0] and attributes[j]['rr'] == sit_key[1] and attributes[j]['over'] == sit_key[2] and attributes[j]['wickets'] == sit_key[3]:
                found=1
                l2 = [attributes[j]['total'],attributes[j]['dot_prob'],attributes[j]['sing_prob'],attributes[j]['doub_prob'],attributes[j]['trip_prob'],attributes[j]['four_prob'],attributes[j]['six_prob'],attributes[j]['wkt_prob']]
                break

    return [found,l2]

def batsman_prob(batsman):
    return [batsman['dot_prob'],batsman['sing_prob'],batsman['doub_prob'],batsman['trip_prob'],batsman['four_prob'],batsman['six_prob'],batsman['wkt_prob'],batsman['career_balls']]

def bowler_prob(bowler):
     return [bowler['dot_prob'],bowler['sing_prob'],bowler['doub_prob'],bowler['trip_prob'],bowler['four_prob'],bowler['six_prob'],bowler['wkt_prob'],bowler['career_balls']]        
  
