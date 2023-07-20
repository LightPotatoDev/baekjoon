for i in range(1,N): #기준점
    for j in range(0, i):
        if line[j][1] < line[i][1]:
            dp[i] = max(dp[i],dp[j]+1)

#line = L