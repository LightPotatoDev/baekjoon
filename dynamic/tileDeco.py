n = int(input())
Fib = [1,1]

for _ in range(n-2):
    Fib.append(Fib[-1]+Fib[-2])

if n == 1:
    print(4)
else:
    print(4*Fib[-1]+2*Fib[-2])