import random

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["Ace", "Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
for card in cards:
    print(cards)
    break


