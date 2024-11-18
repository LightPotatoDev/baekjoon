import sys
input = sys.stdin.readline

n = int(input())
L = [0] + list(map(int,input().split()))
for i in range(n):
    L[i+1] += L[i]

m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    print(L[b]-L[a-1])
