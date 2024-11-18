k = int(input())
L = list(input().split())

def reverse(A,a,b):
    B = A[a:b]
    for i in range(a,b):
        A[i] = B[b-i-1]
    return A

max_ans = [9-i for i in range(k+1)]
max_rev = []
rev = []
for i,x in enumerate(L):
    if x == '<':
        rev.append(i)
    elif x == '>':
        max_rev.append(rev)
        rev = []
    if i == k-1:
        max_rev.append(rev)

for r in max_rev:
    if r:
        a,b = r[0],r[-1]+2
        max_ans = reverse(max_ans,a,b)

print(''.join(map(str,max_ans)))

min_ans = [i for i in range(k+1)]
min_rev = []
rev = []
for i,x in enumerate(L):
    if x == '>':
        rev.append(i)
    elif x == '<':
        min_rev.append(rev)
        rev = []
    if i == k-1:
        min_rev.append(rev)

for r in min_rev:
    if r:
        a,b = r[0],r[-1]+2
        min_ans = reverse(min_ans,a,b)

print(''.join(map(str,min_ans)))