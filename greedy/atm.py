n = int(input())
L = list(map(int,input().split()))
L.sort()

L2 = []
t = 0
for i in range(n):
    t += L[i]
    L2.append(t)

print(sum(L2))