w,n = map(int,input().split())
L = list(map(int,input().split()))
L.sort()

two_sum = [0] * 400000
for i in range(n):
    for j in range(i+1,n):
        two_sum[L[i]+L[j]] = (i,j)

def parcel():
    for i in range(n):
        for j in range(i+1,n):
            target = w - L[i] - L[j]
            if not (0 < target < 400000):
                break
            if two_sum[target] != 0 and (i not in two_sum[target]) and (j not in two_sum[target]):
                return "YES"

    return "NO"

print(parcel())