from collections import defaultdict

n = int(input())
words = [input() for _ in range(n)]
D = defaultdict(int)
first = set()

for word in words:
    first.add(word[0])
    for i,x in enumerate(word[::-1]):
        D[x] += 10**i

L = [(i,D[i]) for i in D]
L.sort(key=lambda x:x[1])

if len(L) == 10:
    for i in L:
        if i[0] not in first:
            L.remove(i)
            break

ans = 0
for i in range(10-len(L),10):
    ans += i * L[i-(10-len(L))][1]
print(ans)