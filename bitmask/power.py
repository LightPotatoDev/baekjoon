n = int(input())
n = bin(n)[2:]

ans = 0
for i,x in enumerate(n[::-1]):
    ans += int(x) * 3**i
print(ans)