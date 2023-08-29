from collections import defaultdict

n = int(input())
D = defaultdict(int)

for _ in range(n):
    D[input()[0]] += 1

L = [i for i in D.keys() if D[i] >= 5]
L.sort()
if L:
    print(''.join(L))
else:
    print("PREDAJA")