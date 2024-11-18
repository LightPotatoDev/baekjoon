from itertools import permutations
from copy import deepcopy

L = list(map(int,input().split()))
perm = []
for i in permutations(L):
    perm.append(list(i))

label = [-1]*len(perm)

ax1 = [0,1,4,3]
ax2 = [0,2,4,5]
ax3 = [1,2,3,5]

def rotate(d,axis,times):
    for _ in range(times):
        t = d[axis[0]]
        for j in range(3):
            d[axis[j]] = d[axis[j+1]]
        d[axis[3]] = t

    return d[:]

def rotate_die(d):
    same = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                d_dupe = d[:]
                d_dupe = rotate(d_dupe,ax1,i)
                d_dupe = rotate(d_dupe,ax2,j)
                d_dupe = rotate(d_dupe,ax3,k)
                same.append(d_dupe[:])
    return same

for i in range(len(perm)):
    if label[i] != -1:
        continue
    same_dice = rotate_die(perm[i])
    for j,p in enumerate(perm):
        if label[j] == -1 and p in same_dice:
            label[j] = i

print(len(set(label)))