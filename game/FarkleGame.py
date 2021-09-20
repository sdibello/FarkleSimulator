from game.Player import Player

class FarkleGame:
    players = []

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.winning_score = 10000
        self.current_highscore = 0
        self.rounds = 0
        steve = Player('Steve', 300, 2, 3)
        paul = Player('Paul', 450, 2, 2)
        jerry = Player('Jerry', 250, 3, 3)
        tina = Player('Tina', 350, 3, 2)
        #steve = object(name = 'Steve', handlimit = '300', order=1, BigFatFarkle=0, Farkle=0, open=False)
        #paul = object(name = 'Paul', handlinit = '500', order=2, BigFatFarkle=0, Farkle=0, open=False)
        #jerry = object(name = 'Jerry', handlinit = '250', order=3, BigFatFarkle=0, Farkle=0, open=False)
        #ina = object(name = 'Tina', handlimit = '350', order=4, BigFatFarkle=0, Farkle=0, open=False)
        self.players.append(steve)
        self.players.append(paul)
        self.players.append(jerry)
        self.players.append(tina)

    def calc_highest_score(self):
        current_highscore = 0
        for player in self.players:
            if player.score > current_highscore:
                current_highscore = player.score
        self.current_highscore = current_highscore
        return self.current_highscore
    
    def print_scores(self):
        #creating a new list here, to maintain the order of players in the original list.
        newlist = sorted(self.players, key=lambda x: x.score, reverse=True)
        print(" ----------- Round {0} ------------- ".format(self.rounds))
        for p in newlist:
            print("{0} has {1} ".format(p.name, p.score))
        print(" ----------------------------------- ".format(self.rounds))
