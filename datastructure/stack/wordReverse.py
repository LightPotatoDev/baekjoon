n = int(input())
for i in range(1,n+1):
    L = input().split()
    print(f"Case #{i}: {' '.join(L[::-1])}")