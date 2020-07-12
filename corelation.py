from random import choices
import math

def correlate(a,b,c):
    final_prob = [0,0,0,0,0,0,0]
    if c[0]>0:
        print('Situation Occured ' + str(c[0]) + ' times')
        for i in range(0,7):
            
            final_prob[i] = math.sqrt(a[i]*b[i])+c[i+1]
    else : 
        for i in range(0,7):
            final_prob[i] = math.sqrt(a[i]*b[i])
    # print('0' + ' - ' + str(final_prob[0]))
    # print('1' + ' - ' + str(final_prob[1]))
    # print('2' + ' - ' + str(final_prob[2]))
    # print('3' + ' - ' + str(final_prob[3]))
    # print('4' + ' - ' + str(final_prob[4]))
    # print('6' + ' - ' + str(final_prob[5]))
    # print('wkt' + ' - ' + str(final_prob[6]))

    return final_prob 