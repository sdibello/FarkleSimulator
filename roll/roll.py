from enum  import Enum
import random
min=1
max=6
number_of_farkle_dice=5

class die:
    def init(self):
        self.state = 0
        self.value = 0
    def roll(self):
        self.value = random.randint(min, max)
        self.state = die_status.new
        return self.value

class die_status(Enum):
    new = 0
    reRoll = 1
    keep = 2

class dice_rolls:
    rolls = []

    def init(self):
        for x in range(0,number_of_farkle_dice):
            rolls.append(die())

    def drop(self):
        for x in range(0,number_of_farkle_dice):
            if (x.state == die_status.reRoll):
                x.roll()




