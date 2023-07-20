import sys

n = int(input())
L = list(map(int,sys.stdin.readline().split()))
L.sort()
l = len(L)
m = int(input())

def binarysearch(i,l,L):
    low = 0
    high = l-1
    while low <= high:
        mid = low + (high-low) // 2
        if L[mid] == i:
            return 1
        elif L[mid] < i:
            low = mid + 1
        else:
            high = mid - 1
    return 0

for i in (list(map(int,sys.stdin.readline().split()))):
    print(binarysearch(i,l,L))
