import sys
input = sys.stdin.readline

def mapper(s):
    return (ord(s[0])-65)*26+ord(s[1])-65

n = int(input())
cities = []
grid = [[0]*676 for _ in range(676)]
for _ in range(n):
    city,state = input().rstrip().split()
    cn = mapper(city[:2])
    sn = mapper(state)
    cities.append((sn,cn))

for s,c in cities:
    grid[s][c] += 1

ans = 0
for i in range(676):
    for j in range(i,676):
        if i == j:
            continue
        ans += grid[i][j]*grid[j][i]

print(ans)