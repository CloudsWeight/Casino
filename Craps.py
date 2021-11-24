from Dice import Dice
from Player import Player
from Dealer import Dealer
from Bets import Bets

class Craps:
    ''' '''
    def __init__(self):
        self.roll = {}

    def throw_dice(self):
        self.roll = Dice().roll()
        return self.roll

    def init_bets_dealer_and_player(self):
        bets = Bets()
        bets.player(self.player)
        bets.dealer(self.dealer)

    def payout_for_point(self):
        while  self.point == False or self.crap_roll == False:
            if self.roll == 7 and counter == 0:
                dealer.pay(self.player, self.dealer.passline_win(bet))
                print("7, winner!")
            else:
                print(self.roll)
                if self.roll == 7 and counter > 1:
                    print("Crap")

    def open_roll(self):
        self.roll_dice()
        return f"Come out roll looks like!" \
    f"  Roll: {self.roll} Dice: {self.d1, self.d2} Hard ways: {self.hard}"

    def attr(self):
        return {'total':dice.roll, 'hard':dice.hard, 'd1':dice.d1, 'd2':dice.d2}

    def roll_stats(results):
        e = {}
        c = Counter(results)
        #most_common = c.most_common(1)
        for i in c:
            e[i]=c[i]
        return e

def main():
    craps = Craps()
    i = 0
    while i < 10:
        print(craps.throw_dice())
        i+=1
if __name__ == "__main__":
    main()
