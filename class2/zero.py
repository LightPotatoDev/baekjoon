import sys
T = int(input())
L = []

for _ in range(T):
    n = int(sys.stdin.readline())
    if n == 0:
        L.pop(-1)
    else:
        L.append(n)

print(sum(L))