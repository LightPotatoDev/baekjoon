l = int(input())
s = input()

total = 0
for i, x in enumerate(s):
    total += (ord(x)-96)* 31**i
print(total % 1234567891)