n = int(input())
A = []
q = 0
for i in range(n):
    inp = input()
    if inp == "?":
        q = i
    A.append(inp)

m = int(input())
B = []
for _ in range(m):
    B.append(input())

for i in B:
    if (q == 0 or i[0] == A[q-1][-1]) and (q == n-1 or i[-1] == A[q+1][0]):
        if i not in A:
            print(i)
            break