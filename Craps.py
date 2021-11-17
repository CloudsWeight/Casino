from Dice import Dice
from Craps_roll import *
from Player import Player
from Craps_roll import Call_roll
from Dealer import Dealer

class Craps:
    ''' '''
    def __init__(self, Dealer, players = {}):
        self.token = True
        self.players = players
        self.dealer = Dealer
        self.attr = {'dealer': Dealer, 'players':players}
    def roll(self):
        dice = Dice()
        dice.roll()
        self.roll = dice.roll
        if dice.hard == True:
            self.hard = True
        else:
            self.hard = False
    def hard_way(self, bet):
        bet = int(bet)
        return 30 * bet

    def attr(self):
        return {'total':dice.roll, 'hard':dice.hard, 'd1':dice.d1, 'd2':dice.d2}

    def player_prompt(self):
        players = []
        n = int(input("How many players are at the table?"))
        if n < 10:
            if isinstance(n, int) == True:
                i = 0
                while i <n:
                    player = Player()
                    player.prompt()
                    players.append(player)
                    print(f"Greetings {player.name} time to lose all {player.money} of your money")
                    i +=1
            self.players = players

        def turn(self, player):
            player = player
            win = True
            lose = False
            rolls = {}
            i = 0
            if player['token'] == True:
                ans = str(input("Betting WITH or AGAINST the point?: ")).upper()
                if ans == 'WITH':
                    point = win
                else:
                    point = lose
                bet = int(input("How much are you betting on the point?[10,100,1000]: "))
                if player.money - bet >=0:
                    player.money = player.money - bet
                    bet = Bet(self.hard_way())

            def pass_line(self):
                return 1


            def roll_stats(results):
                e = {}
                c = Counter(results)
                #most_common = c.most_common(1)
                for i in c:
                    e[i]=c[i]
                return e

            def move_dice(self, player_old, player_new):
                player1 = player_old
                player1.token = False
                player2 = player_new
                plater2.token = True
                print(f"Moved dice from {player_old} to {player_new}.")

    def table(self):
        dealer = self.dealer
        players = self.players
        print(dealer.token)

    def intro(self):
        print("\n################################################\n"\
        "WELCOME TO THE CRAPS TABLE !\n" \
        "************************************************\n" \
        "Let's play craps!  Make some players. \n" \
        "Decide how they react! \n" \
        "Have fun, make up RanD0m Sl0gans!\n" \
        "  Yo! 11!  Yahtzee!  Snake Eyes!  Barnacles!  \n"
        "################################################\n\n")
        print("")
        print("                         _______")
        print("                 / / \\                \\")
        print("               // ()  \\      ()        \\")
        print("            //          \\    _______ \\")
        print("            \\         //     ()         //")
        print("              \\ ()  //         ()      //")
        print("         ____ \\//   _____   ()   //")
        print("     / \ \               \\")
        print("   / ()  \ \     ()        \\")
        print("/           \ \   _______ \\")
        print("\\          //     ()         //")
        print("  \\ ()  //         ()      //")
        print("     \\//   _____   ()  //")
        print(f"\nIT'S CRAPS TIME BABY!!!\LET'S ROLL!!")



def main():
    craps = Craps('Bill')
    craps.roll()

if __name__ == "__main__":
    main()
