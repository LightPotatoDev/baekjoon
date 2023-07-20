s = int(input())

total = 0
i = 0
while total < s:
    i += 1
    total += i

if total != s:
    print(i-1)
else:
    print(i)