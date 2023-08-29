T = int(input())

for _ in range(T):
    k = int(input())
    L = []

    flag = False
    for i in range(14,-1,-1):
        val = k // 3**i
        if val > 0:
            flag = True
        if flag == True:
            L.append(val)
        k -= val * (3**i)

    print(*L)


