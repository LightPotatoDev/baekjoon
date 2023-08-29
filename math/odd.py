L = []
for _ in range(7):
    i = int(input())
    if i%2 == 1:
        L.append(i)

if L:
    print(sum(L))
    print(min(L))
else:
    print(-1)