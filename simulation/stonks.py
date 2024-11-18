import sys
import math
input = sys.stdin.readline

class Company:
    def __init__(self, data):
        self.group = int(data[0])
        self.name = data[1]
        self.price = int(data[2])

    def __repr__(self):
        return str([self.group,self.name,self.price])

SINGLE = 0
GROUP = 1
GROUPPERCENT = 2

def getPrice(search):
    for comp in comps:
        if comp.name == search:
            return comp.price

def changePrice(search,amount,mode):
    for comp in comps:
        if mode == SINGLE and comp.name == search:
            comp.price += amount
        if mode == GROUP and comp.group == search:
            comp.price += amount
        if mode == GROUPPERCENT and comp.group == search:
            comp.price = comp.price * (100+amount) // 100
            comp.price = comp.price//10*10

n,money,q = map(int,input().rstrip().split())
comps = []
stonks = dict()

for _ in range(n):
    g,h,p = input().rstrip().split()
    comps.append(Company([g,h,p]))
    stonks[h] = 0

for _ in range(q):
    cmd = input().rstrip().split()

    if cmd[0] == '1':
        name, num = cmd[1], int(cmd[2])
        price = getPrice(name)
        if (price*num <= money):
            money -= price*num
            stonks[name] += num

    if cmd[0] == '2':
        name, num = cmd[1], int(cmd[2])
        price = getPrice(name)
        num = min(stonks[name], num)
        money += price*num
        stonks[name] -= num

    if cmd[0] == '3':
        name, incr = cmd[1], int(cmd[2])
        changePrice(name,incr,SINGLE)

    if cmd[0] == '4':
        grup, incr = int(cmd[1]), int(cmd[2])
        changePrice(grup,incr,GROUP)

    if cmd[0] == '5':
        grup, incr = int(cmd[1]), int(cmd[2])
        changePrice(grup,incr,GROUPPERCENT)

    if cmd[0] == '6':
        print(money)

    if cmd[0] == '7':
        total = money
        for st in stonks:
            total += stonks[st] * getPrice(st)
            #print(st,stonks[st],getPrice(st))
        print(total)

#print(comps)