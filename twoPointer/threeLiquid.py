n = int(input())
L = list(map(int,input().split()))
L.sort()
Mix = [0,0,0]
optimal = int(3e9)

def twoPointer(k):
    global Mix
    global optimal

    i = k+1
    j = n-1
    while i < j:
        val = L[k] + L[i] + L[j]
        if abs(val) < abs(optimal):
            Mix = [L[k],L[i],L[j]]
            optimal = val

        if val < 0:
            i += 1
        elif val > 0:
            j -= 1
        else:
            print(*Mix)
            exit()

for k in range(n-2):
    twoPointer(k)
print(*Mix)
