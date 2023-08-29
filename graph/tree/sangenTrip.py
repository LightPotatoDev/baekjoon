import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    for _ in range(m):
        input()
    print(n-1)
