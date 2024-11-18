n = int(input())
L = list(map(int,input().split()))
L.sort()
ans = int(1e9)
for i in range(n):
    ans = min(ans,L[i]+L[2*n-i-1])
print(ans)