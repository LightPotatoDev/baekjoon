import sys

input = sys.stdin.readline

n,m = map(int,input().split())
pokedex = dict()
pokedex2 = dict()

for i in range(1,n+1):
    name = input().rstrip()
    pokedex[name] = i
    pokedex2[i] = name

for _ in range(m):
    q = input().rstrip()
    if q[0].isdigit():
        q = int(q)
        print(pokedex2[q])
    else:
        print(pokedex[q])
