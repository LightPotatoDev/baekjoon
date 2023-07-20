def getI(i,j,k):
    return 441*i+21*j+k

while True:
    a,b,c = map(int,input().split())

    if a== -1 and b == -1 and c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        print(f"w({a}, {b}, {c}) = 1")
        continue
    if a > 20 or b > 20 or c > 20:
        print(f"w({a}, {b}, {c}) = 1048576")
        continue

    L = [0 for _ in range(21**3)]

    for i in range(21):
        for j in range(21):
            for k in range(21):
                if i <= 0 or j <= 0 or k <= 0:
                    L[getI(i,j,k)] = 1
                elif i < j and j < k:
                    L[getI(i,j,k)] = L[getI(i,j,k-1)] + L[getI(i,j-1,k-1)] - L[getI(i,j-1,k)]
                else:
                    L[getI(i,j,k)] = L[getI(i-1,j,k)] + L[getI(i-1,j-1,k)] + L[getI(i-1,j,k-1)] - L[getI(i-1,j-1,k-1)]

    print(f"w({a}, {b}, {c}) = {L[getI(a,b,c)]}")