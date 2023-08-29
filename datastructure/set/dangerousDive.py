n,r = map(int,input().split())
S = set(map(int,input().split()))
N = set(i for i in range(1,n+1))
A = list(N-S)
A.sort()
if A:
    print(*A)
else:
    print("*")