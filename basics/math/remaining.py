T = int(input())
coins = (25, 10, 5, 1)

for _ in range(T):
    n = int(input())
    L = [0]*4

    for i in range(4):
        while n >= coins[i]:
            n -= coins[i]
            L[i] += 1
    print(' '.join(map(str,L)))