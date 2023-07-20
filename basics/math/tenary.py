nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

value = 0
n, b = input().split()
b = int(b)

for i in range(len(n)):
    value += nums.index(n[len(n) - i - 1]) * b ** i

print(value)