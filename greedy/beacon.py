import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int,input().split()))
L.sort()
print(L[(len(L)-1)//2])