s = input()
stk = []
pair = []

for i,x in enumerate(s):
    if x == "(" or x == ")":
        stk.append([i,x])
    if len(stk) >= 2 and stk[-2][1] == "(" and stk[-1][1] == ")":
        pair.append([stk[-2][0],stk[-1][0]])
        stk.pop()
        stk.pop()

ans = set()
for i in range(1,1<<len(pair)):
    L = list(s)
    for j in range(len(pair)):
        if ((i>>j)&1) == 1:
            a,b = pair[j]
            L[a] = "a"
            L[b] = "a"

    res = list(filter(lambda x:x!="a", L))
    ans.add(''.join(res))
ans = list(ans)
ans.sort()
for i in ans:
    print(i)
