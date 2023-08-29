from itertools import combinations

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]
N = {i for i in range(n)}
diff = int(1e10)

def getSkills(team):
    skill = 0
    choice = combinations(team,2)
    for a,b in choice:
        skill += L[a][b]
        skill += L[b][a]
    return skill

for i in range(1,n//2+1):
    comb = combinations(N,i)
    for teamA in comb:
        teamB = N - set(teamA)
        skillA = getSkills(teamA)
        skillB = getSkills(teamB)
        diff = min(diff,abs(skillA-skillB))

print(diff)
