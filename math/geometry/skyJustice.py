import sys
input = sys.stdin.readline

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]
A = []
for i in range(n):
    x,y,s = L[i]
    d = ((x**2)+(y**2))**0.5
    A.append([d/s,i+1])
A.sort(key = lambda x:(x[0],x[1]))
for i in A:
    print(i[1])