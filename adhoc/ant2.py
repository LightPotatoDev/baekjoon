import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    l,n = map(int,input().split())
    L = [abs(int(input())-l) for _ in range(n)]
    fastest = 0
    for i in L:
        if i <= l//2:
            fastest = max(fastest,i)

    print(fastest, max(L))