'''Create a player object with methods to bet and interact with the dealer and tables at the casino.
'''
class Player:
    def __init__(self):
        self.name = None
        self.money = None
        self.slogan = None
        self.players = []
    def prompt_player(self):
        name = input("What's your name?: ")
        self.name = name

        money = int(input("How much money do you have?: "))

        self.money = int(money)
        slogan = input("What would you shout if you won $1,000,000.00?!: ")
        self.slogan = slogan
        print(F'We created {self.name} with ${self.money}.00 in their pocket. "{self.slogan}"')

    def funds(self):
        print(f"PLAYER: {self.name} has MONEY:{self.money}")

    def say_slogan(self):
        print(self.slogan)

    def profit(self, profit=0):
        return profit



def main():
    player = Player()
    player.prompt_player()

if __name__ == "__main__":
    main()
