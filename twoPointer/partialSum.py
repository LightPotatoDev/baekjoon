n,s = map(int,input().split())
L = [0] + list(map(int,input().split()))
minLen = int(1e5)+1
pi = 0
pj = 0

for i in range(n):
    L[i+1] += L[i]

while pj < n:
    val = L[pi] - L[pj]
    if val < s and pi < n:
        pi += 1
    else:
        if val >= s:
            minLen = min(minLen, pi-pj)
        pj += 1

if minLen != int(1e5)+1:
    print(minLen)
else:
    print(0)