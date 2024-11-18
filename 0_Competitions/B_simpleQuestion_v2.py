n,p = map(int,input().split())
B = list(map(int,input().split()))

num = [p]*(n//p)
if n%p != 0:
    num.append(n%p)

for i in range(n):
    if i == 0:
        if B[i] != 1:
            print("NO")
            exit()
    if i != 0:
        if not (0 <= B[i]-B[i-1] <= 1):
            print("NO")
            exit()
    if B[i] > len(num):
        print("NO")
        exit()

i = 0
j = 0
for x in B:
    if i == j and x != i+1:
        print("NO")
        exit()
    if not (x == j or x == j+1):
        print("NO")
        exit()
    if x == j+1:
        num[j] -= 1
        j += 1
    else:
        num[i] -= 1
        if num[i] < 0:
            print("NO")
            exit()
        if num[i] == 0:
            i += 1

print("YES")

