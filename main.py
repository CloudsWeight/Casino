'''
The main Casino file.
'''
from Dealer import Dealer
from Player import Player
from Bets import Bet
from Craps import Craps

def main():
    craps = Craps()
    # Create the Dealer class the create the Player class
    dealer = Dealer()
    # Player(300, 'Larry', "I like to roll box cars baby!")
    Larry = Player(300, 'Larry', "I like to roll box cars baby!")
    bet = hard_way = craps.bet(dealer.collect_bet(Larry.bet(300)))
    print(hard_way, Larry.money, dealer.money)




if __name__ == "__main__":
    main()
