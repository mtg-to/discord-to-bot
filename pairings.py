import random

def pair_random(players): 
    
    random.shuffle(players)
   
    pairs = [(players.pop(),players.pop()) for _ in range(len(players)//2)]
    if len(players)%2 != 0: pairs.append((players.pop(),None))
    return pairs