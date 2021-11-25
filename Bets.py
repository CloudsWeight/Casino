'''Bet.py

'''
class Bets:

    def __init__(self):
        self.win = 0
        self.info = {"dealer":self.dealer, "player":self.player}

    def dealer(self, dealer):
        self.dealer = dealer

    def player(self, player):
        self.player = player

    def win(self):
        self.win = self.odds * self.bet

    def lose(self):
        return None

    def pass_bet(self):
        bet = int(input("How much are you betting?: "))
        self.pass_line_bet = bet
        self.money -self.pass_line_bet
        return self.pass_line_bet

    def ask_bet(self, bet =0):
        if bet == 0:
            bet = int(input("How much are you betting?: "))
            self.bet = bet
            self.money - self.bet
        else:
            self.bet = bet
            self.money - self.bet
        return self.bet

    def bet_the_pass_line(self):
        a = input("Are you betting With" \
                        "or Against the player? [W] or [A]: ")
        if a.upper() == "W":
            a = True
        else:
            a = False
        player.pass_line = a

        print("Dealer:",self.dealer.money," Player",player.money)

        self.dealer.money = self.dealer.money + bet
        print(self.dealer.money)
        txt =self.open_roll()
        print(txt)
        print(self.dealer.money)

    def get_hard_way_num(self, player, number = 0):
        player = player
        if number == 0:
            number = int(input("What number are we betting hard ways on: 2, 4, 6, 8, 10, 12?: "))
        elif number == 2:
            player.hw_num
            print("Snake eyes!  Cheeky monkey.")
        elif number == 4:
            player.hw_num
        elif number == 6:
            player.hw_num
        elif number == 8:
            player.hw_num
        elif number == 10:
            player.hw_num
        elif number == 12:
            player.hw_num
            print("BOX CARS!")
        else:
            print("Gotta be an even number Einstein!  Try again... Please.")
            self.hard_way_num(self, player)
        bet = int(player.ask_bet())
        return player.hw_num, bet

    def hard_way(self, bet):
        bet = int(bet)
        return 30 * bet

    def select_bet(self, player):
        player = player
        b = None
        while b == None:
            print("Select from a bet below: ")
            print("**************************")
            print("[1] Hard Ways bet")
            print("We automatically select" \
            "hard ways for testing.")
            b = 1
        if b == 1:
            print("Hard ways bet")
            player.funds()
            bet = self.hard_way_num(player)
            number = bet[0]
            hw_amount = bet[1] #amount bet
            player.money = player.money - hw_amount
            self.dealer.collect_bet(number, hw_amount)




def main():
    bet = Bet()
    #print(bet.attr)

if __name__ == "__main__":
    main()
