n = int(input())
L = list(map(int,input().split()))
L.sort()
mod = int(1e9)+7

diff = []
for i in range(n-1):
    diff.append(L[i+1]-L[i])

ans = 0
adding = 0
for i in range(n-1):
    adding = ((adding*2)%mod + (diff[i]*(pow(2,i+1,mod)-1))%mod)%mod
    ans = (ans + adding)%mod
print(ans)