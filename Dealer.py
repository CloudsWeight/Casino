'''
Dealer class

'''
from randos import names
from random import randint

names = names

def random_dealer_name():
    n = randint(0, (len(names)-1))
    return names[n]

def make_random_dealer():
    dealer = Dealer()
    dealer.name = random_dealer_name()
    return dealer

class Dealer:

    def __init__(self):
        self.money = 1000000
        self.name = None

    def set_token(self, token):
        return token

    def collect_bet(self, amount=0):
        self.money = self.money + amount
        return amount

    #def ask_bet(self):

    def passline_win(self, bet):
        bet = int(bet)
        return bet * 2

    def hard_way(self, bet):
        bet = int(bet)
        return 30 * bet

    def pay(self, win):
        self.money - win
        return win

def main():
    dealer = Dealer()
    print(dealer.name)

if __name__ == "__main__":
    main()
