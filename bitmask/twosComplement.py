n = int(input())

def complement(b):
    ones = '1' * 32
    res = (int(b,2) ^ int(ones,2)) + 1
    return bin(res)[2:].zfill(32)

b = bin(n)[2:].zfill(32)
print(b)

n2 = (n ^ -n)
print(bin(n2))