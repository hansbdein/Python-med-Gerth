'''
    SAFE DISTANCE

    Your task is to write a function safe_distance(target, vectors), where
    target is a point/tuple (x, y) and vectors is a list of distinct vectors,
    each a tuple (x, y).  The function should return the smallest Euclidean
    distance from target to a point in the plane that is a sum of a subset
    of the vectors. 

    For target = (9, 10) and vectors = [(2, -5), (3, 4), (7, 3)],
    the point closest to target is (10, 7) = (3, 4) + (7, 3) with
    distance sqrt((9 - 10) ** 2 + (10 - 7) ** 2) = sqrt(10) = 3.162.

    Input:  A single line with a Python tuple (target, vectors).
            target is an integer tuple (x, y), with -100 <= x <= 100
            and -100 <= y <= 100, and vectors is a list of distinct
            integer tuples (x, y), with len(vectors) <= 50 and 
            -10 <= x <= 10 and -10 <= y <= 10.

    Ouput:  Distance from target to a closest point in the plane that
            is the sum of a subset of vectors.  The distance should be
            printed with 3 decimals.

    Example:

       Input:  ((9, 10), [(2, -5), (3, 4), (7, 3)])
 
       Output: 3.162

    Note: The below code already handles the input and output.
'''






#This solution very slow for large number of vectors, since it calculates the distance for all subsets
#I cant think of a better way to solve this, which is guranteed to find the correct solution
#I have a few ideas, but there are edge cases where they break down.
#Some of these solutions are at the end of this document.
#Works as long as there is less than 23 vectors, 
#runtime is ridiculous after that, since it scales with n!

def safe_distance(target, vectors):
    L=(dist(target,[sum(x for x,y in sett),sum(y for x,y in sett)])for sett in subsets(vectors))
        
    return min(L)


def dist(l,L):
    return ( (L[0]-l[0])**2 + (L[1]-l[1])**2 )**0.5



#function from assigment 8.2
def subsets(l,index=0):
    if len(l)>index:
        
        return subsets(l,index+1) + subsets(l[0:index]+l[index+1:],index)
    else: return [l]
'''

'''

target, vectors = eval(input())
distance = safe_distance(target, vectors)
print('%.3f' % distance)



'''                 


def safe_distance(target, vectors):
    board=[['.']*100 for x in range(100)]
    
    def search(x,y,moves):
        
        board[y][x]='x'
        
        for move in moves:
            dx,dy=move
            
            try:
                if board[y+dy][x+dx]=='.' and moves:
                    print([vec for vec in moves if vec!=move])
                    search(x+dx,y+dy,[vec for vec in vectors if vec!=move]) 
                    
            except IndexError:
                pass
            
    search(0,0,vectors) 
    
    L=[]
    
    for i in range(100):
        for j in range(100):
            if board[j][i]=='x':
                L.append(dist(target,(j,i)))
            
        
    return min(L)
    
def dist(l,L):
    return ( (L[0]-l[0])**2 + (L[1]-l[1])**2 )**0.5



print(safe_distance((9, 10), [(2, -5), (3, 4), (7, 3)]))




#print(safe_distance((78, 150), [(-4, 7), (6, 5), (7, 7), (-10, -9), (0, -7), (9, 5), (-7, -4), (-2, -8), (7, -1), (7, 1), (4, -6), (-1, 8), (-5, 0), (-6, -2), (4, 6),(9, 3), (1, -5), (7, -7), (-9, 9), (2, 6), (7, -4)]))

# (4, -7), (4, -4), (-10, 9), (-1, 10), (5, -3), (-5, -4), (4, 5), (-6, 6), (-3, -4), (-5, 5), (0, -2), (0, -1), (9, 4), (8, 8), (-7, -2), (1, 8), (-8, 9), (-7, 10), (-2, 6), (5, -7), (4, 7), (-6, 2), (4, 4), (0, -9), 

def dist(l,L):
    return ( (L[0]-l[0])**2 + (L[1]-l[1])**2 )**0.5


beenthere=set()

def safe_distance(target, vectors):
    
    
    def traverse(vecs,start):
        if vecs:
            for vector in vecs:
        
                if addvec(start,vector) not in beenthere:
                    beenthere.add(addvec(start,vector))
                return traverse(vecs.discard(vector),addvec(start,vector))
        
        
    traverse(set(vectors))
def addvec(L,l):
    return ((L[0]+l[0]),(L[1]+l[1]))
                               
'''           