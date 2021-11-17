'''Bet.py

'''
class Bet:

    def __init__(self, bet, odds):
        self.odds = odds
        self.bet = bet
        self.win = 0

    def win(self):
        self.win = self.odds * self.bet
    def lose(self):
        return None

def main():
    bet = Bet()
    #print(bet.attr)

if __name__ == "__main__":
    main()
