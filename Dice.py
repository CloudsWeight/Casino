'''  Dice - class
Description:  self.a = die1, self.b = die2; self.roll = roll_total
 '''
from random import randint

class Dice:

    def __init__(self, n=6):
        self.n_sides = n

    def roll(self):
        sides = self.n_sides
        self.d1 = randint(1,sides)
        self.d2 = randint(1,sides)
        self.roll = self.d1+self.d2
        if self.d1 == self.d2:
            self.hard = True
        else:
            self.hard = False
        return {'total':self.roll, 'd1':self.d1, 'd2':self.d2,'hard': self.hard}

    def hard_way(self):
        return self.roll
    def roll_100(self):
        i =0
        while i <= 100:
            dice = Dice()
            roll = dice.roll()
            if roll['hard'] == True:
                print(roll)
            i +=1

def main():
    i = 0
    while i < 35:
        dice = Dice()
        #print(dice.roll)
        #print(dice.both())
        print()
        i += 1

if __name__ == '__main__':
    main()
