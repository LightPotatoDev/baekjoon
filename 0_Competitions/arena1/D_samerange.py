n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

minmaxA = [0]*n
minmaxB = [0]*n
minNA = int(1e9)
maxNB = 0
for i in range(n):
