n = int(input())
k = int(input())
L = list(map(int,input().split()))
L.sort()
diff = [L[i+1]-L[i] for i in range(n-1)]
diff.sort()
if n-k <= 0:
    print(0)
else:
    print(sum(diff[:n-k]))
