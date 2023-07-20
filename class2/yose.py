n,k = map(int,input().split())
L = [i+1 for i in range(n)]

output = []
if k != 1:
    pos = 0
    curlen = n
    step = k - 1
    while curlen>0:
        pos = (pos+1) % curlen
        step -= 1
        if step <= 0:
            step = k - 1
            curlen -= 1
            output.append(L[pos])
            L.pop(pos)
else:
    output = L

print('<'+', '.join(map(str,output))+'>')