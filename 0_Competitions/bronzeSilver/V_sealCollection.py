from collections import defaultdict
n = int(input())
D = defaultdict(int)
Req = {"B":1, "E":2, "I":1, "L":1, "N":1, "O":1, "R":2,
        "S":1, "V":1, "Z":1}

s = list(input())
for i in s:
    D[i] += 1

ans = int(1e8)
for i in Req:
    ans = min(ans, D[i] // Req[i])

print(ans)