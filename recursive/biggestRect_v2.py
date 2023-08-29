import sys
input = sys.stdin.readline

def histo(A):
    global maxArea
    print(A)

    if len(A) <= 1:
        return

    minH = min(A)
    maxArea = max(maxArea,minH * len(A))

    histo(A[:A.index(minH)])
    if A.index(minH) < n-1:
        histo(A[A.index(minH)+1:])

while True:
    inp = input().rstrip()
    L = []
    if inp == '0':
        break
    else:
        line = inp.split()
        n = int(line[0])
        L = list(map(int,line[1:]))

    maxArea = 0
    histo(L)
    print(maxArea)


