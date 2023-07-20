import sys

n = int(input())
L = list(map(int,sys.stdin.readline().split()))

def compress(L):
    unique_coords = sorted(set(L))
    comp_vals = {}

    for i,x in enumerate(unique_coords):
        comp_vals[x] = i

    comp_coords = [comp_vals[x] for x in L]
    return comp_coords

print(' '.join(map(str,compress(L))))