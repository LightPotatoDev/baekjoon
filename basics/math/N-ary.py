nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

value = ""
n, b = map(int,input().split())

size = 0
while n >= b ** size:
    size += 1

for i in range(size):
    div = b ** (size - i - 1)
    value += nums[n // div]
    n -= (n//div) * div

print(value)