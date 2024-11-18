d,k = map(int,input().split())

fibo = [0,1,1]
for _ in range(30):
    fibo.append(fibo[-1] + fibo[-2])
a_coef = fibo[d-2]
b_coef = fibo[d-1]

for a in range(1,100000):
    if (k - a_coef*a) % b_coef == 0:
        b = (k - a_coef*a) // b_coef
        print(a)
        print(b)
        break