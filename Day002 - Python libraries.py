import random
from codecs import IncrementalDecoder

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["Ace", "Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
for card in cards:
    print(cards)
    break

import statistics
print(statistics.mean([1000, 500]))

import sys
print(sys.version)
print(sys.version_info)

import cowsay
print(cowsay.__doc__)






