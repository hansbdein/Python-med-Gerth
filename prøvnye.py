# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:41:23 2021

@author: Hans
"""
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 18:05:46 2021

@author: Hans
"""
from copy import deepcopy
import random

class Card():
    
    #Create the instance variables suit and value
    def __init__(self, value, suit):                          
        self.value = value
        self.suit = suit
        
    #print card names with special cases for cards with unique names in prügl   
    def __str__(self):                                        
        if self.value==1:
            return str(self.suit) + ' es'
        
        if self.value==11:
            if self.suit=='Spar':
                return 'Spar Mogens'
            else:
                return str(self.suit) + ' knægt'
            
        if self.value==12:
            if self.suit=='Ruder': 
                return 'Ruder Helge'
            else:
                return str(self.suit) + ' Dame'
        
        if self.value==13:
            return str(self.suit) + ' konge'   
        
        if self.value=='J': #The suit of the Joker is not shown
            return 'Joker'
        
        return str(self.suit) + ' ' + str(self.value)
    
    
    def color(self):                                    
        #all cards with suits other than hearts or diamonds will return black
        #This is important as it prevents the jokers from being given to other players
        if self.suit=='Hjerter' or self.suit=='Ruder':
            return 'r'
        return 'b'
    
class Deck():

    #Create the deck
    def __init__(self):
        self.cards = []
        self.construct()
        
    #method for populating the deck
    def construct(self):
        for s in ['Klør', 'Hjerter', 'Spar', 'Ruder']:
            for v in range(1,14):
                self.cards.append(Card(v, s))
        self.cards.extend([Card('J', None)]*4)
        
    #Function for showing the whole deck, mainly used fro troubleshooting
    def show_deck(self):
        for card in self.cards:
            print(card)
    
    #Does what it says on the tin
    def shuffle(self):
        random.shuffle(self.cards)
        
    #Probably the most simple and elegant use of the pop() function.    
    def draw(self):
        return self.cards.pop()
    
    #return the remaining number of cards
    
    def __len__(self):
        return len(self.cards)
        


def winning(L): 
    #check for win by number or sum
    if len(L)==5 or sum(L)==25:
        return True
    
    #check for win with an ace with avlue 14
    if sum(L)==12:
        if 1 in L:            
            return True
    
    #If no other statements returned anything the player does not win
    return False

#function for see how trashy a players cards, which is the average for noneempty hands
def trashscore(L):
    #make sure we dont divide by zero, and set trash score for empty hand
    if L==[]:
        return 5
    
    return sum(L)/len(L)


n=3     #number of players

#create a deck
thedeck=Deck()
#[thedeck.construct() for x in range(9)] #extension of the program to play megaprügl



limits=[]
limitwins=[]


    
totalwins8=[]
heldig=[]
uheldig=[]

