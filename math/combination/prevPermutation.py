n = int(input())
L = list(map(int,input().split()))

bound = n
for i in range(n-1,-1,-1):
    bound = i
    if i == 0:
        print(-1)
        exit()
    if L[i-1] > L[i]:
        break

A = L[:bound-1]
B = L[bound-1:]
p = B[0]-1
while not p in B:
    p -= 1
B.remove(p)
B.sort(reverse=True)
B = [p] + B
print(*(A+B))