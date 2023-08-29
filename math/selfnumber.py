L = [0] * 10001
def adding(n):
    A = []
    for i in range(5):
        A.append((n%10**(i+1))//(10**i))
    return sum(A)+n

for i in range(1,10001):
    if L[i] == 0:
        L[i] = 2
        j = i
        while True:
            j = adding(j)
            if j > 10000:
                break
            L[j] = 1

for i in range(10001):
    if L[i] == 2:
        print(i)