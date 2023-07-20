import math
import sys
input = sys.stdin.readline

n = int(input())
L = []
for _ in range(n):
    L.append(int(input()))
L.sort()

dist = []
for i in range(n-1):
    dist.append(L[i+1] - L[i])
gcd = math.gcd(dist[0],dist[1])
for i in range(2,n-1):
    gcd = math.gcd(gcd,dist[i])

maxtrees = (L[-1] - L[0]) // gcd + 1
print(maxtrees - n)

#g = math.gcd(*diffs)  #math.gcd(*L) - 리스트의 최대공약수