'''
Dealer class

'''
class Dealer:

    def __init__(self,money = 1000000, name = 'Dean',   token = True):
        self.money = money
        self.name = name
        self.token = token

    def attr(self):
        return {'money':self.money,'name':self.name, 'token':self.token}

    def set_token(self, token):
        return token

    def __repr__(self):
        return self.attr()
    def __str__(self):
        return attr()

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
    pass
    #dealer = Dealer()

if __name__ == "__main__":
    main()
