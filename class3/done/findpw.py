import sys
input = sys.stdin.readline

n,m = map(int,input().split())
D = dict()
for _ in range(n):
    site, pw = input().rstrip().split()
    D[site] = pw

for _ in range(m):
    print(D[input().rstrip()])
