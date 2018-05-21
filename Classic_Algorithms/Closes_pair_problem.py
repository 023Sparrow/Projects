# Closest pair problem

# unidimensional

# data
from random import random as ran
from functools import total_ordering
import math
point = []
for i in range(0,1000):
    point.append(float(100*ran()))

# Brute-force algorithm
def forcepair(data):
    if len(data) < 2:
        return None
    else:
        mindist = len(data)
        for i in range(1,len(data)-1):
            for j in range(i+1,len(data)):
                p,q = data[i],data[j]
                if abs(q-p) < mindist:
                    mindist = abs(q-p)
                    closestpair = (q,p)
        return closestpair

#print('the force algorithm answer is: {}'.format(forcepair(point)))            

# divide and conquer solution
def dividecomquer(datas):
    S = []
    datas.sort(reverse=False)
    mid = (max(datas)-min(datas))/2
    pointL = list(filter(lambda x:x<mid,datas))
    pointR = list(filter(lambda x:x>=mid,datas))
    minpairL = forcepair(pointL)
    minpairR = forcepair(pointR)
    if abs(minpairL[0]-minpairL[1])-abs(minpairR[0]-minpairR[1]) >= 0:
        minpair = minpairL
    else:
        minpair = minpairR
    mindistLR = min(abs(minpairL[0]-minpairL[1]),abs(minpairR[0]-minpairR[1]))
    for x in datas:
        if abs(x-mid) <= mindistLR/2:
                S.append(x)
    if len(S) < 2:
        pass
    else:
        minpairS = forcepair(S)
        mindistS = abs(minpairS[0]-minpairS[1])
        if mindistLR <= mindistS:
            pass
        else:
            minpair = mindpairS
    return minpair

#print('the divide and conquer solution answer is :{}'.format(dividecomquer(point)))


# 2-dimensional
class P2d():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __sub__(self,other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


