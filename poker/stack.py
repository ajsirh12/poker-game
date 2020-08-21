from random import *

class stack:

    def __init__(self):
        self.item = list()
        self.top = 0

    def get_top(self):
        return self.top

    def push(self, deck):
        self.top = 0
        self.item = list()
        for i in range(len(deck)):
            idx = randint(0, (len(deck)-i)-1)
            self.top += 1
            self.item += [deck[idx]]
            deck[idx] = deck[len(deck)-i-1]
        return self.item

    def pop(self):
        self.top -= 1
        return self.item[self.top]

# if __name__ == '__main__':
#
#     asd = stack()
#     qwe = [1,2,3,4,5]
#     print(asd.push(qwe))
