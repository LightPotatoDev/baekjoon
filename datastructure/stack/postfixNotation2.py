n = int(input())
s = input()
L = [int(input()) for _ in range(n)]

stk = []
for i in s:
    if i == "+":
        a = stk.pop()
        b = stk.pop()
        stk.append(a+b)
    elif i == "-":
        a = stk.pop()
        b = stk.pop()
        stk.append(b-a)
    elif i == "*":
        a = stk.pop()
        b = stk.pop()
        stk.append(a*b)
    elif i == "/":
        a = stk.pop()
        b = stk.pop()
        stk.append(b/a)
    else:
        stk.append(L[ord(i)-65])

print("{:.2f}".format(stk[0]))