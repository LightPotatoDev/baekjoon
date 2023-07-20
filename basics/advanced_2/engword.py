import sys
input = sys.stdin.readline

D = dict()
n,m = map(int,input().split())
for _ in range(n):
    s = input().rstrip()
    if len(s) >= m:
        if s in D:
            D[s] += 1
        else:
            D[s] = 1

D = sorted(D.items(), key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in D:
    print(i[0])