n = int(input())
L = list(map(int,input().split()))
L.remove(max(L))
print(sum(L))