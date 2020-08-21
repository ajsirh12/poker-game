class player:

    def __init__(self):
        self.player = list()

    def chk_player(self, cnt):
        self.player = list()
        for i in range(cnt+1):
            self.player += [[]]
        return self.player

    def get_player(self):
        return self.player

    def set_player(self, player):
        self.player = player

# if __name__ == '__main__':
#
#     qwe = player()
#     asd = qwe.chk_player(3)
#     print(asd)


