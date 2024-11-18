import sys
input = sys.stdin.readline
from collections import deque

n,g = map(int,input().split())
cows = [[] for _ in range(n+1)]
groups = [set() for _ in range(g+1)]

for group in range(1,g+1):
    L = set(map(int,input().split()[1:]))
    for cow in L:
        cows[cow].append(group)
    groups[group] = L.copy()

toInvite = deque([1])
invited = [0] * (n+1)

while toInvite:
    cow = toInvite.popleft()

    if invited[cow] == 1:
        continue

    invited[cow] = 1

    for i in cows[cow]:
        if cow in groups[i]:
            groups[i].remove(cow)
        if len(groups[i]) == 1:
            last = groups[i].pop()
            toInvite.append(last)

print(sum(invited))