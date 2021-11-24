from random import randint, shuffle
from Player import Player



names = ['Karen', 'Mary', 'Tammy', 'Linda', 'Lori', 'Michelle', 'Michael', 'John', 'David', 'Mark', 'Richard', 'William', 'Kenneth', 'James', 'Robert']

def randomoney():
    i = 0
    money = []
    l = len(names)
    while i < l:
        money.append(randint(20,1000))
        i += 1
    return money, names

def randodict(money, names):
    random_players = []
    random = randomoney()
    i = 0
    for v in random[0]:
        random_players.append((v,names[i]))
        i +=1
    return random_players

def create_rando_players():
    players = []
    r = randomoney()
    v = randodict(r[0],r[1])
    for i in v:
        player = Player()
        player.name = i[1]
        player.money = i[0]
        players.append(player)
    return players

def main():
    r = create_rando_players()
    for v in r:
        print(v.name, v.money)

if __name__ == "__main__":
    main()
