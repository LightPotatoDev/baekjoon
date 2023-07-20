n,r,c = map(int,input().split())
y_bound = [0,2**n-1]
x_bound = [0,2**n-1]
value = 0

for i in range(n, 0, -1):
    if r <= (y_bound[0]+y_bound[1]) // 2:
        y_bound[1] -= 2**(i-1)
    else:
        y_bound[0] += 2**(i-1)
        value += 4**(i-1) * 2

    if c <= (x_bound[0]+x_bound[1]) // 2:
        x_bound[1] -= 2**(i-1)
    else:
        x_bound[0] += 2**(i-1)
        value += 4**(i-1)

print(value)