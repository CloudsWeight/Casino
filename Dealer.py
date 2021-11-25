'''
Dealer class

'''
from randos import names
from random import randint

names = names
def random_dealer_name():
    n = randint(0, (len(names)-1))
    return names[n]

class Dealer:

    def __init__(self):
        self.money = 1000000
        self.name = random_dealer_name()

    def set_token(self, token):
        return token

    def collect_bet(self, number, amount):
        self.money = self.money + amount
        self.number = number
        return amount, number

    #def ask_bet(self):

    def passline_win(self, bet):
        bet = int(bet)
        return bet * 2

    def hard_way(self, bet):
        bet = int(bet)
        return 30 * bet

    def pay(self, player, win):
        win = win
        self.money - win
        player.money
        return win

def main():
    dealer = Dealer()
    print(dealer.name)

if __name__ == "__main__":
    main()
