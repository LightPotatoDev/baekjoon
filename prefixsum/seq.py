n,k = map(int,input().split())

L = list(map(int,input().split()))
A = [sum(L[:k])]
for i in range(n-k):
    A.append(A[i]+L[i+k]-L[i])

print(max(A))