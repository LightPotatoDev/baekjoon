grid = [[0 for _ in range(100)] for _ in range(100)]

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            grid[x-1+i][y-1+j] = 1

ones = 0
for i in range(100):
    ones += grid[i].count(1)

print(ones)