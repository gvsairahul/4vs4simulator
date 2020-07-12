from random import choices
import math

def correlate(a,b,c):
    final_prob = [0,0,0,0,0,0,0]
    if c[0]>0:
        for i in range(0,7):
            final_prob[i] = a[i]+b[i]+c[i+1]
    else : 
        for i in range(0,7):
            final_prob[i] = a[i]+b[i]
            
    return final_prob 