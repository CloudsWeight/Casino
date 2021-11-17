from Player import *
class Generate_player:

    def __init__(self, player):
        self.player = player
        self.name = player['name']



    def prompt(self):
        n = input("How many players are currently playing craps at this table? [1 - 10] : ")

    def name(self):
        name_ans = input(f"Player {i}'s name is?: ")
        return name_ans
    def money(self):
        money_ans = int(input(f"How much money does {name_ans} have? : "))
        return money_ans

    def multiple(self, n):
        n = n
        i = 0 # iterator
        players = {} # index of player objects
        while i < int(n): # user input decides player total
            # name and money prompt for Player object
             # index names into players dict for selections
             name = Player(name_ans, money_ans)
             players[i] = name
             i += 1  # .,'}avoid black hole
        names = []
        for i in players.values():
            names.append(i)
        print(names)

        return players
