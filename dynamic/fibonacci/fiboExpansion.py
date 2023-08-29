mod = int(1e9)
L = [0,1]
n = int(input())
for i in range(abs(n)-1):
    L.append((L[i]+L[i+1])%mod)

if n<0 and n%2 == 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(L[abs(n)])