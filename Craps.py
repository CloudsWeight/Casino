from Dice import Dice
from Player import Player
from Dealer import Dealer
from Bets import Bets
import randos

class Craps:
    ''' '''
    def __init__(self):
        self.roll = {}
        self.players = randos.make_ten_players()
        self.point = False

    def list_players(self):
        players = []
        for i in self.players:
            players.append({"name":i.name, "money":i.money})
        return players

    def automate_players(self):


    def throw_dice(self):
        self.roll = Dice().roll()
        self.d1 = self.roll["d1"]
        self.d2 = self.roll["d2"]
        self.total = self.d1 + self.d2
        if self.d1 == self.d2:
            self.hard == True
        else:
            self.hard = False
        return self.total

    def roll_for_point(self):
        if self.point == False:
            self.throw_dice()
            return (f"{self.total, self.d1 self.d2} Hard ways is (self.hard}"")


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
    print("Here are the current players at the table")
    for i in craps.players:
        print(f"{i.name} has ${i.money}.00")

if __name__ == "__main__":
    main()
