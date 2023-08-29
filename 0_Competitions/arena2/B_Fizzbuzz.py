L = [input() for _ in range(3)]
n = 0
ind = 0
for i,x in enumerate(L):
    if x.isdigit():
        n = int(x)
        ind = i

next = n + (3-ind)
if next%15 == 0:
    print("FizzBuzz")
elif next%3 == 0:
    print("Fizz")
elif next%5 == 0:
    print("Buzz")
else:
    print(next)