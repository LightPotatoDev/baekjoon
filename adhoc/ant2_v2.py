import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    l,n = map(int,input().split())
    L = [int(input()) for _ in range(n)]
    endDist = [min(i,l-i) for i in L]
    print(max(endDist), max([l-i for i in endDist]))