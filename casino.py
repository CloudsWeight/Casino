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
    # intro to Casino
    #casino.intro()
    # create the dice for CRAPS
    dice = Dice()

    # create the Dealer
    dealer = Dealer()
    dealer.name = 'Bob'
    print(f"{dealer.name} will be working at {casino.name} tonight")

    # create the players at the table
    craps = Craps(dealer)
    craps.roll()
    #craps.player_prompt()
    players = [Player(50,'Larry')]
    rolls = []
    db = {}

    print(f"{players[0].name} gets the dice first")

    number = int(input("What's the number to bet on?: "))

    bet = int(input("How much are you betting?: "))

    point_win = False

    print("Come out roll commence!")
    bet_win = craps.hard_way(bet)
    bet = players[0].bet(bet, number)
    if bet[1] == craps.roll and craps.hard == True:
        Dealer.pay(players[0], bet_win)
    print(players[0].money)

    #dealer.collect_bet()
#    print(players[0].money, dealer.money)


if __name__ == '__main__':
    main()
