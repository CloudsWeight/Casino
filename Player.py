'''Create a player object with methods to bet and interact with the dealer and tables at the casino.

(name, money, slogan)

'''

class Player():
    def __init__(self,money=20, name='Earl', slogan="Get bread", token=False):
        super().__init__()
        self.money = money
        self.slogan = slogan
        self.name = name
        self.token =token

    def attr(self):
        return {'money':self.money,'name':self.name, 'slogan':self.slogan, 'token':self.token}

    def announce_player(self):
        if self.token == True:
            return self.slogan, self.slogan

    def profit(self, profit=0):
        return self.money + profit

    def bet(self, bet, number):
        self.money = self.money - bet
        self.number = number
        return bet

    def tell_bet(self, bet):
        return str(bet)

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
                print("Must be integer.")

        slogan = str(input("What do they shout at the table?"))
        self.slogan = slogan
        print(F'We created {self.name} with {self.money} in their pocket. {self.slogan}')


def main():
    player = Player().prompt()

if __name__ == "__main__":
    main()
