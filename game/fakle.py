
class FarkleGame:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.players = 0
        self.winning_score = 10000
        steve = object(name = 'Steve', handlimit = '350', order=1, BigFatFarkle=0, Farkle=0, open=False)
        paul = object(name = 'Pual', handlinit = '500', order=2, BigFatFarkle=0, Farkle=0, open=False)
        jerry = object(name = 'Jerry', handlinit = '250', order=2, BigFatFarkle=0, Farkle=0, open=False)
        self.players = []
        self.players.append(steve, paul)

