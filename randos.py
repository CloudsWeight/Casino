from random import *

from Player import Player

names = ['Karen', 'Mary', 'Tammy', 'Linda', 'Lori', 'Michelle', 'Michael', 'John', 'David', 'Mark', 'Richard', 'William', 'Kenneth', 'James', 'Robert', 'Kenneth', 'Scott', 'Jeffrey', 'Thomas', 'Joseph', 'Donald', 'Brian', 'Eric', 'Gary', 'Heather', 'Nicole', 'Amber', 'Crystal', 'April', 'Elizabeth', 'Erin', 'Rebecca', 'Rachel', 'Christine']

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
    randos = randomoney()
    i = 0
    for v in randos[0]:
        random_players.append((v,names[i]))
        i +=1
    return random_players

def create_randos():
    players = []
    r = randomoney()
    v = randodict(r[0],r[1])
    for i in v:
        player = Player()
        player.name = i[1]
        player.money = i[0]
        players.append(player)
    return players

def shuffle_randos():
    list_players = create_randos()
    shuffled_list = []
    i = 0
    n = len(list_players)
    while i < n:
        r = randint(0,(n-1))
        shuffled_list.append(list_players[r])
        i+=1
    return shuffled_list

def make_ten_players():
    list = shuffle_randos()
    n = (len(list)-1)
    list_of_ten = []
    i =0
    while i <9:
        r = randint(0,n)
        if list[r] not in list_of_ten:
            list_of_ten.append(list[r])
            i+=1
        else:
            pass

    return list_of_ten


def main():
    l = make_ten_players()
    for i in l:
        print(i.name, i.money)

if __name__ == "__main__":
    main()
