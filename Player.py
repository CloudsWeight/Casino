'''Create a player object with methods to bet and interact with the dealer and tables at the casino.
'''
class Player:
    def __init__(self,money=20, name='Earl', slogan="Get bread", token=False):
        super().__init__()
        self.money = money
        self.slogan = slogan
        self.name = name
        self.token =token
        self.hw_num = 0
        self.bet = 0
        self.pass_line = None
        self.pass_line_bet = 0

    def attr(self):
        return {'money':self.money,'name':self.name, 'slogan':self.slogan, 'token':self.token}

    def pass_bet(self):
        bet = int(input("How much are you betting?: "))
        self.pass_line_bet = bet
        self.money -self.pass_line_bet
        return self.pass_line_bet

    def ask_bet(self, bet =0):
        if bet == 0:
            bet = int(input("How much are you betting?: "))
            self.bet = bet
            self.money - self.bet
        else:
            self.bet = bet
            self.money - self.bet
        return self.bet

    def funds(self):
        print(f"PLAYER: {self.name} has MONEY:{self.money}")

    def funds_prompt(self):
        number = int(input("How much money does this player have?: "))
        self.money = number

    def announce_player(self):
        if self.token == True:
            return self.slogan, self.slogan

    def profit(self, profit=0):
        return self.money + profit

    def bet(self, bet, number):
        self.money = self.money - bet
        self.number = number
        return bet

    def tell_bet(self):
        return str(self.bet)

    def prompt(self):
        name = str(input("\nWhat is the name of this player?: "))
        self.name = name
        i = 0
        while i == 0:
            try:
                money = int(input("How much money do they have?: "))
                self.money = money
                i =1
            except:
                print("Must be an integer.")
        slogan = str(input("What do they shout at the table?"))
        self.slogan = slogan
        print(F'We created {self.name} with {self.money} in their pocket. {self.slogan}')
'''
# AI Randomness,,,
    def randomness(self):
        if __name__ == "__main__":
            from casino import casino as casino
            player = Player()
'''





def main():
    player = Player().prompt()

if __name__ == "__main__":
    main()
