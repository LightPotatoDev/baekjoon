a = list(input())
aR = a[::-1]
l = len(a)
t = input()
stk1 = []
stk2 = []

i = 0
j = len(t)-1
mode = 0

while i <= j:
    while mode == 0 and i <= j:
        stk1.append(t[i])
        i += 1

        if len(stk1) >= l and stk1[-l:] == a:
            mode = 1
            for _ in range(l):
                stk1.pop()

    while mode == 1 and i <= j:
        stk2.append(t[j])
        j -= 1

        if len(stk2) >= l and stk2[-l:] == aR:
            mode = 0
            for _ in range(l):
                stk2.pop()

while stk2:
    p = stk2.pop()
    stk1.append(p)
    if len(stk1) >= l and stk1[-l:] == a:
        for _ in range(l):
            stk1.pop()

print(''.join(stk1))
