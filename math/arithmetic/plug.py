import sys
input = sys.stdin.readline

n = int(input())
s = sum([int(input()) for _ in range(n)])
print(s-n+1)