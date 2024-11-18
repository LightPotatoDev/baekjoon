import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
D = dict()
for _ in range(n):
    s,p = input().rstrip().split()
    D[s] = int(p)

score = 0
for _ in range(k):
    s = input().rstrip()
    score += D[s]
    D.pop(s)

S = list(D.values())
S.sort()
minS = 0
maxS = 0
for i in range(m-k):
    minS += S[i]
    maxS += S[-(i+1)]
print(score+minS, score+maxS)