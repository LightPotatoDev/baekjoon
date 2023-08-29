import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int,input().split()))

if n == 1:
    print(sum(L)-max(L))
    exit(0)

side1 = (n-2)**2 + (4*n-8)*(n-1)
side2 = 4*(n-1) + (4*n-8)
side3 = 4

case2 = [(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,6),
        (3,5),(3,6),(4,5),(4,6),(5,6)]
case3 = [(1,2,3),(1,2,4),(1,5,3),(1,5,4),(6,2,3),(6,2,4),(6,5,3),(6,5,4)]

def getSum(case):
    S = []
    for c in case:
        s = 0
        for i in c:
            s += L[i-1]
        S.append(s)
    return S

min1 = min(L)
min2 = min(getSum(case2))
min3 = min(getSum(case3))

print(side1*min1 + side2*min2 + side3*min3)