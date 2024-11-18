import sys
input = sys.stdin.readline

class Meat:
    def __init__(self,data):
        self.cost = data[0]
        self.weight = data[1]
        self.bonus = data[2]

    def __repr__(self):
        s = str(self.cost) + " " + str(self.weight) + " " + str(self.bonus)
        return s


n,m = map(int,input().split())
L = [tuple(map(int,input().split())) for _ in range(n)]
L.sort(key=lambda x:(x[1],x[0]))

meats = []
prevCost = -1
wSum = 0
curBonus = 0
for w,c in L:
    if prevCost < c:
        curBonus = wSum
    meats.append(Meat([c,w,curBonus]))
    prevCost = c
    wSum += w

ans = int(1e10)
prevCost = -1
sameCost = []

def setCost():
    global ans
    global sameCost
    w = 0
    c = 0
    if sameCost:
        w = sameCost[0].bonus
    for i in sameCost:
        w += i.weight
        c += i.cost
        if w >= m:
            ans = min(ans,c)

    sameCost = []

for meat in meats[::-1]:
    if meat.cost != prevCost:
        setCost()
    sameCost.append(meat)
    prevCost = meat.cost
setCost()

if ans == int(1e10):
    print(-1)
else:
    print(ans)