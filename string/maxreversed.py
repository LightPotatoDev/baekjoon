a, b = input().split()
a2, b2 = a[::-1], b[::-1]
print(max(int(a2), int(b2)))