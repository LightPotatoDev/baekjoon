from collections import defaultdict

n = int(input())
words = [input() for _ in range(n)]
D = defaultdict(int)

for word in words:
    for i,x in enumerate(word[::-1]):
        D[x] += 10**i

L = list(D.values())
L.sort(reverse=True)
ans = 0
for i,x in enumerate(L):
    ans += (9-i) * x
print(ans)