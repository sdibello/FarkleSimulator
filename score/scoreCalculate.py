

# straight
# count repeats
# count 1, and 5's.
def calcScore(rolls):
    score = 0
    score = detect_straight(rolls)
    if (score > 0):
        return score 
    
#detect 3 3s, or 3 4s.
def count_repeats(rolls):
    return 100

# detect a 1,2,3,4,5 or a 2,3,4,5,6
def detect_straight(rolls):
    if rolls.count(1) == 1 and rolls.count(2) == 1:
        return 1500
    return 0