# import random

# coin = random.choice(['Heads', 'Tails'])
# print(coin)

# cards = ["jacks", "queens", "kings", "aces"]
# random.shuffle(cards)
# for card in cards:
#     print(card)
    
# number = random.randint(1,10)
# print(number)

# import statistics
# print(statistics.mean([100,90]))
# print(statistics)

import statistics
import cowsay
import sys
try:
    print("Hello my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
    sys.exit()
    
    


# import statistics 
# import sys
# print(statistics.mean([int(sys.argv[1]), int(sys.argv[2])]))