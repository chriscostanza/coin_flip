import random
from collections import Counter

def coin_flip():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Heads'
    else:
        return 'Tails'

def flip_counter(flip,times):
    
    flip_list = []
    
    while times > 0:
        flip_list.append(flip())
        times -= 1
    
    d = Counter(flip_list)
    dict(d)
    
    for a,b in d.items():
        print(a,b)
        
    if d['Tails']>d['Heads']:
        print('\nTails wins!!')
    else:
        print('\nHeads wins!!')

def flip_ask():
    
    ask = True
    
    while ask:
    
        try:
            num = int(input("How many times would you like to flip the coin?: "))
            return num
        except:
            print("Enter a valid number!!")

# the program

game_on = True

while game_on:

    flip_num = flip_ask()

    flip_counter(coin_flip,flip_num)

    replay_ask = True

    while replay_ask:

	    replay = input("Would you like to flip again? Y/N: ")

	    if replay[0].upper() == 'Y':
	    	replay_ask = False
	    	continue
	    elif replay[0].upper() == 'N':
	    	replay_ask = False
	    	game_on = False
	    else:
	    	print('Enter a valid reply!')

