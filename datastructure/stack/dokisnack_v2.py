n = int(input())
L = list(map(int,input().split()))

stk = []
cnt = 1
for i in L:
    if i == cnt:
        cnt += 1
        while stk and stk[-1] == cnt:
            cnt += 1
            stk.pop()
    else:
        stk.append(i)

if stk:
    print("Sad")
else:
    print("Nice")
