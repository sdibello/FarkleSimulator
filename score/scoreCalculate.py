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
    
    # find straights first
    if  detect_straight(rolls): 
        return Scores.STRAIGHT
    #detect sets   
    repeatScore = count_repeats(rolls)
    score = add_score(repeatScore, score)
    # count 1, and 5's.
    score = add_score(score, count_singles(rolls))

    return score


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
                print(scored_dice)
                print(remaining_dice)
                return dicescore
            elif seen[y] == 4:
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                print(scored_dice)
                print(remaining_dice)
                return Scores.THREE_ONES * 2
            else:
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                scored_dice.append(remaining_dice.pop(remaining_dice.index(1)))
                print(scored_dice)
                print(remaining_dice)
                return ((Scores.THREE_ONES*2)*2)

        if seen[y] == 3:
            return y*100
        if seen[y] == 4:
            return (y*100)*2
        if seen[y] == 5:
            return ((y*100)*2)*2
    return 0

def count_singles(rolls):
    fives = rolls.count(5)
    ones = rolls.count(1)    
    return (fives * Scores.FIVE) + (ones * Scores.ONE) 

# detect a 1,2,3,4,5 or a 2,3,4,5,6
def detect_straight(rolls):
    #there can be no straight if there are duplicates.
    seen = set()
    uniq = [x for x in rolls if x not in seen and not seen.add(x)]        
    if (len(seen) != 5):
        return False

    #find gaps in a sequence. if there are gaps, then there is no sequence
    findMissing = [x for x in range(rolls[0], rolls[-1]+1)  if x not in rolls]
    if (len(findMissing) > 0):
        return False

    return True