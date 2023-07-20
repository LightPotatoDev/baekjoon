n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort(reverse=True)

total = 0
for i in range(n):
    total += A[i] * B[i]

print(total)