for spil in range(100000):  
    
    if not (spil+1)%5000:
        print(str((spil+1)//1000)+'%')
    
    #create a list of hands
    Gamestate=[[] for x in range(n)] 
    
    #create a new deck
    L=deepcopy(thedeck)
    #shuffle the deck
    L.shuffle()
    
    turns=len(L)
    
    #creates a list of wins for each player
    wins=[0]*n
    

    #Loop that plays the game
    for turn in range(turns):
        player=turn%n  
        
        #draw a card
        card=L.draw()
        
    
        #check for Mogens and Helge
        if (card.value==11 and card.suit=='Spar' 
        or card.value==12 and card.suit=='Ruder'):        
            
            wins[player]+=1
            continue
        
        #check for jokers
        if card.value=='J':
            Gamestate[player]=[]
            wins[player]+=1
            continue
        
        #check if card is black 
        if card.color()=='b':
            
            #check if the player can take the card
            if sum(Gamestate[player])+card.value<=25:
                Gamestate[player].append(card.value)
                
                #check if this card made the player win, then discard their hand
                if winning(Gamestate[player]):
                    
                    Gamestate[player]=[]
                    wins[player]+=1 
                continue 
            
            continue
        
        #If we are still in the loop, the card is red
        
        
        #See if any player needs exactly this card to win, 
        # and if true give it to them.
        
        breaker=False #bool to break out of the nested loop
        for i in range(n):
            player=(turn+i+1)%n
            
            if (sum(Gamestate[player])+card.value<=25 and 
                winning(Gamestate[player]+[card.value]) and
                len(Gamestate[player])!=4):
                
                
                Gamestate[player]=[]
                wins[player]+=1
                
                breaker=True
                break
            
        if breaker:
            continue
        
        #See if anyone can win via trash
        for i in range(n):
            player=(turn+i+1)%n
            
            if (sum(Gamestate[player])+card.value<=25 and 
                len(Gamestate[player])==4):
                
                Gamestate[player]=[]
                wins[player]+=1
                
                breaker=True
                break
            
        if breaker:
            continue     
        

        
        
        
        
        #if there were no immediate winners find the best player on which to build trash
        
        skraldidx = max([
            (-trashscore(hand), #Choose whoever has lowest trash score
             len(hand),         #if tie occurs who has most cards
             (idx-player)%n,    #Pick player who has to wait longest for their next turn
             idx) for (idx,hand) in enumerate(Gamestate)])[3]
        
        '''
        #give aces to people with no cards if the trash can win by other means
        if (card.value==1 
            and sum(Gamestate[skraldidx])>11 
            and sum(Gamestate[skraldidx]) not in [sum(Gamestate[i])  for i in range(n) if i!=skraldidx]
            ):
            
            for i in range(n):
                player=(turn-i-1)%n
                
                if sum(Gamestate[player])==0:
                    Gamestate[player].append(card.value)
                    
                    breaker=True
                    break
        
        if breaker:
            continue        
        '''
        #uden 633 637 625 632 633 634 635 633 633 640 12.63357 and 12.635648 (1M games)
        #med simpel  12.6245 (1M games)
        #med komplex ES bestemmelse 12.634352 and 12.631878 (1M games)
        
        
        

        #Give the player the card, if the player would still be a good trash.
        if trashscore(Gamestate[skraldidx]+[card.value])<=5 and card.value<10:
            Gamestate[skraldidx].append(card.value)
    
            continue
        
        
        #Make a list of all players who can take the card, and are not designated trash
        validplayers = [x for x in range(n) 
                        if sum(Gamestate[x])+card.value<25 and x!=skraldidx ]
        
        
        #sort valid player by hand size
        validplayers=sorted(validplayers, key=lambda x: sum(Gamestate[x]))
        
        
        #make a list of players who would have a good hand after recieving the card
        goodplayers=[]
        for i in validplayers:
            
            #Check if giving the player the card would put them in a state, 
            #where the only need one additional card to win
            #If they have an ace they can already win with one card
            if (sum(Gamestate[i])+card.value>=10 
                and sum(Gamestate[i])<11
                and 1 not in Gamestate[i]):
                
                goodplayers.append(i)
                Gamestate[i].append(card.value)
                
                sums=[sum(x) for x in Gamestate]
                
                #check if two players have the same hand sum, and if so, 
                #remove the card and try the next player
                if len(sums) != len(set(sums)):
                    
                    Gamestate[i]=Gamestate[i][:-1]
                    continue
                
                breaker=True
                break

              
        if breaker:
            continue

            
        #if all good players would result in a duplicate
        if goodplayers:
            Gamestate[goodplayers[0]].append(card.value)
            continue
    
    
        #if there were no player who would have a good hand after getting the card
        if validplayers:
            Gamestate[validplayers[0]].append(card.value)
            continue
                
        
        #if No one else could take the card, give it to the designated trash
        if sum(Gamestate[skraldidx])+card.value<=25:
            Gamestate[skraldidx].append(card.value)
            continue
    
    
    
    
    
    
    '''
    totalwins7.append(wins[0])
    totalwins7.append(wins[1])
    totalwins7.append(wins[2])
    '''
    totalwins8.append(max(wins))

len(totalwins8)
len([x for x in totalwins8 if x>6])
len([x for x in totalwins8 if x>6])/len(totalwins8)

    #heldig.append(max(wins))
    #uheldig.append(min(wins))
        
'''
import matplotlib.pyplot as plt
plt.figure()
plt.plot(limits,limitwins)
'''

#print(sum(heldig)/len(heldig))
#print(sum(uheldig)/len(uheldig))

