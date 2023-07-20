T = int(input())

def groupcheck(s):
    curstr = ''
    strlist = []
    for i in s:
        if i != curstr:
            if i in strlist:
                return 0
            else:
                strlist.append(curstr)
                curstr = i
    return 1

g = 0
for _ in range(T):
    g += groupcheck(input())

print(g)