n = int(input())

L = []
for _ in range(n):
    L.append(list(map(int,input().split())))

white = 0
blue = 0

def sum_2d(L):
    return sum([sum(i) for i in L])

def cut(L):
    L1 = [L[i][0:size//2] for i in range(0,size//2)]
    L2 = [L[i][size//2:size] for i in range(0,size//2)]
    L3 = [L[i][0:size//2] for i in range(size//2,size)]
    L4 = [L[i][size//2:size] for i in range(size//2,size)]
    return [L1,L2,L3,L4]

checkL = [L]
while checkL:
    L_cur = checkL[0]
    size = len(L_cur)

    if sum_2d(L_cur) == 0:
        white += 1
    elif sum_2d(L_cur) == size ** 2:
        blue += 1
    else:
        for i in cut(L_cur):
            checkL.append(i)
    checkL.pop(0)

print(white)
print(blue)