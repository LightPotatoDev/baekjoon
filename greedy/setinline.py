n = int(input())
L = list(map(int,input().split()))
order = [0]*n

for i,x in enumerate(L):
    order[x-1] = i

ans = 1
lis = 1
for i in range(1,n):
    if order[i-1] < order[i]:
        lis += 1
    else:
        ans = max(ans,lis)
        lis = 1
ans = max(ans,lis)

print(n-ans)