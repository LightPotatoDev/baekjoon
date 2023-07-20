s = input()

nums = []
oper = []

if s[0] == '-':
    oper.append('-')
    s = s[1:]
else:
    oper.append('+')

substr = ""
curNum = False
for i in s:
    if i.isdigit() and i != '0' and curNum == False:
        curNum = True
    if curNum == True:
        if i.isdigit():
            substr += i
        else:
            nums.append(int(substr))
            substr = ""
            oper.append(i)
            curNum = False
nums.append(int(substr))

total = 0
curState = "+"
for i,x in enumerate(oper):
    if x == '-':
        curState = "-"
    if curState == "+":
        total += nums[i]
    else:
        total -= nums[i]

print(total)

#operator 각각을 저장할 필요 없이 -가 첫 번째로 나오는 위치만 저장하면 됨