from itertools import combinations, permutations
import math

n = int(input())
table = [list(map(int,input().split())) for _ in range(n)]
diff = 10**9

comb = list(combinations([i for i in range(n)],n//2))

for i in range(math.comb(n,n//2)//2):
    teamA = comb[i]
    teamB = comb[-1-i]

    skillA = 0
    skillB = 0

    for j in list(permutations(teamA,2)):
        skillA += table[j[0]][j[1]]

    for j in list(permutations(teamB,2)):
        skillB += table[j[0]][j[1]]

    if abs(skillA-skillB) < diff:
        diff = abs(skillA-skillB)

print(diff)