lines = [6,2,5,5,4,5,6,3,7,5]
diff = [[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        diff[i][j] = lines[j]-lines[i]

n = input()
l = len(n)
delta_cost = []
for i in range(l):
    a = []
    num = int(n[l-i-1])
    for j in range(10):
        cost = ((j-num)%10) * 10**i
        a.append((diff[num][j], cost))
    delta_cost.append(a)

print(delta_cost)

def digital_counter(nonzero_row):
    DP_SIZE = 20
    INF = int(1e4)
    dp = [[INF]*DP_SIZE for _ in range(l+1)]
    dp[0][0] = 0

    for i in range(l):
        for d,c in delta_cost[i]:
            if i == nonzero_row and d == 0 and c == 0:
                c = 10 ** (nonzero_row+1)
            for j in range(-DP_SIZE//2, DP_SIZE//2):
                if dp[i][j] != INF:
                    dp[i+1][j+d] = min(dp[i+1][j+d], dp[i][j]+c)

    for row in dp:
        print(row)

for i in range(l):
    digital_counter(i)