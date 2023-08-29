n = int(input())
d = int(1e9)+7

ans = 1
for i in range(n//2):
    ans = (ans * (2*i+1)) % d
print(ans)