from collections import deque

n = int(input())
de = deque([i+1 for i in range(n)])

curlen = n
while n > 1:
    de.popleft()
    a = de.popleft()
    de.append(a)
    n -= 1

print(de[0])