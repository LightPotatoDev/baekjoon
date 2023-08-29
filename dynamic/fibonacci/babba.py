n = int(input())
A = [0,1]
B = [1,1]

for i in range(n-2):
    A.append(A[i]+A[i+1])
    B.append(B[i]+B[i+1])
print(A[n-1],B[n-1])