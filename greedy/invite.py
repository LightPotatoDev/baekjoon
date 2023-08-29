n = int(input())
L = list(map(int,input().split()))
L.sort(reverse=True)

for i in range(n):
    L[i] += i+1

print(max(L)+1)