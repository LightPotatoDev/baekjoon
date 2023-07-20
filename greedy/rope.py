import sys
input = sys.stdin.readline

n = int(input())
L = []
for _ in range(n):
    L.append(int(input()))

L.sort()
max_w = 0
for i in range(n):
    max_w = max(L[i] * (n-i),max_w)

print(max_w)