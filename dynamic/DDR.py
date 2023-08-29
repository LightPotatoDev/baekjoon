L = list(map(int,input().split()))[:-1]

dp = [[[-1]*5 for _ in range(5)] for _ in range(len(L)+1)]
dp[0][0][0] = 0

def calc(prev,next):
    if prev == next:
        return 1
    elif prev == 0:
        return 2
    elif (prev+next)%2 == 1:
        return 3
    else:
        return 4

def update(old,new):
    if old == -1:
        return new
    elif old > new:
        return new
    else:
        return old

def move(ind,mv):
    for i in range(5):
        for j in range(5):
            if dp[ind][i][j] != -1:
                if i != mv:
                    dp[ind+1][i][mv] = update(dp[ind+1][i][mv], dp[ind][i][j]+calc(j,mv))
                if j != mv:
                    dp[ind+1][mv][j] = update(dp[ind+1][mv][j], dp[ind][i][j]+calc(i,mv))

for i,x in enumerate(L):
    move(i,x)

minP = int(4e6)
for i in dp[len(L)]:
    for j in i:
        if j != -1:
            minP = min(j,minP)
print(minP)

for i in dp:
    for j in i:
        print(j)
    print('')

