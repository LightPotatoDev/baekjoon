from collections import deque

n = int(input())
H = list(map(int,input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]

