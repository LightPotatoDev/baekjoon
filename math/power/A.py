a = int(input())
x = int(input())
MOD = int(1e9)+7
ans = 1

aSquared = []
for i in range(64):
    aSquared.append(a)
    a = (a*a) % MOD

for i in range(64):
    if (x >> i) & 1 == 1:
        ans = (ans * aSquared[i]) % MOD

print(ans)
