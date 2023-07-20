import sys
input = sys.stdin.readline

n,m = map(int,input().split())
D = dict()
for i in range(n):
    D[input()] = i

contains = 0
for i in range(m):
    try:
        D[input()]
        contains += 1
    except:
        pass

print(contains)