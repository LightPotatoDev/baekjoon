T = 0
while True:
    T += 1
    s = input()
    if s[0] == "-":
        break

    stk = []
    for i in s:
        stk.append(i)
        if len(stk) >= 2 and stk[-2] == "{" and stk[-1] == "}":
            stk.pop()
            stk.pop()

    odd = int(stk.count('{') % 2 == 1)
    print(f"{T}. {len(stk)//2 + odd}")