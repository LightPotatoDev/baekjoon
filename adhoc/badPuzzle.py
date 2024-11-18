from collections import deque

n = int(input())
A = deque(map(int,input().split()))
B = deque(map(int,input().split()))
C = B.copy()
C.reverse()

while A[0] != B[0]:
    p = A.popleft()
    A.append(p)

if A == B:
    print('good puzzle')
    exit(0)

while A[0] != C[0]:
    p = A.popleft()
    A.append(p)

if A == C:
    print('good puzzle')
    exit(0)


print('bad puzzle')