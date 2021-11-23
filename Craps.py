from Dice import Dice
from Player import Player
from Dealer import Dealer
from Bets import Bet

class Craps:
    ''' '''
    def __init__(self, dealer, player, players = []):
        self.token = True
        self.players = players
        self.player = player
        self.dealer = dealer
        self.attr = {'dealer': Dealer, 'player':player}

    def roll_dice(self):
        dice = Dice()
        dice.roll_dice()
        self.roll = dice.roll
        self.d1 = dice.d1
        self.d2 = dice.d2
        if dice.hard == True:
            self.hard = True
        else:
            self.hard = False
        self.hard
        return self.roll, self.d1, self.d2

    def main_loop(self):
        bet = Bet()
        bet.player(self.player)
        bet.dealer(self.dealer)
        print("entering the arena...")
        #self.intro()
        roll_db = {}
        ans = input("Do you want to play? [Y/N]: ").upper()
        while ans == 'Y':
            if self.player.money >0:
                self.point = False
                self.crap_roll = False

                bet.select_bet(self.player)
                self.roll_dice()
                i = 0
                while  self.point == False or self.crap_roll == False:
                    if self.roll == 7 and counter == 0:
                        dealer.pay(self.player, self.dealer.passline_win(bet))
                        print("7, winner!")
                    else:
                        print(self.roll)
                        if self.roll ==
                        i+1
                        pass
            counter = i
            print(self.player.money)
            ans = input("Do you want to play? [Y/N]: ")
            ans = ans.upper()
        if ans != "Y":
                print(f"{ans}???\n Really..." \
                " So you don't want to play!?  K bye")

    def open_roll(self):
        self.roll_dice()
        return f"Come out roll looks like!" \
    f"  Roll: {self.roll} Dice: {self.d1, self.d2} Hard ways: {self.hard}"

    def attr(self):
        return {'total':dice.roll, 'hard':dice.hard, 'd1':dice.d1, 'd2':dice.d2}

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
        print(f"Moved dice from {player1} to {player2}.")

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
                    print(f"Greetings {player.name}" \
                    " time to lose all {player.money} of your money")
                    i +=1
            self.player = players

    def table(self):
        dealer = self.dealer
        players = self.player
        print(dealer.token)

    def intro(self):
        print("\n################################################\n"\
        "WELCOME TO THE CRAPS TABLE !\n" \
        "************************************************\n" \
        "Let's play craps!  Make some players. \n" \
        "Decide how they react! \n" \
        "Have fun, make up RanD0m Sl0gans for each player" \
        " \nYo! 11!  Yahtzee!  Snake Eyes!  Barnacles!\n"  \
        "################################################n")
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
    dealer = Dealer(1000000,"Larry")
    test_player = Player(100, "Test Player", "Hot mic!  Hello!")
    craps = Craps(dealer, test_player)
    craps.main_loop()
if __name__ == "__main__":
    main()
