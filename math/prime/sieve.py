n,k = map(int,input().split())
L = [0] * (n+1)
for i in range(2,n+1):
    if L[i] == 0:
        j = i
        while j <= n:
            if L[j] == 0:
                L[j] = 1
                k -= 1
            if k == 0:
                print(j)
                exit()
            j += i
