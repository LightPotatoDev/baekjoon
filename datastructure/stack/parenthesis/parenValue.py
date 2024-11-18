s = input()
stk = []
nums = [[] for _ in range(30)]
correct = True

for i in s:
    l = len(stk)
    if i == "(" or i == "[":
        stk.append(i)
    elif i == ")":
        if not stk or stk[-1] != "(":
            correct = False
            break
        else:
            stk.pop()
    elif i == "]":
        if not stk or stk[-1] != "[":
            correct = False
            break
        else:
            stk.pop()

    if i == "(":
        nums[l].append(2)
    elif i == "[":
        nums[l].append(3)
    elif i == ")" and sum(nums[l]) != 0:
        nums[l-1][-1] = 2 * sum(nums[l])
        nums[l] = []
    elif i == "]" and sum(nums[l]) != 0:
        nums[l-1][-1] = 3 * sum(nums[l])
        nums[l] = []

if stk:
    correct = False
if correct:
    print(sum(nums[0]))
else:
    print(0)