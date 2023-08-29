n = int(input())
L = [0,0]

for _ in range(n):
    L[int(input())] += 1

if L[0] > L[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")