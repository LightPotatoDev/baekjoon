import sys

print(3,22)
sys.stdout.flush()

grid_front = [[1]*22 for _ in range(3)]
grid_back = [[1]*22 for _ in range(3)]

D,L,U,R = 1,2,3,4
FIN_Y = 1
FIN_X = 21

grid_front[0][0] = D
grid_front[0][1] = R
grid_front[1][0] = R
grid_front[1][1] = R

grid_front[1][2] = R
grid_back[1][2] = R
grid_front[2][2] = U
grid_back[2][2] = U
for j in range(3,22):
    grid_front[1][j] = R
    grid_back[1][j] = D
    grid_front[2][j] = L
    grid_back[2][j] = L

grid_front[FIN_Y][FIN_X] = 0
grid_back[FIN_Y][FIN_X] = 0

for g in grid_front:
    print(''.join(map(str,g)))
    sys.stdout.flush()
for g in grid_back:
    print(''.join(map(str,g)))
    sys.stdout.flush()
print(2,2)
sys.stdout.flush()

k = int(input())
if k%4 == 0:
    grid_front[0][1] = L
    grid_front[1][1] = U
    grid_back[1][1] = R
elif k%4 == 2:
    grid_front[1][1] = L
    grid_back[1][1] = R
elif k%4 == 3:
    grid_front[1][1] = U
    grid_back[1][1] = R
    grid_front[0][1] = D

n = (k-1)//4
b = "{0:018b}".format(n)
for i in range(18):
    if b[17-i] == '1':
        grid_front[1][3+i] = D
        grid_back[1][3+i] = R

for g in grid_front:
    print(''.join(map(str,g)))
    sys.stdout.flush()
for g in grid_back:
    print(''.join(map(str,g)))
    sys.stdout.flush()