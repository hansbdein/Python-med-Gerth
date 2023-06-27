"""
HANDIN 2 (palindrome)

This handin is done by:

    201706079 Hans Brüner Dein

Reflection upon solution:

    
Initially I used the string.ascii_letters package from the previous handin to 
make a list of strings based on ascii letters, but since i wanted 
capital letters first i just defined my own string. It can only create 56 labels,
but that should be plenty for this assignment. 

For part b I made a for loop where I just deleted the chosen items to avoid double counting. 
I found this easier than checking if a number had already been selected. 
The downside is that this would be difficult to implement using list comprehension.

for c I first made a for-loop as a test, then i made a much simpler function 
using list comprehension. And the I made an even simpler function.

For d I basically replicated my function from c, except I removed the if statement
and made the second variable be selected from pairs(B)


e was triviel
"""



from random import randint

letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def generate_labels(n):return[ letters[i] for i in range(n)]

def permute(L):
    Lp=[]
    for i in range(len(L)):
        rn=randint(0,len(L)-1)
        Lp.append(L[rn])
        del L[rn]
    return Lp

def pairs(L):return [ (a, b) for a in L for b in L if a<b]
    
def canonical_triplets(A, B):return[(a, b) for a in A for b in pairs(B)]

def anchored_triplets(L, R):return canonical_triplets(L, R)+canonical_triplets(R, L)


    
    


#def pairs(L):
#    Lp=[]
#    for i in range(len(L)-1):
#        for j in range(i+1,len(L)):
#            Lp.append((L[i],L[j]))
#    return Lp













