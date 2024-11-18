import sys
input = sys.stdin.readline
from math import perm

n,m = map(int,input().split())
x,y = map(int,input().split())
case = 0
A = 0
B = 0
for _ in range(m):
    a,b = map(int,input().split())
    if a != 0:
        A += 1
    else:
        B += 1

case = perm(9-A-B,n-A-B) * perm(n-A,B)
print(case*x + ((case-1)//3)*y)