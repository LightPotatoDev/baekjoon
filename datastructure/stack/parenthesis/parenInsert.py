s = input()
stk = []
for i in s:
    stk.append(i)
    if len(stk) >= 2 and stk[-2] == "(" and stk[-1] == ")":
        stk.pop()
        stk.pop()

print(len(stk))