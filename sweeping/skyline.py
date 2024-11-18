import sys
input = sys.stdin.readline

n = int(input())
builds = [list(map(int,input().split())) for _ in range(n)]
builds.sort(key = lambda x:(x[0], x[1], x[2]))
D = {builds[0][0]:builds[0][1], builds[0][2]: 0}

for i in range(n-1):
    l1, h1, r1 = builds[i]
    l2, h2, r2 = builds[i+1]

    D[]
