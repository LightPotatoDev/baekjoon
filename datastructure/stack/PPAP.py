s = input()
stk = []
ppap = ["P","P","A","P"]
for i in s:
    stk.append(i)
    if len(stk) >= 4 and all([stk[-i]==ppap[i] for i in range(4)]):
        for i in range(4):
            stk.pop()
        stk.append("P")

if stk == ["P"]:
    print("PPAP")
else:
    print("NP")