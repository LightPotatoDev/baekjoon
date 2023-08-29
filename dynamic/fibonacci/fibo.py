n = int(input())

cnt = 0
def fib(n):
    global cnt
    if n == 1 or n == 2:
        return 1
    else:
        cnt += 1
        return fib(n-1)+fib(n-2)

fib(n)
print(cnt+1, n-2)