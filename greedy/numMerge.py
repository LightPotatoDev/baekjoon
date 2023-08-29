import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]
L.sort()

neg = []
pos = []
hasZero = False

for i in L:
    if i < 0:
        neg.append(i)
    elif i == 0:
        hasZero = True
    else:
        pos.append(i)

ans = 0
neg = neg[::-1]
while len(neg) >= 2:
    a = neg.pop()
    b = neg.pop()
    ans += a*b

while len(pos) >= 2:
    a = pos.pop()
    b = pos.pop()
    if a != 1 and b != 1:
        ans += a*b
    else:
        ans += a+b

if hasZero:
    print(ans + sum(pos))
else:
    print(ans + sum(pos) + sum(neg))