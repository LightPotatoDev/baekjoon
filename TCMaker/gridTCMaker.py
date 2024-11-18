import random

n,m = map(int,input().split())
min_n, max_n = map(int,input().split())
add_space = int(input())

f = open('gridTC.txt', 'w')
f.write(str(n) + ' ' + str(m) + '\n')
for _ in range(n):
    for _ in range(n):
        f.write(str(random.randint(min_n, max_n)))
        if add_space != 0:
            f.write(' ')
    f.write('\n')

f.close()
