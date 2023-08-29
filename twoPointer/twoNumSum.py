n = int(input())
L = list(map(int,input().split()))
x = int(input())

L.sort()
i = 0
j = n-1

cnt = 0
while i < j:
    if L[i]+L[j] > x:
        j -= 1
    elif L[i]+L[j] < x:
        i += 1
    else:
        cnt += 1
        j -= 1
        i += 1
print(cnt)