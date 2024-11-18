n = int(input())
gacha = list(map(int,input().split()))

order = []
for i in range(n):
    order.insert(gacha[i],i+1)
print(*order[::-1])