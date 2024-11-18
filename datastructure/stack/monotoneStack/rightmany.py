n = int(input())
L = list(map(int,input().split()))

appears = [0] * 1000001
for i in L:
    appears[i] += 1

stack = []
F = [-1]*n
for i,x in enumerate(L):
    a = appears[x]
    while stack and stack[-1][2] < a:
        F[stack[-1][0]] = x
        stack.pop()
    stack.append((i,x,appears[x]))

print(*F)