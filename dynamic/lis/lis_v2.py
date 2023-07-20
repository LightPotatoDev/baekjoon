n = int(input())
L = list(map(int,input().split()))
dp = [[] for _ in range(n)]

for i,x in enumerate(L):
    if i == 0:
        dp[i] = [[x]]
    else:
        for j in dp[i-1]:
            if x <= j[-1]:
                dp[i].append([x])
                if len(j) > 1:
                    dp[i].append(j)
            elif x == j[-1] + 1:
                dp[i].append(j+[x])
            else:
                dp[i].append(j)
                dp[i].append(j+[x])


    #끝자리가 같으면, 길이가 제일 긴 것 중 하나만 남김

    #길이가 같으면, 끝자리가 제일 작은 것만 남김


print(dp)