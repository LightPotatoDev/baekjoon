n = int(input())

def secondmin(L):
    A = L[:]
    A[L.index(min(L))] = 1001
    return A.index(min(A))

dp1 = [0 for _ in range(n)] #최선책 선택
dp2 = [0 for _ in range(n)] #차선책 선택

for i in range(n):
    L = list(map(int,input().split()))
    first = L.index(min(L))
    second = secondmin(L)

    print(first,second)

    if i == 0:
        dp1[i] = [L[first],first]
        dp2[i] = [L[second],second]

    if i >= 1:
        if dp1[i-1][1] == first: #최선 -> 최선 불가능
            dp1[i] = [dp2[i-1][0] + L[first],first]
            dp2[i] = [dp1[i-1][0] + L[second],second]
        elif dp1[i-1][1] == second: #최선 -> 차선 불가능
            dp1[i] = [dp1[i-1][0] + L[first],first]
            dp2[i] = [dp2[i-1][0] + L[second],second]
        else:
            dp1[i] = [dp1[i-1][0] + L[first],first]
            dp2[i] = [dp1[i-1][0] + L[second],second]

        if dp1[i][0] > dp2[i][0]:
            dp1[i],dp2[i] = dp2[i],dp1[i]


    print(dp1)
    print(dp2)