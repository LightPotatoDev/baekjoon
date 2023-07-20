#dp
L = [[1,3]]

n = int(input())
for i in range(n-1):
    L2 = []

    for x in L:
        tmp = x[:]
        for j in range(0,2):
            if tmp[j] != 1: tmp[j] = 5 - tmp[j]
        L2.append(tmp)

    L2.append([1,3])

    for x in L:
        tmp = x[:]
        for j in range(0,2):
            if tmp[j] != 3: tmp[j] = 3 - tmp[j]
        L2.append(tmp)

    L = L2[:]

print(len(L))
for i in L:
    print(' '.join(map(str,i)))

"""ghkrxhd410: recursive
def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n-1, start, 6-start-end)
    print(start, end)
    hanoi(n-1, 6-start-end, end)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)
"""