from bisect import bisect_right

n = int(input())
L = [int(input()) for _ in range(n)]
L.sort(reverse = True)
point = 0
cutline = (60,100,140,200,250)
for i in L[:42]:
    point += bisect_right(cutline,i)
print(sum(L[:42]), point)
