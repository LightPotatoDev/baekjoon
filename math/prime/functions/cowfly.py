from itertools import combinations

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n,m = map(int,input().split())
H = list(map(int,input().split()))

Ans = set()
comb = combinations(H,m)
for c in comb:
    s = sum(c)
    if isPrime(s):
        Ans.add(s)

Ans = list(Ans)
Ans.sort()
if Ans:
    print(*Ans)
else:
    print(-1)