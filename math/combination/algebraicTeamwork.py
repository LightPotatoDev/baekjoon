from math import factorial
import sys
input = sys.stdin.readline

T = int(input())
p = int(1e9)+7
for _ in range(T):
    n = int(input())
    print((factorial(n)-1)%p)