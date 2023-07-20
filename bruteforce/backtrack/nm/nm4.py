n,m = map(int,input().split())
L = [i+1 for i in range(n)]
seq = []

def picknumber(L,index,subset):
    global seq
    if index >= m:
        seq.append(subset)
        return

    for i in range(len(L)):
        A = L[:]
        a = A[i]
        picknumber(A[A.index(a):],index+1,subset+[a])

picknumber(L,0,[])
for i in seq:
    print(' '.join(map(str,i)))