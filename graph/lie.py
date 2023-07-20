import sys
input = sys.stdin.readline

n,m = map(int,input().split())
real = set(map(int,input().split()[1:]))

parties = []
for _ in range(m):
    parties.append(set(map(int,input().split()[1:])))

for people in parties:
    if len(real&people) >= 1:
        real = real|people
for people in parties[::-1]:
    if len(real&people) >= 1:
        real = real|people

cnt = 0
for people in parties:
    if len(real&people) == 0:
        cnt += 1
print(cnt)