import sys
input = sys.stdin.readline

n = int(input())
ans = 0
mod = int(1e9)+7

for _ in range(n):
    x,k = map(int,input().split())
    s = 0
    i = 0
    while k > 0:
        if k & 1 == 1:
            s = (s + pow(x,i,mod)) % mod
        i += 1
        k >>= 1
    ans = (ans + s) % mod

print(ans)