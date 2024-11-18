import sys
input = sys.stdin.readline

class Com:
    def __init__(self,t,i):
        self.time = 0
        self.work = t
        self.num = i

    def __repr__(self):
        print(f"{self.time} {self.work} {self.num}")

n = int(input())
coms = [[] for _ in range(101)]
for i in range(1,n+1):
    l,t = map(int,input().split())
    coms[l].append(Com(t,i))

for i in range(1,n):
    for prev in coms[i]:
        for next in coms[i+1]:
            send = (prev.num - next.num) ** 2
            next.time = max(next.time, prev.time + prev.work + send)

ans = 0
for i in coms:
    for j in i:
        ans = max(ans, j.time + j.work)
print(ans)
