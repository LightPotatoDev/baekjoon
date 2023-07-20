N = int(input())
L = list(map(int, input().split()))
maximum = max(L)

L2 = [i/maximum*100 for i in L]
avg = sum(L2) / N
print(avg)