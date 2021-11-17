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

    print(f"{players[0].name} gets the dice first")

    number = int(input("What's the number to bet on?: "))

    bet = int(input("How much are you betting?: "))
    come_bet = int(input("How much on the pass line?"))
    come_bet *2
    craps.roll()
    point = craps.roll
    print(craps.roll)
    hard = craps.hard
    dealer.collect_bet(players[0].bet(come_bet,2), craps.roll)
    print("Come out roll commence!")
    i = 0
    while point == False or craps == False:
        if craps.roll == 7 and i == 0:
            dealer.pay(players[0],come_bet)
            print("7, winner!")
            craps.roll()
        else:
            craps.roll()
            print(craps.roll)
            if craps.roll == point:
                print("winner")

    bet_win = craps.hard_way(bet)
    bet = players[0].bet(bet, number)
    if players[0].number == craps.roll and craps.hard == True:
        Dealer.pay(players[0], bet_win)
    print(players[0].money)


if __name__ == '__main__':
    main()
