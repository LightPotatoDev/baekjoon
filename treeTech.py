from collections import deque

class Land:
    def __init__(self):
        self.tree = deque([])
        self.dead = []
        self.energy = 5

    def feed_tree(self):
        alive = deque([])
        for t in self.tree:
            if t <= self.energy:
                alive.append(t+1)
                self.energy -= t
            else:
                self.dead.append(t)
        self.tree = alive

    def dead_to_energy(self):
        for d in self.dead:
            self.energy += d // 2
        self.dead = []

    def add_tree(self,age):
        self.tree.appendleft(age)

    def sort_tree(self):
        self.tree = sorted(self.tree)

    def get_tree(self):
        return self.tree

    def add_energy(self, amount):
        self.energy += amount

    def __repr__(self):
        return f'Trees: {self.tree}, Energy: {self.energy}'

n,m,k = map(int,input().split())
grid = [[Land() for _ in range(n)] for _ in range(n)]
A = [list(map(int,input().split())) for _ in range(n)]
for _ in range(m):
    x,y,z = map(int,input().split())
    grid[x-1][y-1].add_tree(z)

for i in range(n):
    for j in range(n):
        grid[i][j].sort_tree()

def spring():
    for i in range(n):
        for j in range(n):
            grid[i][j].feed_tree()

def summer():
    for i in range(n):
        for j in range(n):
            grid[i][j].dead_to_energy()

def fall():
    dy = [0,-1,-1,-1,0,1,1,1]
    dx = [1,1,0,-1,-1,-1,0,1]

    def grow(y,x):
        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < n:
                grid[ny][nx].add_tree(1)

    for y in range(n):
        for x in range(n):
            for tree in grid[y][x].get_tree():
                if tree % 5 == 0:
                    grow(y,x)

def winter():
    for i in range(n):
        for j in range(n):
            grid[i][j].add_energy(A[i][j])

for _ in range(k):
    spring()
    summer()
    fall()
    winter()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(grid[i][j].get_tree())
print(ans)