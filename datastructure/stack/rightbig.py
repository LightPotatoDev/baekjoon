n = int(input())
L = list(map(int,input().split()))

stack = []
NGE = [-1]*n
for i,x in enumerate(L):
    while stack and stack[-1][1] < x:
        NGE[stack[-1][0]] = x
        stack.pop()
    stack.append((i,x))

print(*NGE)