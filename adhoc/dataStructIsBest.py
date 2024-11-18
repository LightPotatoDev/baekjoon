n,m = map(int,input().split())

for _ in range(m):
    k = int(input())
    L = list(map(int,input().split()))
    for i in range(k-1):
        if L[i] < L[i+1]:
            print("No")
            exit(0)

print("Yes")