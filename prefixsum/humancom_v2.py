import sys
input = sys.stdin.readline
from bisect import bisect_left

s = input().rstrip()
q = int(input())
D = dict()

for i,x in enumerate(s):
    if x not in D:
        D[x] = [i]
    else:
        D[x] += [i]

for _ in range(q):
    a,l,r = input().split()
    l = int(l)
    r = int(r)
    if a in D:
        l_i = bisect_left(D[a],l)
        r_i = bisect_left(D[a],r+1)
        print(r_i - l_i)
    else:
        print(0)
