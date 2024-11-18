import sys
input = sys.stdin.readline

class Character:
    def __init__(self, data):
        self.data = data
        self.hp = data[0]
        self.maxhp = data[1]
        self.atk = data[2]
        self.df = data[3]
        self.exp = data[4]
        self.lv = data[5]
        self.weapon = data[6]
        self.armor = data[7]
        self.y = data[8]
        self.x = data[9]
        self.accessory = data[10]

    def levelup(self):
        self.lv += 1
        self.exp = 0
        self.maxhp += 5
        self.hp = self.maxhp
        self.atk += 2
        self.df += 2

    def won(self,reward):
        if "EX" in self.accessory:
            reward = int(reward * 1.2)
        self.exp += reward
        if "HR" in self.accessory:
            self.hp = min(self.hp+3, self.maxhp)
        if self.exp >= self.lv*5:
            self.levelup()

    def revive(self,yi,xi):
        self.y = yi
        self.x = xi
        self.hp = self.maxhp
        self.accessory.remove("RE")

class Monster:
    def __init__(self, data):
        self.data   = data
        self.name   = data[0]
        self.atk    = int(data[1])
        self.df     = int(data[2])
        self.hp     = int(data[3])
        self.maxhp  = int(data[3])
        self.exp    = int(data[4])
        self.isBoss = data[5]

    def __repr__(self):
        return str(self.data)

class Item:
    def __init__(self, data):
        self.data = data
        self.itemtype = data[0]
        self.effect = data[1]

    def __repr__(self):
        return str(self.data)

n,m = map(int,input().split())
yi,xi = 0,0

L = []
Mobs  = [[0]*m for _ in range(n)]
Items = [[0]*m for _ in range(n)]
moves = []

char = Character([20,20,2,2,0,1,0,0,0,0,set()])
turn = 0

def initialize():
    global char,moves,yi,xi

    mobcount  = 0
    itemcount = 0
    for i in range(n):
        row = list(input().rstrip())
        for j,x in enumerate(row):
            if x == "@":
                char.y,char.x = i,j
                yi,xi = i,j
                row[j] = "."
            if x == "M":
                Mobs[i][j] = 1
            if x == "M" or x == "&":
                mobcount += 1
            if x == "B":
                itemcount += 1
        L.append(row)

    moves = list(input().rstrip())

    for _ in range(mobcount):
        r,c,s,w,a,h,e = input().rstrip().split()
        isBoss = Mobs[int(r)-1][int(c)-1] == 1
        Mobs[int(r)-1][int(c)-1] = Monster([s,w,a,h,e,isBoss])

    for _ in range(itemcount):
        r,c,t,s = input().rstrip().split()
        Items[int(r)-1][int(c)-1] = Item([t,s])

def printstats():
    global char,turn
    for i in L:
        print(''.join(i))
    print(f"Passed Turns : {turn}")
    print(f"LV : {char.lv}")
    print(f"HP : {char.hp}/{char.maxhp}")
    print(f"ATT : {char.atk}+{char.weapon}")
    print(f"DEF : {char.df}+{char.armor}")
    print(f"EXP : {char.exp}/{char.lv*5}")

def gameover(result,alive):
    global char,turn,yi,xi
    if "RE" in char.accessory and char.hp <= 0:
        char.revive(yi,xi)
        return

    if alive:
        L[char.y][char.x] = "@"
    else:
        char.hp = 0

    printstats()
    print(result)
    exit()

def getitem(y,x):
    global char
    item = Items[y][x]

    if item.itemtype == "W":
        char.weapon = int(item.effect)
    elif item.itemtype == "A":
        char.armor = int(item.effect)
    elif item.itemtype == "O" and len(char.accessory) < 4:
        char.accessory.add(item.effect)

    Items[y][x] = 0
    L[y][x] = "."
    char.y,char.x = y,x

def fight(y,x):
    global char
    mob = Mobs[y][x]
    hunt = False
    mul = 1

    if "CO" in char.accessory:
        mul = int("DX" in char.accessory) + 2

    if "HU" in char.accessory and mob.isBoss:
        char.hp = char.maxhp
        hunt = True

    while True:
        mob.hp -= max(1,(char.atk+char.weapon)*mul-mob.df)
        mul = 1
        if mob.hp <= 0:
            Mobs[y][x] = 0
            L[y][x] = "."
            char.y,char.x = y,x
            char.won(mob.exp)
            if mob.isBoss:
                gameover("YOU WIN!",True)
            break

        if hunt == False:
            char.hp -= max(1,mob.atk-(char.df+char.armor))
        hunt = False
        if char.hp <= 0:
            mob.hp = mob.maxhp
            gameover(f"YOU HAVE BEEN KILLED BY {mob.name}..",False)
            break

Direction = {"L":[0,-1], "R":[0,1], "U":[-1,0], "D":[1,0]}
def move(dir):
    global char

    dy,dx = Direction[dir]
    ny,nx = char.y+dy, char.x+dx

    if 0 <= ny < n and 0 <= nx < m:
        if L[ny][nx] == "." or L[ny][nx] == "^":
            char.y,char.x = ny,nx
        if L[ny][nx] == "&" or L[ny][nx] == "M":
            fight(ny,nx)
        if L[ny][nx] == "B":
            getitem(ny,nx)

    if L[char.y][char.x] == "^":
        if "DX" in char.accessory:
            char.hp -= 1
        else:
            char.hp -= 5
        if char.hp <= 0:
            gameover("YOU HAVE BEEN KILLED BY SPIKE TRAP..",False)

initialize()

for i in moves:
    turn += 1
    move(i)

gameover("Press any key to continue.",True)
