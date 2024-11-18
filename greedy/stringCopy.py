s = list(input())
p = list(input())

def contains(target):
    if len(target) == 0:
        return True

    ptr = 0
    for i in s:
        if i == target[ptr]:
            ptr += 1
        else:
            ptr = 0
            if i == target[ptr]:
                ptr += 1
        if ptr >= len(target):
            return True
    return False

targ = []
ans = 1

for i,x in enumerate(p):
    targ.append(x)
    if not contains(targ):
        targ = [x]
        ans += 1
print(ans)