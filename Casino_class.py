from Craps import Craps as craps

class Casino:

    def __init__(self, name):
        self.name = str(name.upper())
        self.craps = craps

    def intro(self):
        intro = print(f"\n################################################\n"\
        f"WELCOME TO THE {self.name} CASINO!\n" \
        "************************************************\n" \
        f"We get to have a ruckus of a good time  by creating custom players and" \
        f" deciding how they'll react at the table! \n" \
        f"Have fun, make up custom players with RanD0m Sl0gans!\n" \
        f"################################################\n" \
        f"*********************************************************************")
        pass

    def decide_game(self):
        return self.craps()

def main():
    casino = Casino("Cupertino")
    casino.intro()


if __name__ == "__main__":
    main()
