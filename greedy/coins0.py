n,k = map(int,input().split())
L = [int(input()) for _ in range(n)]

coins = 0
for i in range(n-1, -1, -1):
    coins += k // L[i]
    k -= (k//L[i]) * L[i]

print(coins)