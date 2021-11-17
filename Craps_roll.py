from Dice import Dice

class Call_roll():

    def __init__(self, roll, hard = False):
        self.roll = roll
        self.hard = hard
        if self.hard == True:
            self.hard_announce()
        else:
            pass

    def number_of_rolls(self, rolls = 0):
        if rolls == 0:
            num = int(input("How many rolls to simulate?  [Use num pad]: "))

        i = 0
        while i < num:
            dice = Dice()
            print(dice.a, dice.b, dice.roll)
            if dice.hard == 1:
                print("Hard ways roll!")
            i +=1

    def hard_announce(self):
        return "The hard way!"


    #    return self.x
