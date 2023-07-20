import math
n = int(input())
L = list(map(int,input().split()))
L.sort()

lcm = math.lcm(*L)
if L[-1] == lcm:
    print(lcm * L[0])
else:
    print(lcm)

#min(L) * max(L)