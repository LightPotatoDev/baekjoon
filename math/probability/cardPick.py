n = int(input())
L = list(map(int,input().split()))
D = {}
mod = int(1e9)+7
ans = 0

for i in L:
    if i in D:
        D[i] += 1
    else:
        D[i] = 1

for i in D:
    ans = (ans + D[i] + (ans * D[i]) % mod) % mod
print(ans)