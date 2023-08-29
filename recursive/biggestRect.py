import sys
input = sys.stdin.readline

while True:
    inp = input().rstrip()
    L = []
    if inp == '0':
        break
    else:
        L = list(map(int,inp.split()[1:]))

    for i in range(len(L)):
        L[i] = (L[i],i)
    maxArea = 0
    S = sorted(L)
    zeros = []




