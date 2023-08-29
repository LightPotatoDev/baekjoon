mod = int(1e9)+7
L = [0,1]
n = int(input())
for i in range(n-1):
    L.append((L[i]+L[i+1])%mod)

print(L[n])