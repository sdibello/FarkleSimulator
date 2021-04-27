import collections

# straight
# count repeats
# count 1, and 5's.
def calcScore(rolls):
    score = 0
    if (detect_straight(rolls) == True):
        print("Straights!")
        score = 1500
    else:
        print("There are no straights")
    
    find_missing(rolls)
    if (score > 0):
        return score 
    
#detect 3 3s, or 3 4s.
def count_repeats(rolls):
    return 100

def find_missing(lst):
    print([x for x in range(lst[0], lst[-1]+1) if x not in lst])
    

# detect a 1,2,3,4,5 or a 2,3,4,5,6
def detect_straight(rolls):
    #there can be no straigh if there are duplicates.
    seen = set()
    uniq = [x for x in rolls if x not in seen and not seen.add(x)]        
    if (len(seen) != 5):
        return False

    #find missing items in a sequence.
    dups = set()
    findMissing = [x for x in range(rolls[0], rolls[-1]+1)  if x not in rolls]
    if (len(findMissing) > 0):
        return False

    return True