n,m = map(int,input().split())
L = list(map(int,input().split()))
L.sort()
seq = set()

def picknumber(L,index,subset):
    global seq
    if index >= m:
        seq.add(' '.join(map(str,subset)))
        return

    A = L[:]
    for i in range(len(L)):
        a = A.pop(0)
        picknumber(A,index+1,subset+[a])

picknumber(L,0,[])

seq_list = []
for i in seq:
    seq_list.append(list(map(int,i.split())))
seq_list.sort()
for i in seq_list:
    print(' '.join(map(str,i)))