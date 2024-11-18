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
    while i <= n:
        hp = prefixSum(i,j)
        if i <= l <= j <= r:
            hp -= prefixSum(l,i)
        elif l <= i <= r <= j:
            hp -= prefixSum(i,r)
        elif l <= i <= j <= r:
            hp -= prefixSum(i,j)
        elif i <= l <= r <= j:
            hp -= prefixSum(l,r)

        if hp < hpNeeded and j < n:
            j += 1
        else:
            i += 1
            if hp >= hpNeeded:
                wins += 1
                print(atk,hp,turns)
                print(l,r,i,j)
                print('')

    return wins

for i in range(1,n+1):
    for j in range(i,n+1):
        ans += battle(prefixSum(i,j),i,j)

print(ans)