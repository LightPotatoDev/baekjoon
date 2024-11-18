import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]
L.sort()
s = 0
for i in range(n):
    s += abs((i+1)-L[i])
print(s)