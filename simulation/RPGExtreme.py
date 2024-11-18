import sys
input = sys.stdin.readline

class Monster:
    def __init__(self, data):
        self.data = data
        self.name = data[0]
        self.atk  = int(data[1])
        self.df   = int(data[2])
        self.hp   = int(data[3])
        self.exp  = int(data[4])

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
cy,cx = 0,0 #character position
by,bx = 0,0 #boss position

L = []
Mobs  = [[0]*m for _ in range(n)]
Items = [[0]*m for _ in range(n)]
moves = []

hp     = 20
maxhp  = 20
atk    = 2
df     = 2
exp    = 0
lv     = 1
turn   = 0
weapon = 0
armor  = 0

def initialize():
    global cy,cx,by,bx,moves

    mobcount  = 0
    itemcount = 0
    for i in range(n):
        row = list(input().rstrip())
        for j,x in enumerate(row):
            if x == "@":
                cy,cx = i,j
                row[j] = "."
            if x == "M":
                by,bx = i,j
            if x == "M" or x == "&":
                mobcount += 1
            if x == "B":
                itemcount += 1
        L.append(row)

    moves = list(input().rstrip())

    for _ in range(mobcount):
        r,c,s,w,a,h,e = input().rstrip().split()
        Mobs[int(r)-1][int(c)-1] = Monster([s,w,a,h,e])

    for _ in range(itemcount):
        r,c,t,s = input().rstrip().split()
        Items[int(r)-1][int(c)-1] = Item([t,s])

def printboard():
    for i in L:
        print(''.join(i))
    print('')
    for i in Mobs:
        print(i)
    print('')
    for i in Items:
        print(i)

def gameover(result,alive):
    global hp,maxhp,atk,df,exp,lv,turn,cy,cx,weapon,armor
    if alive:
        L[cy][cx] = "@"
    printboard()
    print(f"Passed Turns : {turn}")
    print(f"LV : {lv}")
    print(f"HP : {hp}/{maxhp}")
    print(f"ATT : {atk}+{weapon}")
    print(f"DEF : {df}+{armor}")
    print(f"EXP : {exp}/{lv*5}")
    print(result)
    exit()

def levelup():
    global exp,lv,hp,atk,df
    lv += 1
    exp = 0
    maxhp += 5
    hp = maxhp
    atk += 2
    df += 2

def fight(y,x):
    global hp,atk,df,exp,weapon,armor
    mob = Mobs[y][x]

    while True:
        mob.hp -= max(1,(atk+weapon)-mob.df)
        if mob.hp <= 0:
            Mobs[y][x] = 0
            L[y][x] = "."
            cy,cx = y,x
            exp += mob.exp
            if exp >= lv*5:
                levelup()
            if [y,x] == [by,bx]:
                gameover("YOU WIN!",True)
            break
        hp -= max(1,mob.atk-(df+armor))
        if hp <= 0:
            gameover(f"YOU HAVE BEEN KILLED BY {mob.name}..",False)

Direction = {"L":[0,-1], "R":[0,1], "U":[-1,0], "D":[1,0]}
def move(dir):
    global cy,cx,hp

    dy,dx = Direction[dir]
    ny,nx = cy+dy, cx+dx

    if 0 <= ny < n and 0 <= nx < m:
        if L[ny][nx] == "." or L[ny][nx] == "^":
            cy,cx = ny,nx
        if L[ny][nx] == "&":
            fight(ny,nx)
        if L[ny][nx] == "B":
            getitem(ny,nx)

    if L[cy][cx] == "^":
        hp -= 5
        if hp <= 0:
            gameover("YOU HAVE BEEN KILLED BY SPIKE TRAP..",False)

initialize()

for i in moves:
    turn += 1
    move(i)
    if hp <= 0:
        break
gameover("Press any key to continue.",True)
