from collections import deque

n,s,w,g = map(int,input().split())
Card = deque()
Land = []
Price = [0]*(4*n-4)
Bought = [0]*(4*n-4)
pos = 0
money = s
donation = 0
trapped = 0
req = 0

for _ in range(g):
    action, amount = map(int,input().split())
    Card.append([action,amount])

#S:Start, D:DesertIsland, C:Contribute, T:Travel
#L:Land, G:Golden
Special = ("S","D","C","T")
for i in range(4*n-4):
    if i%(n-1) == 0:
        Land.append(Special[i//(n-1)])
        continue

    info = input().split()
    if info[0] == "G":
        Land.append("G")
    else:
        Land.append("L")
        Price[i] = int(info[1])
        req += 1

def move(dist):
    global pos
    global money

    tiles = 4*(n-1)
    a = (pos//tiles + 1) * tiles
    b = ((pos+dist) // tiles) * tiles
    money += w * ((b-a)//tiles + 1)

    pos = (pos+dist) % tiles
    action(pos)

def action(pos):
    global money
    global trapped
    global donation

    if Land[pos] == "L":
        if Bought[pos] == 0 and money >= Price[pos]:
            Bought[pos] = 1
            money -= Price[pos]

    elif Land[pos] == "G":
        action,amount = Card[0]
        Card.rotate(-1)
        if action == 1:
            money += amount

        elif action == 2:
            if money >= amount:
                money -= amount
            else:
                print("LOSE")
                exit()

        elif action == 3:
            if money >= amount:
                money -= amount
                donation += amount
            else:
                print("LOSE")
                exit()

        elif action == 4:
            move(amount)

    elif Land[pos] == "S":
        pass

    elif Land[pos] == "D":
        trapped = 3

    elif Land[pos] == "C":
        money += donation
        donation = 0

    elif Land[pos] == "T":
        move(n-1)

#Dice
rolls = int(input())
for i in range(rolls):
    a,b = map(int,input().split())
    if trapped == 0:
        move(a+b)
    else:
        if a == b:
            trapped = 0
        else:
            trapped -= 1

if req == sum(Bought):
    print("WIN")
else:
    print("LOSE")