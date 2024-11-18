s = "1(" + input() + ")"
nums = [[] for _ in range(50)]
stk = []

t = 0
for i in range(len(s)):
    l = len(stk)
    if s[i].isdigit():
        if s[i+1] == "(":
            nums[l].append(t)
            nums[l].append(int(s[i]))
            t = 0
        elif s[i+1] == ")":
            nums[l].append(t+1)
            t = 0
        else:
            t += 1
    elif s[i] == "(":
        stk.append(s[i])
    elif s[i] == ")":
        stk.pop()
        nums[l-1][-1] *= sum(nums[l])
        nums[l] = []

print(sum(nums[0]))