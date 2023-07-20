import sys

n = int(input())
L = [int(sys.stdin.readline()) for _ in range(n)]
L.sort()

for i in L:
    print(i)