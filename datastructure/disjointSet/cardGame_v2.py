import sys
input = sys.stdin.readline

def find(n1):
    if n1 == N[n1][parent]:
        return n1

    root = find(N[n1][parent])
    N[n1][parent] = root
    return root

def union(n1,n2):
    root1 = find(n1)
    root2 = find(n2)
    if root1 == root2:
        return
    if N[root1][rank] >= N[root2][rank]:
        N[root2][parent] = N[root1][parent]
        if N[root1][rank] == N[root2][rank]:
            N[root1][rank] += 1

        N[root1][maxCard] = max(N[root1][maxCard], N[root2][maxCard])
    else:
        N[root1][parent] = N[root2][parent]

        N[root2][maxCard] = max(N[root1][maxCard], N[root2][maxCard])

def nearUnion(node,i):
    if 1<=i<=int(4e6)+1 and N[i][cantUse] == True:
        union(node,i)

data,parent,rank,cantUse,maxCard = 0,1,2,3,4

n,m,k = map(int,input().split())
N = [0]+[[i,i,1,True,i] for i in range(1,int(4e6)+1)] #data,parent,rank,cantUse,maxCard
Cards = list(map(int,input().split()))

for i in Cards:
    N[i][cantUse] = False

for i in range(1,int(4e6)):
    if N[i][cantUse] and N[i+1][cantUse]:
        union(i,i+1)

Opponent = list(map(int,input().split()))
for i in Opponent:
    num = i+1
    card = N[num]
    if card[cantUse] == True:
        num = N[num][maxCard]+1
        card = N[num]

    N[num][cantUse] = True
    print(num)
    nearUnion(num,num-1)
    nearUnion(num,num+1)
