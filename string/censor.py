from collections import deque
from itertools import islice

bomb = list(input())
s = input()
l = len(bomb)

L = deque()
censorLeft = True
pl = 0
pr = len(s)-1
print(pl,pr)

while True:
    if pl == pr:
        break
    if censorLeft:
        L.append(s[pl])
        pl += 1
        if len(L) >= l and list(islice(L,len(L)-l,len(L))) == bomb:
            for j in range(l):
                L.pop()
            censorLeft = False
    else:
        L.appendleft(s[pr])
        pr -= 1
        if len(L) >= l and list(islice(L,0,l)) == bomb:
            for j in range(l):
                L.popleft()
            censorLeft = True


print(''.join(L))
