# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:28:35 2021

@author: Hans
"""
def memoize(f):
    answers = {}
    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    return wrapper


def change_greedy(value, coins):
    L=[]
    remaincoins=sorted(coins)[::-1]
    while value:
        
        
        for coin in remaincoins:
            
            if coin<=value:
                
                L.append(coin)
                value-=coin
                break
            else: remaincoins=remaincoins[1:]
        
            
    return L

def change_greedy_alt(value, coins):
    L=[]

    for coin in sorted(coins)[::-1]:
        while coin<=value:
            L.append(coin)
            value-=coin
        
    return L

@memoize
def number_of_coins(value, coins):
    if value==0:
        return 0
    else: 
        return min(1+number_of_coins(value-coin,coins) for coin in coins if coin<=value )
    


@memoize
def change(value, coins):
    if value==0:
        return []
    else: 
        
        return min(([coin]+change(value-coin,coins) for coin in coins if coin<=value),key=len)


'''

def change_iterative(value, coins):
    solutions = [[]]*(value+1)
    for i in range(1,value+1):
        solutions[i]=min([solutions[i-coin]+[coin] for coin in coins if coin<=i],key=len)        
    return solutions[-1]

'''

def change_iterative(value, coins):
  assert value >= 0,'Function only valid for positive payments'
  solutions = {}
  maximum=max(coins)
  for subvalue in range(value+1):
    if subvalue == 0:
      solutions[subvalue] = []
    else: 
      solutions[subvalue] = min([[coin] + solutions[subvalue-coin] for coin in coins if coin <= subvalue],key=len)
      
    if subvalue > maximum:
        solutions[subvalue-maximum]=None
    
  return solutions[value]






print(change_greedy_alt(35, (1, 7, 10)))
print(change_greedy(35, (1, 7, 10)))
print(number_of_coins(35, (1, 7, 10) ))
print(change(35, (1, 7, 10) ))
print(change_iterative(35, (1, 7, 10) ))