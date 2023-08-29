import sys
input = sys.stdin.readline

n = int(input())
L = [float(input()) for _ in range(n)]

for i in range(1,n):
    L[i] = max(L[i-1]*L[i], L[i])

print("{:.3f}".format(round(max(L),3)))