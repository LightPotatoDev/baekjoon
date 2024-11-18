import sys
input = sys.stdin.readline

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]

def triArea(v1,v2):
    crossprod = v1[0]*v2[1] - v1[1]*v2[0]
    return 1/2 * crossprod

area = 0
for i in range(1,n-1):
    v1 = [L[i][0]-L[0][0], L[i][1]-L[0][1]]
    v2 = [L[i+1][0]-L[0][0], L[i+1][1]-L[0][1]]
    area += triArea(v1,v2)

print(abs(area))