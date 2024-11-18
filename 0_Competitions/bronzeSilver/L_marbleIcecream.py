from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int,input().split()))
D = defaultdict(int)
for i in L:
    D[i] += 1

q = int(input())
for _ in range(q):
    eat = list(map(int,input().split()))[1:]
    adding = list(map(int,input().split()))[1:]
    act = True

    eatD = defaultdict(int)
    for i in eat:
        eatD[i] += 1

    for i in eatD:
        if i in D and eatD[i] <= D[i]:
            pass
        else:
            act = False

    if act:
        for i in eatD:
            D[i] -= eatD[i]
        for i in adding:
            D[i] += 1

ans = []
for i in D:
    for _ in range(D[i]):
        ans.append(i)

print(len(ans))
if len(ans) != 0:
    print(*ans)