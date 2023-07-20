n = int(input())
L = [[1,0],[2,1]] #[2x2 타일 미포함,2x2 타일 포함]

for i in range(2,n):
    L.append([L[i-1][0]+L[i-2][0] , L[i-2][0]+L[i-2][1]*2+L[i-1][1]])

print(sum(L[n-1])%10007)