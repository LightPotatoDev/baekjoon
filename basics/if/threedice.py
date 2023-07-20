eyeList = list(map(int,input().split()))
eyeSet  = set(eyeList)
bonus = (10000, 1000, 0)
multiply = (1000, 100, 100)
same = len(eyeSet)
n = 0

if same == 2:
    for i in eyeList:
        if eyeList.count(i) == 2:
            n = i
            break
else:
    n = max(eyeList)

print(bonus[same - 1] + n * multiply[same - 1])
