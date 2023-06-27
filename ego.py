# -*- coding: utf-8 -*-
"""
Created on Mon May 24 18:05:46 2021

@author: Hans
"""
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
        self.cards.extend([Card('J', None)]*3)
        
    #Function for showing the whole deck, mainly used fro troubleshooting
    def show_deck(self):
        for card in self.cards:
            print(card)
    
    #Does what it says on the tin
    def shuffle(self):
        random.shuffle(self.cards)
        
    #draw a card with pop(), put it among the drawn cards, and return it.   
    def draw(self):
        return self.cards.pop()
    
    #return the remaining number of cards
    
    def __len__(self):
        return len(self.cards)
        

from copy import deepcopy
n=4     #number of players

#create a deck
thedeck=Deck()
#[thedeck.construct() for x in range(9)] #extension of the program to play megaprügl

totalwins1=[]
heldig=[]
uheldig=[]


for i in range(100000):  
    
    if not i%5000:
        print(str(i//1000)+'%')
    
    #create a list of hands
    Gamestate=[[] for x in range(n)] 
    
    #shuffle the deck
    L=deepcopy(thedeck)
    L.shuffle()
    
    turns=len(L)
    
    #creates a list of wins for each palyer
    wins=[0]*n
    

    #Loop that plays the game
    for turn in range(turns):
        player=turn%n  
        
        '''
        #code for manually inputing every card
        v=input('what is the cards value? ')
        s=input('what is the cards suit? ')
        
        try: 
            v=int(v)
        except:
            1
        card=Card(v,s)
        '''
        
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
        
        #make sure the player can take the card
        if sum(Gamestate[player])+card.value<=25:
            Gamestate[player].append(card.value)
            
        #check for win by number of cards
        if len(Gamestate[player])==5:
            Gamestate[player]=[]
            wins[player]+=1
            continue
        
        #check for win by sum including an ace with value 14
        if sum(Gamestate[player])==12:
            if 1 in Gamestate[player]:            
                Gamestate[player]=[]
                wins[player]+=1
                continue
        #check for win by sum
        if sum(Gamestate[player])==25:
            Gamestate[player]=[]
            wins[player]+=1
        
    totalwins1.append(sum(wins))
    heldig.append(max(wins))
    uheldig.append(min(wins))
        
import matplotlib.pyplot as plt
#plt.figure('egoprügl')
plt.hist(totalwins1,bins=10,range=(8,18),histtype='step')

print(sum(totalwins1)/len(totalwins1))
print(sum(heldig)/len(heldig))
print(sum(uheldig)/len(uheldig))