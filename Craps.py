''''''
import time
import intro
from Dice import Dice
from Player import Player
from Dealer import Dealer, make_random_dealer
from Bets import Bets
import randos
from random import randint

class Craps:
    ''' '''
    def __init__(self):
        self.roll = {}
        self.players = randos.make_ten_players()
        self.point = False
        self.hard = None

    def ask_to_play(self):
        ans = input("Do you want to roll the dice? [Y]es or [N]o: ").upper()
        if ans == "Y":
            print("OK!  Let's roll!")
            return True
        elif ans != 'Y':
            print("Weasely wimp!")
            return False

    def list_players(self):
        for i in self.players:
            print(i.name, "has $", i.money,".00 to play")

    def throw_dice(self):
        self.roll = Dice().roll()
        self.d1 = self.roll["d1"]
        self.d2 = self.roll["d2"]
        self.total = self.d1 + self.d2
        if self.d1 == self.d2:
            self.hard == True
        else:
            self.hard = False
        return self.total

    def announce_roll(self):
        print("Throwing the dice!")
        time.sleep(1)
        self.throw_dice()
        print(self.d1,self.d2)
        print(self.total, "is the roll!")
        time.sleep(1)

    def bet_boxcars(self):
        print("Betting on the box cars!")
        time.sleep(2)
        for i in self.players:
            big_bet = round((i.money / 5),0)
            print(i.name, 'might bet', big_bet, "WATCH OUT!")
            try:
                bet_amnt = i.bet_sum(randint(5,big_bet))
                print("TRUE BET:",i.name, "is betting", bet_amnt, "to win $", 30*bet_amnt)
                if bet_amnt ==0:
                    bet_amnt = i.bet_sum(randint(5,big_bet))
                    print(i.name, "betting", bet_amnt)
                    self.dealer.collect_bet(bet_amnt)
                    i.box_cars = True
                else:
                    i.box_cars = False
            except:
                print("Not enough money")
                i.box_cars = False

    def automate_players(self):
        ans = self.ask_to_play()
        while ans == True:
            self.bet_boxcars()
            self.announce_roll()
            time.sleep(.5)
            if self.total == 12:
                for i in self.players:
                    self.payout_boxcars(i)
                self.automate_players()
            elif ans == False:
                return

    def payout_boxcars(self,player):
        if self.total == 12:
            player.money = player.money   + self.dealer.pay(player.bet*30)
            print(f"Won {player.bet *30}!")
        else:
            return "Roll again."

    def roll_for_point(self):
        if self.point == False:
            self.throw_dice()
            return f"{self.total, self.d1, self.d2} Hard ways is {self.hard}"



def main():
    craps = Craps()
    intro.intro()
    print(craps.make_dealer().name, "is the dealer.")
    craps.list_players()
    craps.automate_players()

if __name__ == "__main__":
    main()
