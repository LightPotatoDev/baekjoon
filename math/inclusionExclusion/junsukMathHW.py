T = int(input())
L = list(map(int,input().split()))
for i in L:
    three = (3 * (i//3) * (i//3+1)) // 2
    seven = (7 * (i//7) * (i//7+1)) // 2
    dupe = (21 * (i//21) * (i//21+1)) // 2
    print(three + seven - dupe)