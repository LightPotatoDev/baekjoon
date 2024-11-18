import sys
input = sys.stdin.readline
from bisect import bisect_right

T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int,input().split()))
    m = int(input())
    B = list(map(int,input().split()))
    A.sort()

    for i in B:
        ind = bisect_right(A,i)
        if A[ind-1] == i and ind != 0:
            print(1)
        else:
            print(0)