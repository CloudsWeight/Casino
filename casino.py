'''Python Casino
Description:  A fun casino game where you create
 a table of craps players with custom slogans.
  Roll the dice, interact with players, spend money!
  Play until you reach $0 or make it to the penthouse suite!

Authors:  CSULB cohort 10 with some customizations by CkoudsWeight

License:  Github the Unlicense
'''
#import json
from random import randint
from Dice import Dice
from Craps import Craps
from Craps_roll import Call_roll as roll
from Player import Player
from Casino_class import Casino as Casino
from Generate_player import Generate_player as create_player
from Dealer import Dealer

def main():
    casino_name = "Test Palace"
    casino = Casino(casino_name)
    dealer = Dealer()
    dealer.name = 'Bob'
    print(f"{dealer.name} will be working at {casino.name} tonight")
    # create the players at the table
    craps = Craps(dealer)
    #craps.player_prompt()
    players = [Player(100,'test_player')]
    test_player = players[0] # easier to remember for test
    craps.main_loop()

    def random(self, player):
        player = player

if __name__ == '__main__':
    main()
