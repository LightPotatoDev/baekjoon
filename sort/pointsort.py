import sys

n = int(input())
L = []
for _ in range(n):
    L.append(list(map(int,sys.stdin.readline().split())))

L.sort(key=lambda x:(x[1],x[0]))
for i in range(n):
    print(' '.join(map(str,L[i])))