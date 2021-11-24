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
        self.d1 = self.roll["d1"]
        self.d2 = self.roll["d2"]
        self.total = self.d1 + self.d2
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
    n = int(input("How many rolls to simulate?: "))
    r = Craps()
    i = 0
    l7 =[]
    hw =[]
    numbers_rolled = []
    while i < n:
        r.throw_dice()
        if r.total == 7:
            l7.append(("SEVEN", r.d1, r.d2))
        elif r.d1 == r.d2:
            hw.append(("HARD WAYS", r.d1, r.d2))
        numbers_rolled.append(r.total)
        i+=1
    for i in numbers_rolled:
        print(i)
    print(f"Out of {n} rolls we had {len(hw)} hard ways rolls and {len(l7)} seven rolls")
if __name__ == "__main__":
    main()
