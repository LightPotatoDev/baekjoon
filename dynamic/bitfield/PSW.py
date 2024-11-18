import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]
k = int(input())

dp = [[0]*(1<<n) for _ in range(k)]
mask = (1<<n)-1
allDigit = sum([len(str(i)) for i in L])
dp[0][0] = 1

def PSW(r,digit,visited):
    if visited == mask:
        return

    for i in range(n):
        if visited & (1<<i) == 0:
            newR = (r+(L[i]*10**(digit-1)%k))%k
            print(newR,bin(visited)[2:].zfill(3))
            dp[newR][visited | (1<<i)] += dp[r][visited]
            for j in dp:
                print(j)
            print('')
            PSW(newR,digit-len(str(L[i])), visited | (1 << i))


PSW(0,allDigit,0)
for i in dp:
    print(i)
