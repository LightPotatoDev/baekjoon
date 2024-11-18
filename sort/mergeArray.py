n,m = map(int,input().split())
L = list(map(int,input().split())) + list(map(int,input().split()))
L.sort()
print(*L)