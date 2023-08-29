n = int(input())
L = list(map(int,input().split()))
A = []

for i in range(n):
    B = []
    for j in range(i):
        if L[j] < L[i]:
            B.append(A[j])
        else:
            B.append(0)
    A.append(max(B,default=0)+L[i])

print(max(A))