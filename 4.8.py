"""
HANDIN 2 (palindrome)

This handin is done by:

    201706079 Hans Brüner Dein

Reflection upon solution:

The solution was pretty simple, my main goal was for the program to require 
minimal computation for the most common case, namely no palindrome. 
If there is no palindrome the program will only compare 2 numbers for each letter
making the runtime linear, which is the best one can hope for in this case. 
This solution was my initial idea and the only issue i ran into was that the 
.txt file was saved in the wrong unicode format, but this was quicky resolved 
by reformatting the file itself. Though none of these exist in the given file,
the program can easily handle palindromes with more than 7 digits. 
The program will however give an error if the first or last seven digits are
palindromes, since this is such a rare edge case, and that i could not find a 
solution, that wouldn't sicnificantly impact runtime I have elected to leave the bug in

Updates on resubmission

For the even palindromes, I just ran the same loop again with the indices shifted.
Probably not the most elegant solution, but it works. 
For the edge case I just added a simple r<=n<len(S)-r to the while loop
to check if the indices exist before the comparison, it will perform this check 
for every index, which is inefficient, but checking for less would mean i would 
have choose a maximum length for the palindromes in edge cases, which would only 
make them more rare but not impossible.
"""


from string import ascii_letters, digits


# this section takes the text file and converts it to a lower case string
s = open('saxo.txt').read()  
S = s.lower()
S = "".join([c for c in S if c in ascii_letters or c in digits])


#list for storing lengths and placement of the palindromes
res=[]


for n in range(3,len(S)-3):     #runs though a list of all digits that could be the center of a 7 letter palindrome
    
    if S[n-1]==S[n+1]:
        r=2                         #sets and resets the variable for lenght of palindrome
        while r<=n<len(S)-r and S[n-r]==S[n+r]:       #a simple loop that progressively checks palindromes of greater length
            r+=1
            
        
            if r>3:                     #this outputs any found palindromes with seven or more letters
                res.append((n-r+1,S[n-r+1:n+r]))
            
        
    if S[n]==S[n+1]:  
        r=2                         #sets and resets the variable for lenght of palindrome
        while r-1<=n<len(S)-r and S[n-r+1]==S[n+r]:       #a simple loop that progressively checks palindromes of greater length
            r+=1
            
        
            if r>4:                     #this outputs any found palindromes with seven or more letters
                res.append((n-r+2,S[n-r+2:n+r]))
            






print('(index of palindrome start,palindrome)')
print(res)
