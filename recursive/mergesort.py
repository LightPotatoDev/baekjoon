import sys
input = sys.stdin.readline

def merge(L,p,q,r):
    global save_i
    global tmp
    i,j,t = p,q+1,1
    tmp = [0] * (len(L)+1)
    while i <= q and j <= r:
        if L[i] <= L[j]:
            tmp[t] = L[i]
            t += 1
            i += 1
        else:
            tmp[t] = L[j]
            t += 1
            j += 1
    while i <= q:
        tmp[t] = L[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = L[j]
        t += 1
        j += 1
    i,t = p,1
    while i <= r:
        L[i] = tmp[t]
        save_i += 1
        if save_i == k:
            print(tmp[t])
        i += 1
        t += 1


def merge_sort(L,p,r):
    if p < r:
        q = (p+r) // 2
        merge_sort(L,p,q)
        merge_sort(L,q+1,r)
        merge(L,p,q,r)


n,k = map(int,input().rstrip().split())
L = list(map(int,input().rstrip().split()))
save = 0
save_i = 0
merge_sort(L,0,len(L)-1)
if save_i < k:
    print(-1)