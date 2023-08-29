import math
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
b,c = map(int,input().split())

cnt = 0
for a in A:
    a -= b
    cnt += 1
    if a < 0:
        continue
    cnt += math.ceil(a/c)
print(cnt)