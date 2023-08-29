import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]

L.sort()

ans = 0
while len(L) >= 3:
    ans += L.pop()+L.pop()
    L.pop()

print(ans+sum(L))