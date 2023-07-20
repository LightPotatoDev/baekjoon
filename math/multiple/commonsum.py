while True:
    n = int(input())
    if n == -1:
        break
    L = []

    for i in range(1, n):
        if n%i == 0:
            L.append(i)

    if sum(L) == n:
        print(f"{n} = {' + '.join(map(str,L))}")
    else:
        print(f"{n} is NOT perfect.")