'''Create a player object with methods to bet and interact with the dealer and tables at the casino.
'''
from random import randint

class Player:
    def __init__(self):
        self.name = None
        self.money = 0.0
        self.slogan = None

    def create_new_player(self):
        name = input("What's your name?: ")
        self.name = name
        money = int(input("How much money do you have?: "))
        self.money = money
        slogan = input("What would you shout if you won $1,000,000.00?!: ")
        self.slogan = slogan
        print(F'We created {self.name} with ${self.money}.00 in their pocket. "{self.slogan}"')
        ans = input("Do you want to create a new player?").upper()
        if ans == "Y":
            self.create_new_player()
        else:
            print("0k.")
            return

    def bet_sum(self, num=0):
        self.bet = num
        self.money = self.money - num
        return self.bet

    def play_for_player(self):
        ans = input("Do you want to play for a player? [Y] or [N]: ")
        if ans.upper() != "Y":
            return "N"
        else:
            for i in self.players:
                print(i.name)
                print("Which player do you want to play for?")

    def say_slogan(self):
        print(self.slogan)

    def profit(self, profit=0):
        return profit

def main():
    player = Player()


if __name__ == "__main__":
    main()
