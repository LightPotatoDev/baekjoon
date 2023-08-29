import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    L = input().rstrip().split()
    n = float(L[0])
    for i in L[1:]:
        if i == "@":
            n *= 3
        elif i == "%":
            n += 5
        elif i == "#":
            n -= 7

    print("{:.2f}".format(n))