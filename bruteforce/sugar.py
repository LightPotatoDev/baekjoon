n = int(input())

L = []
for a in range(1667):
    for b in range(1001):
        if 3*a + 5*b == n:
            L.append(a+b)

if len(L) != 0:
    print(min(L))
else:
    print(-1)