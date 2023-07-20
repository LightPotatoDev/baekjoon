n = int(input())
L = [500,100,50,10,5,1]
k = 1000 - n

coins = 0
for i in range(6):
    coins += k // L[i]
    k -= (k//L[i]) * L[i]

print(coins)