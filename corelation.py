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
    
    sum=0
    for i in range(0,7):
        sum+=final_prob[i]

    print('0' + ' - ' + str(round(final_prob[0]/sum,2))
    +str(' 1' + ' - ' + str(round(final_prob[1]/sum,2)))
    +str(' 2' + ' - ' + str(round(final_prob[2]/sum,2)))
    +str(' 3' + ' - ' + str(round(final_prob[3]/sum,2)))
    +str(' 4' + ' - ' + str(round(final_prob[4]/sum,2)))
    +str(' 6' + ' - ' + str(round(final_prob[5]/sum,2)))
    +str(' wkt' + ' - ' + str(round(final_prob[6]/sum,2))))

    return final_prob 