'''Python Casino
Description:  A fun casino game where you create
 a table of craps players with custom slogans.
  Roll the dice, interact with players, spend money!
  Play until you reach $0 or make it to the penthouse suite!

Authors:  CSULB cohort 10 with some customizations by CkoudsWeight

License:  Github the Unlicense
'''
import json
from random import randint
from Dice import Dice
from Craps import Craps
from Craps_roll import Call_roll as roll
from Player import Player
from Casino_class import Casino as Casino
from Generate_player import Generate_player as create_player
from Dealer import Dealer

def main():
    #create the Casino
    casino_name = "Test Palace"
    casino = Casino(casino_name)

    # create the Dealer
    dealer = Dealer()
    dealer.name = 'Bob'
    print(f"{dealer.name} will be working at {casino.name} tonight")
    # create the players at the table
    craps = Craps(dealer)
    #craps.player_prompt()
    players = [Player(50,'Larry')]
    rolls = []
    db = {}
    Larry = players[0] # easier to remember for test

    ans = input("Do you want to play? [Y/N]: ")
    ans = ans.upper()
    print(ans)
    while ans == 'Y':
        # Loop game
        # number = int(input("What's the number to bet on?: "))
        # bet = int(input("How much are you betting?: "))
        #come_bet = int(input("How much on the pass line?"))
        # create craps point
        craps.roll()

        print(craps.roll, craps.d1, craps.d2, craps.hard)

        # craps.hard is boolean
        # True = hard ways / False = not hard ways
        bet = int(input("How much to bet on the pass line?: "))
        # dealer.collect_bet() method
        # collect_bet takes the number to bet on, and the amount to bet
        # number is the 'point'
        # amount is user input
        # point and craps have not happened yet
        point = False
        crappy_roll = False
        b = None
        while b == None:
            print("Select another bet below: ")
            print("[1] Hard Ways bet")
            b = 1
        if b == 1:
            print("Hard ways bet")
            number = int(input("What's the number to bet on?: "))
            hw_amount = int(input("How much are you betting?: "))
            hard_way_bet = dealer.collect_bet(number, hw_amount)
        print("Come out roll commence!")
        i = 0
        while point == False or crappy_roll == False:
            if craps.roll == 7 and i == 0:
                dealer.pay(Larry, dealer.passline_win(bet))
                print("7, winner!")
            else:
                pass
        print(type(bet_win), bet_win)
        print(players[0].money)




if __name__ == '__main__':
    main()
