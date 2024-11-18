import sys
input = sys.stdin.readline

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
dp = [[[0]*100 for _ in range(m)] for _ in range(n)] #[y][x][prob]

