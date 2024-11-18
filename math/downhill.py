n,h = map(int,input().split())
if n == 0:
    print(h)
    exit()

A = [h] + list(map(int,input().split())) + [0]
A = A[::-1]
rope = 0

for i in range(n+1):
    rope_add = max(0,A[i+1]-A[i] - rope/2)
    rope += rope_add

print(rope)
