import sys
input = sys.stdin.readline

n,k = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
L.sort(key=lambda x:(x[1],x[2],x[3]), reverse=True)
grade = [0]*(n+1)
rank = 1
for i,x in enumerate(L):
    c,g,s,b = x
    if i != 0:
        pc,pg,ps,pb = L[i-1]
        if pg != g or ps != s or pb != b:
            rank = i+1
    grade[c] = rank


print(grade[k])