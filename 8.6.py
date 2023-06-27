"""
HANDIN 4 (triplet distance - part II)

This handin is done by:

    201706079 Hans Brüner Dein

Reflection upon solution:

Først insatte jeg koden fra forrige opgave. Hvorefter jeg til del a lavede en 
if statement, som splittede alle en liste op i to grene, og hvis grenene havde mere
end 2 elementer, forsatte rekursivt. For at løse den næste del kopierede jeg først 
collect_leaves fra forlæsningen. Og inspireret af den, lavede jeg en ligende funktion
der finder alle triplets

del c brugte jeg bare de funktioner jeg allerede havde defineret

Med den måde jeg har løst problemet, så kan jeg på 10 sekunder med min computer 
regne triplet distance for træer med 190 blade. jeg timede også funktionerne, 
som lavede træerne, for at sikre mig at det ikke var dem som var langsomme.


"""

#PREVIOUS ASSIGMENT

from random import randint
from copy import deepcopy

letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def generate_labels(n):return [letters[ i % len(letters)]*(i//len(letters)+1) for i in range(n)]


def permute(L):
    Ln=deepcopy(L)
    Lp=[]
    for i in range(len(Ln)):
        rn=randint(0,len(Ln)-1)
        Lp.append(Ln[rn])
        del Ln[rn]
    return Lp

def pairs(L):return [ (a, b) for a in L for b in L if a<b]
    
def canonical_triplets(A, B):return[(a, b) for a in A for b in pairs(B)]

def anchored_triplets(L, R):return canonical_triplets(L, R)+canonical_triplets(R, L)

#PREVIOUS ASSIGMENT
    



#a

def generate_tree(L):
    if len(L)>1:
        split=randint(1,len(L)-1)
        return (generate_tree(L[:split]),generate_tree(L[split:]))
    
    else: return L[0]
    
              
    




#b

def collect_leaves(tree, leaves=None):
    if leaves == None:
        leaves = set()
    if isinstance(tree, str):
        leaves.add(tree)
    else:
        for child in tree:
            collect_leaves(child, leaves)
    return leaves

'''
def generate_triplets(T,triplets=None):
    if triplets == None:
        triplets = set()
    for triplet in anchored_triplets(collect_leaves(T[0]), collect_leaves(T[1])):
        triplets.add(triplet)
    if len(collect_leaves(T[0]))>2:
        generate_triplets(T[0], triplets)
    if len(collect_leaves(T[1]))>2:
        generate_triplets(T[1], triplets)
    return (list(collect_leaves(T)),list(triplets))
'''

def generate_triplets(T):
    if isinstance(T, str):
        return [T], []

    left, right = T #unpack 1 step
    left_labels, left_triplets = generate_triplets(T[0])
    right_labels, right_triplets = generate_triplets(T[1])

    labels = left_labels + right_labels
    triplets = left_triplets + right_triplets
    triplets += anchored_triplets(left_labels, right_labels)

    return labels, triplets

#c

def triplet_distance(T1, T2):
    n=len(collect_leaves(T1)) 
    return n*(n-1)*(n-2)/6-len(set(generate_triplets(T1)[1]) & set(generate_triplets(T2)[1]))




#d
'''
from time import time

start = time()

trees=(generate_tree(permute(generate_labels(300))),generate_tree(permute(generate_labels(300))))

print(time() - start)

start2 = time()

triplet_distance(trees[0],trees[1])

print(time() - start2)
'''
#e
T1=((('A','F'),'B'),('D',('C','E')))   

T2=(((('D','A'),'B'),'F'),('C','E'))

T3=(('C','A'),'B')
 

def relabel(tree,new_names): 
    return tuple([relabel(x,new_names) if type(x) is tuple  
                  else new_names[x] if x in new_names.keys() else x for x in tree])  

def leaf_count(tree):
    return sum([leaf_count(x) if type(x) is tuple else 1 for x in tree]) 


def tree_size(tree):
    return max([leaf_count(tree)+tree_size(x) if type(x) is tuple else 2 for x in tree]) 


def print_ascii_tree(tree):
    
    n=tree_size(tree)+2
    
    lines=[[' ']*(2*n+1) for i in range(n)]
    
    def makebranches(branch,start):
        
        m=leaf_count(branch)

            
        for i in range(m):
            lines[start[1]+i][start[0]+i+1]='\\'
            lines[start[1]+i][start[0]-i]='/'
        
        
        if isinstance(branch[0], tuple):
            makebranches(branch[0],(start[0]-m,start[1]+m))
        else:
            lines[start[1]+m][start[0]-m-1]="'"
            lines[start[1]+m][start[0]-m]=branch[0]
            lines[start[1]+m][start[0]-m+1]="'"
            
            
        if isinstance(branch[1], tuple):
            makebranches(branch[1],(start[0]+m,start[1]+m))
        else:
            lines[start[1]+m][start[0]+m]="'"
            lines[start[1]+m][start[0]+m+1]=branch[1]
            lines[start[1]+m][start[0]+m+2]="'"
            
            
        
        
        
    makebranches(tree,[n,0])
    
    [print(''.join(line)) for line in lines]
    
            
    
print_ascii_tree(T3)   
print_ascii_tree(T2)   
print_ascii_tree(T1)   
    
    
'''
def print_ascii_tree(tree):
    
    n=tree_size(tree)+2
    
    #lines=[[' ']*2*n for i in range(n)]
    lines=[[' ' for j in range(2*n)] for i in range(n)]
    
    def makebranches(branch,start):
        if isinstance(branch, tuple):
            m=leaf_count(branch)
            #print(n)
            #print(m)
            
            for i in range(m):
                lines[start[1]+i][start[0]+i+1]='\\'
                lines[start[1]+i][start[0]-i]='/'
            
            makebranches(branch[0],(start[0]-m,start[1]+m))
            makebranches(branch[1],(start[0]+m,start[1]+m))
        else:
            lines[start[1]][start[0]]=branch
        
        
    makebranches(tree,[n,0])
    
    [print(''.join(line)) for line in lines]

'''
    

