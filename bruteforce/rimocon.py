from itertools import product

n = int(input())
m = int(input())
available = [0,1,2,3,4,5,6,7,8,9]
if m != 0:
    L = map(int,input().split())
    for i in L:
        available.remove(i)
options = set()

#1. + 혹은 -만 누르는 경우
options.add(abs(n-100))

#2. 숫자 버튼도 누르는 경우
prod = []
for i in range(1,7):
    prod += list(product(available,repeat=i))
for i in prod:
    gen = int(''.join(map(str,i)))
    options.add(len(str(gen)) + abs(gen-n))

print(min(options))