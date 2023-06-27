
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
        self.drawncards = []
        
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
        
    #Probably the most simple and elegant use of the pop() function.    
    def draw(self):
        drawncard=self.cards.pop()
        self.drawncards.append(drawncard)
        return drawncard
    
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




from copy import deepcopy
n=4     #number of players

#create a deck
thedeck=Deck()
#[thedeck.construct() for x in range(9)] #extension of the program to play megaprügl

totalwins2=[]
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
                
                #check if this card made the player win
                if winning(Gamestate[player]):
                    Gamestate[player]=[]
                    wins[player]+=1 
                continue 
            
            continue
        
        #If we are still in the loop, the card is red
        
        #See if any player can win with the card, and if true let them.
        
        breaker=False #bool to break out of the nested loop
        for i in range(n):
            player=(turn+i+1)%n
            
            if (sum(Gamestate[player])+card.value<=25 and 
            winning(Gamestate[player]+[card.value])):
                
                Gamestate[player]=[]
                wins[player]+=1
                
                breaker=True
                break
            
        if breaker:
            continue
        
        #See if any player can take the card, and if true give it to them
        #Starting with the player who has to wait the longest for his next turn
        for i in range(n):
            player=(turn-i-1)%n
            
            if sum(Gamestate[player])+card.value<25:
                Gamestate[player].append(card.value)
                
                breaker=True
                break
            
        if breaker:
            continue
        
    totalwins2.append(sum(wins))
    heldig.append(max(wins))
    uheldig.append(min(wins))
        
import matplotlib.pyplot as plt
#plt.figure('gentleman')
plt.hist(totalwins2,bins=10,range=(8,18),histtype='step')

print(sum(totalwins2)/len(totalwins2))
print(sum(heldig)/len(heldig))
print(sum(uheldig)/len(uheldig))
        
