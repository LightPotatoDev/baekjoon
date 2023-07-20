from itertools import combinations

n,m = map(int,input().split())

chickens = []
houses = []

for i in range(n):
    line = list(map(int,input().split()))
    for j,x in enumerate(line):
        if x == 1:
            houses.append([i,j])
        if x == 2:
            chickens.append([i,j])

dist = [[] for _ in range(len(houses))]

for i,x in enumerate(houses):
    for y in chickens:
        dist[i].append(abs(x[0]-y[0]) + abs(x[1]-y[1]))

comb = combinations([i for i in range(len(chickens))],m)

def makeNewdist(combi):
    newdist = [[] for _ in range(len(houses))]
    for i,x in enumerate(dist):
        for y in combi:
            newdist[i].append(x[y])
    return newdist

mindist = 10**7
for c in comb:
    newdist = makeNewdist(c)
    chickendist = 0
    for i in newdist:
        chickendist += min(i)
    mindist = min(mindist, chickendist)

print(mindist)
