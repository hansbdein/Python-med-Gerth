# -*- coding: utf-8 -*-
"""
HANDIN 5 (eight queens puzzle)

This handin is done by:

    201706079 Hans Brüner Dein

Reflection upon solution:

Først indså jeg at der kun er et sæt af rækker, som løser problemet,
eftersom der kun kan være en dronning pr søjle og række.
Ved at indsætte denne begrænsning behøver jeg kun at tjekke om der var mere end 
en dronning på hver diagonal. Først lavede jeg en liste af de forskellige rækker.
Kort efter indså jeg at jeg kun behøvede at gemmen positionen af dronningen frem 
for hele rækken. Da der findes n! forskellige permutationer af disse lister, 
valgte jeg en tilfældig permutation frem for at køre i gennem dem alle, da jeg
ved der altid er mindst en løsning for n>3 og at der faktisk også er langt mere 
end en for store n. Jeg tjekker også positioner uden for brættet, det var 
nemmere end at beragte alle diagonaler som havende længde 10. Hvilket selvfælgelig 
fordobler køretiden, men dette er ligemeget, da køretiden alligevel eksplodere 
omkring n=16, da algorytmen skalere med n^2*n! divideret med antal løsninger, 
som jeg fandt frem til skalere med cirka 7^n, så alt i alt n!*n^2/7^n. 
Dette er selvfølgelig langt bedre en at gå igennem alle konfigurationer, 
som er n^2!/(n^2-n)!, hvilket for n>>1 er n^2n. 
Tror måske det er muligt at reducere køretiden med en faktor n, men uanset hvad,
er det n! som myrder min køretid, hvilket som sagt stadig er umådelig meget bedre end n^2n
Løsningen i hintet ligner noget (n^2)^(n+1)/n^7, 
så min kode er bedre end Gerth's med tilstrækkeligt stort n.
Jeg har brugt for lang tid på det her.
    
"""


from  random import shuffle


        

def valid(positions):
    n=len(positions)        #således at funtionen ikke er bundet til nogle eksterne variabler
    for i in range(n):          #kører gennem søjlerne
        dia=[0]*4                  #lav en tom liste til fundne dronniger
        
        for j in range(n):          #kører gennem rækkerne i og tjekker diagonaler fra top og bund
            if positions[j]==j+i:
                dia[0]+=1           #tjekker efter dronniger på venstre diagonal fra toppen
            if positions[j]==i-j:
                dia[1]+=1           #tjekker efter dronniger på højre diagonal fra toppen
            if positions[n-j-1]==j+i:
                dia[2]+=1           #tjekker efter dronniger på venstre diagonal fra bunden
            if positions[n-j-1]==i-j:
                dia[3]+=1           #tjekker efter dronniger på højre diagonal fra bunden
        
        if any(x>1 for x in dia):   #tjekker om 2 dronninger blev fundet på en diagonal
            return False
        
    return True    #true, hvis ingen dobbelte dronninger blev fundet på nogle af diagonalerne




n = int(input("Size of board: "))

positions=list(range(n)) #lav en liste af dronninge-positioner

if n<4:     
    print('no solutions')   #undgår den uendelige søgning, for n<4
else:
    
    while not valid(positions):       #løkken der tjekker tilfældige konfigurationer indtil den finder en gyldig
        shuffle(positions)



print('\n'.join(['.'*i+'Q'+'.'*(n-1-i) for i in positions])) #print et bræt baseret på de gyldige dronninge-positioner



"""

Kode der prøver at finde en approximativ scalafaktor for antal løsninger.
Tænkte jeg ville vedlægge det

"""
import matplotlib.pyplot as plt

from math import log
#antal løsninger til problemet
L=[1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596,2279184,14772512,95815104,666090624,4968057848,39029188884,314666222712,2691008701644,24233937684440,227514171973736,2207893435808352,22317699616364044,234907967154122528]



#print([log(x) for x in L[3:]])
y=[log(x) for x in L[3:]]
#y=[x/5**i for i,x in enumerate(L) ]

plt.plot(range(len(y)),y)

y2=list(map(lambda x: 2*x-3,range(len(y))))

plt.plot(range(len(y2)),y2)


plt.ylabel('log(number of solutions)')
plt.xlabel('size of board')







