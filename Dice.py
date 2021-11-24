'''  Roll the dice, return d1 and d2, check if the dice are the same
'''
from random import randint
from statistics import mean as mean
from statistics import median as median
from statistics import mode as mode

def roll(n = 6):
    n = n
    return {"d1":randint(1,n),"d2":randint(1,n)}


class Dice:

    def __init__(self, n=6):
        self.sides = int(n)

    def roll(self, n = 6):
        n = n
        self.dict = {"d1":randint(1,n),"d2":randint(1,n)}
        return self.dict

    def check_hard_ways(self):
        if self.dict["d1"] == self.dict["d2"]:
            return self.dict["d1"], self.dict["d2"]

    def check_n(self, n=6):
        n = n
        if self.dict["d1"] + self.dict["d2"] == n:
            return self.dict["d1"], self.dict["d2"]

    def check_seven(self):
        if self.dict["d1"] + self.dict["d2"] == 7:
            return self.dict["d1"], self.dict["d2"], self.dict["d1"] + self.dict["d2"]

    def check_hard_or_7(self):
        self.hard_ways()
        self.check_seven()

    def roll_n_times(self, n = 7):
        n = n
        i =0
        hard_ways_list = []
        while i <= n:
            a = check_hard_ways(self.throw_dice())
            if a is not None:
                hard_ways_list.append(a)
            i +=1
        return hard_ways_list

    def roll_100(self, n =100):
        ''' average player rolls 5 times, returns a list of the averages of hardways for 100 players rolling 5 times '''
        i = 0
        l = []
        while i < n:
            a =self.roll_n_times()
            if a is not None:
                l.append(len(a))
            i+=1
        return l

def stats(data):
    return mean(data), median(data), mode(data)

def main():
    hard = []
    seven = []
    i =0
    while i < 100:
        dice = Dice()
        r = dice.roll()
        if dice.check_hard_ways() is not None:
            hard.append(r)
        elif dice.check_seven() is not None:
            seven.append(r)
        i +=1
    print({"seven":seven, "hard":hard})

if __name__ == '__main__':
    main()
