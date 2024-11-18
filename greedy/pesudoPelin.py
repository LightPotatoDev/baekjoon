T = int(input())

def checkpelin(i,j):
    while i < j:
        if s[i] != s[j]:
            return [0,i,j]
        i += 1
        j -= 1
    return [1,i,j]

for _ in range(T):
    s = input()
    p1 = 0
    p2 = len(s)-1

    res,p1,p2 = checkpelin(p1,p2)
    if res == 1:
        print(0)
        continue
    if res == 0:
        res2,a,b = checkpelin(p1+1,p2)
        res3,a,b = checkpelin(p1,p2-1)
        if res2 == 0 and res3 == 0:
            print(2)
        else:
            print(1)
