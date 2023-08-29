def getAllDiv(n):
    Div = [[1] for _ in range(n+1)]
    for i in range(2,n+1):
        for j in range(i,n+1,i):
            Div[j].append(i)
    return Div

D = getAllDiv(100000)

n = int(input())
sticks = [0]*100001
for i in list(map(int,input().split())):
    sticks[i] = 1

q = int(input())
targets = list(map(int,input().split()))
