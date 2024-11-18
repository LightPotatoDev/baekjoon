k = int(input())
buy,cut = 0,0

if k.bit_count() == 1:
    print(k,0)
    exit()

for i,x in enumerate(str(bin(k))[2:]):
    buy = 2**(i+1)
    if x == '1':
        cut = i+1
print(buy,cut)