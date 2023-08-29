n = int(input())
das = int(input())
L = []
for _ in range(n-1):
    L.append(int(input()))

if not L:
    print(0)
    exit(0)

cnt = 0
while True:
    L.sort()
    if L[-1] < das:
        break
    else:
        cnt += 1
        L[-1] -= 1
        das += 1

print(cnt)
