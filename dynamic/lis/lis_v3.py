n = int(input())
L = list(map(int,input().split()))
dp = [[] for _ in range(n)]

for i,x in enumerate(L):
    if i == 0:
        dp[i] = [[x]]
    else:
        dp[i].append([x])
        for j in dp[i-1]:
            dp[i].append(j)
            if j[-1] < x:
                dp[i].append(j + [x])

    #끝자리가 같으면, 길이가 제일 긴 것 중 하나만 남김
    D = dict()
    for j in dp[i]:
        if j[-1] not in D:
            D[j[-1]] = j
        if len(j) > len(D[j[-1]]):
            D[j[-1]] = j
    dp[i] = list(D.values())

    #길이가 같으면, 끝자리가 제일 작은 것만 남김
    D = dict()
    for j in dp[i]:
        if len(j) not in D:
            D[len(j)] = j
        if j[-1] < D[len(j)][-1]:
            D[len(j)] = j
    dp[i] = list(D.values())


ans = [arr for arr in dp[n-1] if len(arr) == max([len(arr) for arr in dp[n-1]])][0]
print(len(ans))
print(' '.join(map(str,ans))) # = print(*ans)