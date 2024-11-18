n = int(input())
mobAtk,mobHp = map(int,input().split())
cards = list(map(int,input().split()))
cardSum = [0]*(n+1)
ans = 0

for i in range(n):
    cardSum[i+1] = cardSum[i] + cards[i]

def prefixSum(l,r):
    return cardSum[r]-cardSum[l-1]

def battle(atk,l,r):
    turns = (mobHp-1) // atk + 1
    hpNeeded = mobAtk*turns + 1
    wins = 0

    i = 1
    j = 1
    while i <= n and j <= n:
        if l <= i <= r:
            i = r+1
            continue
        if l <= j <= r:
            j = r+1
            continue

        hp = prefixSum(i,j)
        if i <= l <= r <= j:
            hp -= prefixSum(l,r)


        if hp < hpNeeded and j < n:
            j += 1
        else:
            if hp >= hpNeeded:
                wins += (n-j+1) - int(j <= l) * (r-l+1)
            i += 1

    return wins

for i in range(1,n+1):
    for j in range(i,n+1):
        ans += battle(prefixSum(i,j),i,j)

if ans != 0:
    print(ans)
else:
    print('IMPOSSIBLE')