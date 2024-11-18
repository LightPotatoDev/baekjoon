import sys
input = sys.stdin.readline

n = int(input())
x,s = map(int,input().split())
ans = "NO"

for i in range(n):
    c,p = map(int,input().split())
    if c <= x and p > s:
        ans = "YES"
        break

print(ans)