import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]
L.sort(reverse=True)
s = 0
for i in range(n):
    s += max(0,L[i]-i)
print(s)