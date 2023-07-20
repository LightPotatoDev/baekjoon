T = int(input())

def setpeople(inp, out, n):
    for i in range(n):
        out[i] = sum(inp[0:i+1])
    return out

for _ in range(T):
    k = int(input())
    n = int(input())

    L1 = [i+1 for i in range(n)]
    L2 = [0]*n

    for i in range(k-1):
        L2 = L1.copy()
        L1 = setpeople(L2,L1,n)

    print(sum(L1))

#for j in range(): L[j] += L[j-1]