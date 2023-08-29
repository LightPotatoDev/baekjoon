m = int(input())
n = int(input())

L = [i**2 for i in range(1,101)]
A = []
cnt = 0
for i in range(m,n+1):
    if i in L:
        A.append(i)

if A:
    print(sum(A))
    print(min(A))
else:
    print(-1)