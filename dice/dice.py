import random

def rollDice(number_of_dice):
    items = []
    for x in range(0,5):
        rv = random.randint(1, 6)
        items.append(rv)
    return items
