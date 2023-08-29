from collections import defaultdict

n = int(input())
D = defaultdict(int)
for _ in range(n):
    D[input()] += 1

most = [i for i in D.keys() if D[i] == max(D.values())]
most.sort()
print(most[0])