n = int(input())
L = list(map(int,input().split()))

totalMax = -1000
total = 0
for i in range(n):
    total += L[i]

    if totalMax < total:
        totalMax = total

    if total < 0:
        total = 0

print(totalMax)

""" by totwjfakd
for i in range(1, n) :
    arr[i] = max(arr[i-1]+arr[i], arr[i])
"""