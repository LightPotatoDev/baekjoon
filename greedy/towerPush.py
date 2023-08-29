n = int(input())
H = list(map(int,input().split())) + [1000001]
stack = []
cnt = 0
for i in H:
    if stack and stack[-1] <= i:
        stack = []
        cnt += 1
    stack.append(i)

print(cnt)