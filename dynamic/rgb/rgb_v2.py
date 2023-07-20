n = int(input())

def secondmin(L):
    A = L[:]
    A[L.index(min(L))] = 1001
    return A.index(min(A))

dp = []

for i in range(n):
    L = list(map(int,input().split()))
    op1 = L.index(min(L))
    op2 = secondmin(L)
    op3 = L.index(max(L))

    if i == 0:
        dp.append([[L[op1],op1],[L[op2],op2],[L[op3],op3]])

    if i >= 1:
        A = []
        #최선 -> 최선 불가능
        if dp[i-1][0][1] == op1:
            A = [[dp[i-1][0][0]+L[op2],op2],
                 [dp[i-1][0][0]+L[op3],op3],
                 [dp[i-1][1][0]+L[op1],op1]]
        #최선 -> 차선 불가능
        elif dp[i-1][0][1] == op2:
            A = [[dp[i-1][0][0]+L[op1],op1],
                 [dp[i-1][0][0]+L[op3],op3],
                 [dp[i-1][1][0]+L[op2],op2]]
        #최선 -> 최악 불가능
        else:
            A = [[dp[i-1][0][0]+L[op1],op1],
                 [dp[i-1][0][0]+L[op2],op2],
                 [dp[i-1][1][0]+L[op3],op3]]
        A.sort()
        dp.append(A)

print(dp[-1][0][0])

""" by jyj4128043
rgb = [[x for x in map(int,input().split())] for _ in range(n)]
for i in range(1,n):
  rgb[i][0] = min(rgb[i-1][1],rgb[i-1][2]) + rgb[i][0]
  rgb[i][1] = min(rgb[i-1][0],rgb[i-1][2]) + rgb[i][1]
  rgb[i][2] = min(rgb[i-1][1],rgb[i-1][0]) + rgb[i][2]
print(min(rgb[n-1]))

각 단계에서:
    0번째 원소 선택 시,
    바로 전 단계에서 min(1번째 원소,2번째 원소)의 값을 더함
    나머지에 대해서도 반복
"""