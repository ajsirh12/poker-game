from poker.stack import *

class Card:

    def __init__(self):
        self.symbol = ['♠', '♥', '◆', '♣']
        self.cardnum = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cardDeck = list()
        self.shuffle = list()
        self.stk = stack()

    def making(self):
        for i in self.symbol:
            for j in self.cardnum:
                self.cardDeck += [i+j]
        return self.cardDeck

    def shuffled(self, deck):
        self.shuffle = self.stk.push(deck)

        return self.shuffle

    def givecard(self, player):
        for j in range(2):
            for i in range(1, len(player)):
                player[i] += [self.stk.pop()]
        return player

    def opencard(self, player):
        player[0] += [self.stk.pop()]
        return player[0]

# if __name__ == '__main__':
#
#     asd = Card()
#     d = asd.making()
#     zxc = player()
#     k = zxc.chk_player(3)
#
#     print(asd.shuffled(d))
#     print(k)
#     print(asd.givecard(k))
#     print(asd.opencard(k))
#     print(asd.opencard(k))
#     print(asd.opencard(k))
#     print(asd.opencard(k))
#     print(asd.opencard(k))

