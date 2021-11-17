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

    def collect_bet(self,bet, number):
        self.money = self.money + bet
        self.number = number
        return bet, number

    def hard_way(self, bet):
        bet = int(bet)
        return 30 * bet

    def pay(self, player, win):
        self.money - int(win )
        player.money
        return win

def main():
    pass
    #dealer = Dealer()

if __name__ == "__main__":
    main()
