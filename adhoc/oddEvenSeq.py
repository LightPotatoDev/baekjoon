n = int(input())
L = list(map(lambda x:int(x)%2, input().split()))
print(int(L.count(0) == n//2 and L.count(1) == (n+1)//2))