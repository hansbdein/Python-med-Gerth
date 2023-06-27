

'''

def subset_sum(x,L):
    for i in range(2**len(L)):
        subset = [L[y]for x in format(i, "0"+str(len(L))+"b") for y in range(len(L)) if int(x)]
        if sum(subset)==x: 
            return subset

#def subset(i,L):

#    return [L[y] for y, x in enumerate(format(i, "0"+str(len(L))+"b")) if int(x)]

'''

def subset_sum(x,L):
    for i in range(2**len(L)):
        subset = [L[y] for y, x in enumerate(format(i, "0"+str(len(L))+"b")) if int(x)]
        if sum(subset)==x: 
            return subset
        
print(subset_sum(120, [0, 3, 8, 11, -1,5,10,40,-23,6,-12,43,432,23]))

#def subset_sum(x,L):
    




def subsets(l,index=0):
    if len(l)>index:
        
        return subsets(l,index+1) + subsets(l[0:index]+l[index+1:],index)
    else: return [l]
    
    
def subset_sum2(x,l,index=0):   

    if len(l)>index:
        
        return subset_sum2(x,l,index+1) or subset_sum2(x,l[0:index]+l[index+1:],index)
    
    elif sum(l)==x:
        return l

    else: return False
    
    
    
def subset_sum3(x,l,index=0):   

    if sum(l)==x:
        return l
    elif len(l)>index:
        
        return subset_sum3(x,l,index+1) or subset_sum3(x,l[0:index]+l[index+1:],index)

    else: return False
    

#print(subsets([1,2,3,4]))
#def subsets(l):
        
from time import time


t=time()

subset_sum(320, [0, 3, 8, 11, -1,5,10,40,-23,6,-12,43,432,23])

tid=t-time()

print(-tid)

t=time()

subset_sum2(120, [0, 3, 8, 11, -1,5,10,40,-23,6,-12,43,432,23])

tid=t-time()

print(-tid)


t=time()

subset_sum3(320, [0, 3, 8, 11, -1,5,10,40,-23,6,-12,43,432,23])

tid=t-time()

print(-tid)

'''


True beauty

from random import randint
from time import time



def subset_sum(x,L):
    t=time()
    while t+10>time():
        subset=[L[x] for x in range(len(L)) if randint(0,1)]
        if sum(subset)==x:
            return subset
    return 'probably no solution'








  
from random import randint
from time import time
#dumt

    t=time()


def subset_dum(x,L):
    
    t=time()
    
    
    def best_method(remainder,subset):
        print('ok')
        if time()-t>10:
            return 'probably no solution'
        if subset:
            remainder-=subset.pop(randint(0,len(subset)-1))
        else: best_method(x,L)
            
        if remainder==0: return subset
            
        elif remainder<0: return best_method(x,L)
            
        else: return best_method(remainder,subset)
    
    return best_method(x,l)
    

from random import random
import  matplotlib.pyplot as plt



def random_points(n):
    return [(random(),random()) for x in range(n)]

def plot_Hull(points,polygon):
    plt.plot(*list(zip(*polygon,polygon[0])), "r-")
    plt.plot(*list(zip(*points)), "go")
    plt.show()



def convex_hull(points):
    
    start = sorted(points)[0]
    
    currentp = start
    poly = [start]
    nextp = None
    
    while nextp != start:
        for point in points:
            nextp=point
            if all(left_turn(currentp, nextp, x) for x in points):
                break
        currentp=nextp
        poly.append(nextp)
    
    return poly
    

def left_turn(p, q, r):
    return False if p==q else (q[0]-p[0]) * (r[1]-p[1]) - (r[0]-p[0]) * (q[1]-p[1]) >= 0    
 '''