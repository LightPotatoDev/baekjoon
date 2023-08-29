import sys
input = sys.stdin.readline

n = int(input())
rSmall = [n-1]*n
lSmall = [0]*n
L = list(map(int,input().split()))

stack = []
for i,x in enumerate(L):
    while stack and stack[-1][1] > x:
        rSmall[stack[-1][0]] = i-1
        stack.pop()
    stack.append((i,x))

stack = []
for i,x in enumerate(L[::-1]):
    while stack and stack[-1][1] > x:
        lSmall[stack[-1][0]] = n-i
        stack.pop()
    stack.append((n-i-1,x))

maxArea = 0
for i in range(n):
    maxArea = max(maxArea, L[i]*(rSmall[i]-lSmall[i]+1))

print(maxArea)