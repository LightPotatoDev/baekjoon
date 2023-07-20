#simulation code

L = ['1','2','3','4','5','6','7','8','9']

n = 100
for a in range(2,n+1):
    A = []
    for i in L:
        if i[-1] == '0':
            A.append(i+str(int(i[-1])+1))
        elif i[-1] == '9':
            A.append(i+str(int(i[-1])-1))
        else:
            A.append(i+str(int(i[-1])+1))
            A.append(i+str(int(i[-1])-1))

    zeros = 0
    ones = 0
    eights = 0
    nines = 0
    for i in A:
        if i[-1] == '0':
            zeros += 1
        if i[-1] == '9':
            nines += 1

    print(f"n={a:3}: len = {len(A):8}, zeros = {zeros:7}, nines = {nines:7}, total = {(zeros+nines):7}")

    L = A[:]

print(len(L))

"""
1 9
2 17     = 9*2   - 1   = 9*2 - 1
3 32     = 17*2  - 2   = 18*2 - 4
4 61     = 32*2  - 3   = 36*2 - 11
5 116    = 61*2  - 6   = 72*2 - 16
6 222    = 116*2 - 10
7 424    = 222*2 - 20
8 813    = 424*2 - 35
9 1556   = 813*2 - 70
10 2986
11 5721
12 10982
13 21053
14 40416
15 77505
16 148785
17 285380
18 547810
19 1050876
20 2017126
21 3869845
22 7427671
"""