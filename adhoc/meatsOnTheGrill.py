import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h,w = map(int,input().split())
    L = [input().rstrip() for _ in range(h)]
    for i in L:
        print(i[::-1])