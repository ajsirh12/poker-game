from poker.card import *
from poker.player import *

def main():

    card = Card()
    poker_play = player()
    deck = card.making()
    # print(deck)
    # deck.sort()
    # print(deck)
    # for i in deck:
    #     print(i[1:], end=", ")
    while 1:
        # num = int(input("시작 : 1 종료 : 0   "))
        # if num == 0:
        #     break
        cnt = int(input("플레이어 수 입력 : "))
        people = poker_play.chk_player(cnt)
        # print(deck)
        deck = card.shuffled(deck)
        # print(deck)
        card.givecard(people)
        for i in range(1, len(people)):
            print("플레이어", i, " : ", people[i])

        for i in range(5):
            print("공개 카드   : ", card.opencard(people))


if __name__ == '__main__':

    main()

