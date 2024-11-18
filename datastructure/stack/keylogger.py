import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input().rstrip()
    stk1 = []
    stk2 = []

    for i in s:
        if i == "<":
            if stk1:
                p = stk1.pop()
                stk2.append(p)
        elif i == ">":
            if stk2:
                p = stk2.pop()
                stk1.append(p)
        elif i == "-":
            if stk1:
                stk1.pop()
        else:
            stk1.append(i)

    print(''.join(stk1) + ''.join(stk2[::-1]))