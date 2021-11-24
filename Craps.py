from Dice import Dice
from Player import Player
from Dealer import Dealer
from Bets import Bets
from randos import create_rando_players, randodict, randomoney

class Craps:
    ''' '''
    def __init__(self):
        self.roll = {}
        self.players = create_rando_players()

    def list_players(self):
        players = []
        for i in self.players:
            players.append({"name":i.name, "money":i.money})
        return players

    def select_random_players(self):
        print(len(self.players))

    def throw_dice(self):
        self.roll = Dice().roll()
        self.d1 = self.roll["d1"]
        self.d2 = self.roll["d2"]
        self.total = self.d1 + self.d2
        return self.total

    def ask_to_play(self):
        ans = input("Play craps? [Y]es or [N]o: ").upper()
        if ans == "Y":
            print("OK!")
            return True
        else:
            print("Weasely wimp!")
            return False
    #def start_turn(self):

def main():
    craps = Craps()
    print(craps.list_players())

if __name__ == "__main__":
    main()
