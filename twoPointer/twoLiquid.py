n = int(input())
L = list(map(int,input().split()))
i = 0
j = n-1
Mix = [0,0]
optimal = int(2e9)

L.sort()
while i < j:
    val = L[i] + L[j]
    if abs(val) < abs(optimal):
        Mix = [L[i],L[j]]
        optimal = val

    if val < 0:
        i += 1
    elif val > 0:
        j -= 1
    else:
        print(*Mix)
        exit()

print(*Mix)
