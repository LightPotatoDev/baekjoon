n = int(input())
mask = 2**(len(bin(n))-2)-1

if n == mask:
    print(1)
    print(n)
else:
    print(2)
    print(n^mask)
    print(n)