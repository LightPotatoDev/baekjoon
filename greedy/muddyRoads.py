import sys
input = sys.stdin.readline

n,l = map(int,input().split())
muds = []
for _ in range(n):
    s,e = map(int,input().split())
    muds.append((s,e))
muds.sort()
ans = 0
covered = 0
for s,e in muds:
    covered = max(covered,s)
    planks = (e-covered-1) // l + 1
    covered += planks * l
    ans += planks
print(ans)
