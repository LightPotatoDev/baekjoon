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

preSum = L[:]
for i in range(1,n):
    preSum[i] += preSum[i-1]

maxNum = -1
for i in range(n):
    num = L[i] * (preSum[rSmall[i]] - preSum[lSmall[i]-1] * int(lSmall[i] != 0))
    if num > maxNum:
        maxNum = num

print(maxNum)