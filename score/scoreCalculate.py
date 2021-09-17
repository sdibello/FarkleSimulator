import collections
from .scoreSet import scoreSet

class Scores:
    THREE_ONES = 1000
    STRAIGHT = 1500
    ONE = 100
    FIVE = 50

# straight
# count sets
# count 1, and 5's.
def calcScore(rolls):
    score = 0
    scored_dice = []
    remaining_dice = rolls
    
    # find straights first
    if  detect_straight(rolls):
        scored_dice = rolls
        remaining_dice = [] 
        return Scores.STRAIGHT, scored_dice, remaining_dice
    #detect sets   
    repeatScore, scored_dice, remaining_dice  = count_repeats(rolls)
    score = add_score(repeatScore, score)
    # count 1, and 5's.
    if (len(remaining_dice) > 0):
        singlescore, singles_scored, remaining_dice = count_singles(remaining_dice) 
        score = add_score(singlescore, score)
        for d in singles_scored:
            scored_dice.append(d)

    return score, scored_dice, remaining_dice

def add_score(existing, new):
    if (new>0):
        return existing+new
    else:
        return existing

#detect 3 3s, or 3 4s.
def count_repeats(rolls):
    seen = {}
    dupes = []
    scored_dice = []
    points = 0
    remaining_dice = rolls

    #find dupes, and how many times it's seen.
    for x in rolls:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] += 1
    
    for y in dupes:
        # Do Processing for 1s, cause they are different then other numbers.
        if y == 1:
            if seen[y] == 3:
                dicescore = Scores.THREE_ONES
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                points = dicescore
            elif seen[y] == 4:
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                points = Scores.THREE_ONES * 2
            elif seen[y] == 5: 
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                points = ((Scores.THREE_ONES*2)*2)
        else:
            if seen[y] == 3:
                scored_dice.append(remaining_dice.pop(remaining_dice.index(y)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(y)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(y)))
                points = y*100
            elif seen[y] == 4:
                scored_dice.append(remaining_dice.pop(remaining_dice.index(y)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(y)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(y)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(y)))
                points = (y*100)*2
            elif seen[y] == 5:
                scored_dice.append(remaining_dice.pop(remaining_dice.index(y)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(y)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(y)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(y)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(y)))
                points = ((y*100)*2)*2

    return points, scored_dice, remaining_dice 

def count_singles(rolls):
    points = 0
    fives = rolls.count(5)
    ones = rolls.count(1)
    scored_dice = []
    remaining_dice = rolls

    for x in range(0, fives):
        scored_dice.append(5)
        remaining_dice.remove(5)
        points = points + Scores.FIVE

    for x in range(0, ones):
        scored_dice.append(1)
        remaining_dice.remove(1)
        points = points + Scores.ONE

    return points, scored_dice, remaining_dice

# detect a 1,2,3,4,5 or a 2,3,4,5,6
def detect_straight(rolls):
    #there can be no straight if there are duplicates.
    seen = set()
    uniq = [x for x in rolls if x not in seen and not seen.add(x)]        
    if (len(seen) != 5):
        return False

    result = all(elem in rolls for elem in [2,3,4,5,6])
    if result == False:
        result = all(elem in rolls for elem in [1,2,3,4,5])
    
    return result