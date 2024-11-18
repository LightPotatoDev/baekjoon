n = int(input())
ans = 0
for _ in range(n):
    stk = []
    s = input()
    for i in s:
        if stk and stk[-1] == i:
            stk.pop()
        else:
            stk.append(i)

    ans += int(len(stk) == 0)

print(ans)