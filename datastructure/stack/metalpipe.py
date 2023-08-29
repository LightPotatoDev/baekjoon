s = input()
s = s.replace("()",".")

pipes = 0
newpipes = 0
cnt = 0
for i in s:
    if i == "(":
        pipes += 1
        newpipes += 1
    elif i == ")":
        pipes -= 1
    elif i == ".":
        cnt += pipes + newpipes
        newpipes = 0

print(cnt)