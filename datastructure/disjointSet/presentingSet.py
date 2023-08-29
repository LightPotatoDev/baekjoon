import sys
input = sys.stdin.readline

n,m = map(int,input().split())
L = [{i} for i in range(n+1)]

for _ in range(m):
    cmd,n1,n2 = map(int,input().split())
    if cmd == 0:
        L[n1] = L[n1] | L[n2]
        L[n2] = L[n1] | L[n2]
    else:
        if n1 in L[n2] and n2 in L[n1]:
            print("YES")
        else:
            print("NO")
    print(L)