T = int(input())

for _ in range(T):
    n = int(input())
    D = dict()
    for _ in range(n):
        e, t = input().split() #equipment, type
        if t in D:
            D[t] += 1
        else:
            D[t] = 1

    typenums = [i+1 for i in D.values()]

    total = 1
    for i in typenums:
        total *= i
    print(total-1)
