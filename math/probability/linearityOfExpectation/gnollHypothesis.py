n,k = map(int,input().split())
L = list(map(float,input().split()))
L += L
ChoiceProb = []
Ans = []

if k == 1:
    print(*[100/n for _ in range(n)])
    exit()

for i in range(n-k+1):
    p = k/n
    for j in range(i):
        p *= (n-k-j) / (n-j-1)
    p *= (k-1)/(n-i-1)
    ChoiceProb.append(p)

for i in range(n):
    p = 0
    origin = n+i
    for j in range(n-k+1):
        p += sum(L[origin-j:origin+1])*ChoiceProb[j]
    Ans.append(p)

print(*Ans)