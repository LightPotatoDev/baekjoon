T = int(input())
for _ in range(T):
    n = int(input())
    if n == 1:
        print(1)
    else:
        print(pow(2,n-2,int(1e9)+7))