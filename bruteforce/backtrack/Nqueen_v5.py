n = int(input())
L = [i for i in range(n)]
cnt = 0

def canplace(subset,index,i):
    banlist = set()
    for j in subset:
        a = j + index - subset.index(j)
        b = j - index + subset.index(j)
        if 0 <= a < n:
            banlist.add(a)
        if 0 <= b < n:
            banlist.add(b)
    if len(banlist) == n:
        return (False,False)
    if i in banlist:
        return (False,True)
    else:
        return (True,True)

def placequeen(L,index,subset):
    global cnt

    if index >= n:
        cnt += 1
        return

    for i in L:
        A = L[:]
        a = A.pop(L.index(i))
        placeable = canplace(subset,index,i)
        if placeable[1] == False:
            return
        elif placeable[0] == True:
            placequeen(A,index+1,subset+[a])

placequeen(L,0,[])
print(cnt)