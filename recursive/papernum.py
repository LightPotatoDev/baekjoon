n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]

papers = [0,0,0] #-1,0,1

def same(A):
    ref = A[0][0]
    for row in A:
        for i in row:
            if i != ref:
                return 9
    return ref

def cut(y,x,n):
    global papers

    num = same([L[i][x:x+n] for i in range(y,y+n)])
    if num != 9:
        papers[num+1] += 1
        return

    for i in range(3):
        for j in range(3):
            cut(y+i*(n//3), x+j*(n//3), n//3)

cut(0,0,n)
for i in papers:
    print(i)